// Navegación móvil + animaciones sutiles al hacer scroll.
(function () {
  // Menú móvil
  var toggle = document.getElementById("navToggle");
  var links = document.getElementById("navLinks");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      links.classList.toggle("is-open");
      toggle.classList.toggle("is-open");
    });
  }

  // Selector de idioma
  var langSelect = document.getElementById("langSelect");
  if (langSelect) {
    langSelect.addEventListener("change", function () {
      window.location.href = "/lang/" + this.value;
    });
  }

  // Header con sombra al hacer scroll
  var nav = document.getElementById("nav");
  if (nav) {
    var onScroll = function () {
      nav.classList.toggle("is-scrolled", window.scrollY > 20);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  // Reveal on scroll (fade-in / slide-in)
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && reveals.length) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12 }
    );
    reveals.forEach(function (el) {
      io.observe(el);
    });
  } else {
    reveals.forEach(function (el) {
      el.classList.add("is-visible");
    });
  }
})();
