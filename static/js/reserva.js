// Lógica del formulario de reserva: límites por vehículo, campos de vuelo
// condicionales y autocompletado de Google Maps (con ahorro de llamadas).
(function () {
  var form = document.querySelector(".reserva-form");
  if (!form) return;

  var capacidades = {};
  try {
    capacidades = JSON.parse(form.getAttribute("data-capacidades") || "{}");
  } catch (e) {
    capacidades = {};
  }

  // Textos traducidos (vienen de los atributos data- del formulario)
  var T = {
    hintPax: form.getAttribute("data-hint-pax") || "Máx. {n} pax.",
    hintLuggage: form.getAttribute("data-hint-luggage") || "Hasta {n}.",
    locLoading: form.getAttribute("data-loc-loading") || "…",
    locDone: form.getAttribute("data-loc-done") || "OK",
  };

  var servicioSel = document.getElementById("servicio_id");
  var pax = document.getElementById("num_pasajeros");
  var maletas = document.getElementById("num_maletas");
  var paxHint = document.getElementById("paxHint");
  var maletasHint = document.getElementById("maletasHint");
  var fecha = document.getElementById("fecha_servicio");

  // No permitir fechas pasadas
  if (fecha) {
    var hoy = new Date().toISOString().split("T")[0];
    fecha.min = hoy;
  }

  // Ajusta máximos de pasajeros/maletas según el vehículo elegido
  function aplicarCapacidad() {
    var cap = capacidades[servicioSel && servicioSel.value];
    if (!cap) {
      if (paxHint) paxHint.textContent = "";
      if (maletasHint) maletasHint.textContent = "";
      return;
    }
    if (pax) {
      pax.max = cap.max;
      pax.min = cap.min;
      if (parseInt(pax.value || "0", 10) > cap.max) pax.value = cap.max;
      if (parseInt(pax.value || "0", 10) < cap.min) pax.value = cap.min;
    }
    if (maletas) {
      maletas.max = cap.maletas;
      if (parseInt(maletas.value || "0", 10) > cap.maletas) maletas.value = cap.maletas;
    }
    if (paxHint) paxHint.textContent = T.hintPax.replace("{n}", cap.max);
    if (maletasHint) maletasHint.textContent = T.hintLuggage.replace("{n}", cap.maletas);
  }
  if (servicioSel) {
    servicioSel.addEventListener("change", aplicarCapacidad);
    aplicarCapacidad();
  }

  // Campos de vuelo visibles solo si recogida/destino menciona "aeropuerto"
  var recogida = document.getElementById("punto_recogida");
  var destino = document.getElementById("destino");
  var vueloBlock = document.getElementById("vueloBlock");
  var numeroVuelo = document.getElementById("numero_vuelo");

  function esAeropuerto(v) {
    return /aeropuerto|airport|jose maria cordova|jmc|rionegro|olaya herrera/i.test(v || "");
  }
  function revisarVuelo() {
    if (!vueloBlock) return;
    var mostrar = esAeropuerto(recogida && recogida.value) || esAeropuerto(destino && destino.value);
    vueloBlock.hidden = !mostrar;
    if (numeroVuelo) numeroVuelo.required = mostrar;
  }
  if (recogida) recogida.addEventListener("input", revisarVuelo);
  if (destino) destino.addEventListener("input", revisarVuelo);
  revisarVuelo();

  // -------- Lista de lugares frecuentes (definidos por el admin) -----------
  var lugares = document.getElementById("lugares_frecuentes");
  if (lugares && recogida) {
    lugares.addEventListener("change", function () {
      var opt = lugares.options[lugares.selectedIndex];
      if (!opt || !opt.value) return;
      recogida.value = opt.value;
      var lat = document.getElementById("recogida_lat");
      var lng = document.getElementById("recogida_lng");
      if (lat) lat.value = opt.getAttribute("data-lat") || "";
      if (lng) lng.value = opt.getAttribute("data-lng") || "";
      revisarVuelo();
    });
  }

  // -------- Botón "Mi ubicación" (GPS del celular) -------------------------
  var btnUbic = document.getElementById("btnMiUbicacion");
  if (btnUbic && recogida) {
    btnUbic.addEventListener("click", function () {
      if (!navigator.geolocation) {
        alert("Tu navegador no permite obtener la ubicación.");
        return;
      }
      var txt = btnUbic.textContent;
      btnUbic.textContent = T.locLoading;
      btnUbic.disabled = true;

      navigator.geolocation.getCurrentPosition(
        function (pos) {
          var la = pos.coords.latitude;
          var ln = pos.coords.longitude;
          document.getElementById("recogida_lat").value = la;
          document.getElementById("recogida_lng").value = ln;

          // Si Maps está cargado, una sola llamada para obtener la dirección.
          if (window.google && google.maps && google.maps.Geocoder) {
            new google.maps.Geocoder().geocode(
              { location: { lat: la, lng: ln } },
              function (results, status) {
                if (status === "OK" && results[0]) {
                  recogida.value = results[0].formatted_address;
                } else {
                  recogida.value = "Mi ubicación (" + la.toFixed(5) + ", " + ln.toFixed(5) + ")";
                }
                revisarVuelo();
              }
            );
          } else {
            recogida.value = "Mi ubicación (" + la.toFixed(5) + ", " + ln.toFixed(5) + ")";
            revisarVuelo();
          }
          btnUbic.textContent = T.locDone;
          btnUbic.disabled = false;
        },
        function () {
          alert("No se pudo obtener tu ubicación. Revisa los permisos del navegador.");
          btnUbic.textContent = txt;
          btnUbic.disabled = false;
        },
        { enableHighAccuracy: true, timeout: 10000 }
      );
    });
  }

  // -------- Google Maps Places Autocomplete --------------------------------
  // Estrategia de ahorro: un único "session token" para agrupar la facturación
  // por sesión (no por tecla) y guardar las coordenadas en campos ocultos para
  // no volver a consultar la API después.
  window.initMapsAutocomplete = function () {
    if (!(window.google && google.maps && google.maps.places)) return;

    var sessionToken = new google.maps.places.AutocompleteSessionToken();
    var opciones = {
      componentRestrictions: { country: "co" }, // Colombia (cambia o quita si operas en otros países)
      fields: ["name", "formatted_address", "geometry"],
      sessionToken: sessionToken,
    };

    function conectar(input, latId, lngId) {
      if (!input) return;
      var ac = new google.maps.places.Autocomplete(input, opciones);
      ac.addListener("place_changed", function () {
        var place = ac.getPlace();
        var lat = document.getElementById(latId);
        var lng = document.getElementById(lngId);
        if (place && place.geometry && place.geometry.location) {
          if (lat) lat.value = place.geometry.location.lat();
          if (lng) lng.value = place.geometry.location.lng();
          if (place.name && place.formatted_address) {
            input.value = place.name + " — " + place.formatted_address;
          }
        }
        revisarVuelo();
        // Token nuevo tras cada selección (cierra la sesión facturable)
        sessionToken = new google.maps.places.AutocompleteSessionToken();
        opciones.sessionToken = sessionToken;
      });
      // Si el usuario escribe a mano, invalidamos coordenadas previas
      input.addEventListener("input", function () {
        var lat = document.getElementById(latId);
        var lng = document.getElementById(lngId);
        if (lat) lat.value = "";
        if (lng) lng.value = "";
      });
    }

    conectar(recogida, "recogida_lat", "recogida_lng");
    conectar(destino, "destino_lat", "destino_lng");
  };
})();
