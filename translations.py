# -*- coding: utf-8 -*-
"""
Traducciones de la interfaz pública.

Idioma principal: inglés (en). Opciones: español (es), alemán (de), chino (zh).
Para agregar/editar textos, modifica los diccionarios de abajo. Cada clave existe
en los 4 idiomas; si falta una, se usa la versión en inglés como respaldo.
"""

# Idiomas disponibles en el selector (código, etiqueta mostrada)
LANGS = [
    ("en", "English"),
    ("es", "Español"),
    ("de", "Deutsch"),
    ("zh", "中文"),
]
DEFAULT_LANG = "en"


TRANSLATIONS = {
    # ======================================================================
    "en": {
        "lang.label": "Language",
        "nav.home": "Home", "nav.services": "Services", "nav.about": "About Us", "nav.book": "Book",
        "nav.login": "Login",

        "hero.title_a": "Executive &", "hero.title_b": "transport, tailored to you",
        "hero.sub": "Professional chauffeurs, guaranteed punctuality and premium care for local and international clients.",
        "hero.book_now": "Book now", "hero.see_services": "View services",

        "home.fleet_eyebrow": "Our fleet", "home.featured": "Featured services",
        "home.featured_lead": "Choose the ideal vehicle for your transfer and book it in seconds.",
        "common.book": "Book", "common.book_name": "Book", "common.passengers": "passengers",
        "home.diff_eyebrow": "The difference", "home.why": "Why choose us?",
        "feat.1.t": "Guaranteed punctuality", "feat.1.d": "We arrive before you do. Your time comes first.",
        "feat.2.t": "Professional chauffeurs", "feat.2.d": "Trained, discreet and trustworthy drivers.",
        "feat.3.t": "International service", "feat.3.d": "We welcome clients from around the world with premium care.",
        "feat.4.t": "Flight tracking", "feat.4.d": "We monitor your flight in real time to adapt.",
        "feat.5.t": "24/7 availability", "feat.5.d": "We are ready any time, every day.",
        "feat.6.t": "High-end vehicles", "feat.6.d": "A modern, comfortable and always spotless fleet.",
        "cta.title": "Ready for your next transfer?",
        "cta.text": "Book online and get confirmation from our team within minutes.",

        "services.eyebrow": "Catalog", "services.title": "Our services",
        "services.lead": "Every service includes a professional chauffeur. Choose the one that best fits your trip and book it instantly.",
        "services.capacity": "Capacity", "services.luggage": "Luggage", "services.up_to": "up to",
        "services.suitcases": "suitcases", "services.ideal_for": "Ideal for",

        "about.eyebrow": "About us", "about.title": "Excellence in every journey",
        "about.lead_1": "was created to deliver a premium transport experience in",
        "about.lead_2": ", where punctuality, safety and discretion are not an extra — they are the standard.",
        "about.history_h": "Our story",
        "about.history_p": "We started with a simple idea: that getting around the city could feel as comfortable and reliable as flying first class. Today we serve executives, families and international travelers with a service designed down to the last detail.",
        "about.mission_h": "Mission",
        "about.mission_p": "To provide safe, punctual and high-quality transfers, exceeding every client's expectations on every trip.",
        "about.vision_h": "Vision",
        "about.vision_p": "To be the leading executive transport company in the region, recognized for operational excellence and a human touch.",
        "about.values_eyebrow": "What defines us", "about.values_title": "Our values",
        "value.1.t": "Punctuality", "value.1.d": "We respect your time as if it were our own.",
        "value.2.t": "Safety", "value.2.d": "Inspected vehicles and certified drivers.",
        "value.3.t": "Discretion", "value.3.d": "Total confidentiality in every service.",
        "value.4.t": "Hospitality", "value.4.d": "Warm, professional care from start to finish.",

        "res.eyebrow": "Online booking", "res.title": "Request your transfer",
        "res.lead": "Fill out the form and our team will confirm your booking within 30 minutes.",
        "res.step1": "1 · Service", "res.service_label": "Service type *", "res.service_ph": "Select a vehicle…",
        "res.pax_short": "pax",
        "res.step2": "2 · Trip", "res.date": "Service date *", "res.time": "Pickup time *",
        "res.pickup": "Pickup point *", "res.pickup_choose": "— Choose a frequent place —",
        "res.pickup_ph": "Hotel, building, airport or address…",
        "res.my_location": "My location", "res.my_location_loading": "Getting location…",
        "res.my_location_done": "✓ Location ready",
        "res.pickup_hint": "Choose a frequent place, type the address, or use your current location.",
        "res.destination": "Destination *", "res.dest_ph": "Hotel, building, airport or address…",
        "res.flight_no": "Flight number", "res.flight_ph": "e.g. AV 8520",
        "res.airline": "Airline", "res.airline_ph": "e.g. Avianca",
        "res.passengers": "Number of passengers *", "res.luggage": "Number of suitcases",
        "res.hint_pax": "Maximum {n} passengers for this vehicle.", "res.hint_luggage": "Up to {n} suitcases.",
        "res.step3": "3 · Your details", "res.fullname": "Full name *", "res.whatsapp": "WhatsApp *",
        "res.phone_ph": "300 000 0000", "res.email": "Email", "res.email_ph": "you@example.com",
        "res.doc_type": "Document type *", "res.doc_num": "Document number",
        "res.comments": "Additional comments", "res.comments_ph": "Baby seat, special luggage, instructions…",
        "res.submit": "Confirm booking",
        "res.note": "* Required fields. After sending, we'll receive your request and contact you to confirm.",

        "err.name": "Name must be at least 3 characters.",
        "err.phone": "Phone / WhatsApp is required.",
        "err.date_req": "Service date is required.",
        "err.date_past": "The date cannot be in the past.",
        "err.date_invalid": "Invalid date.",
        "err.time": "Pickup time is required.",
        "err.pickup": "Pickup point is required.",
        "err.destination": "Destination is required.",

        "conf.title": "Your booking was received!",
        "conf.lead": "We'll contact you within 30 minutes to confirm the details of your transfer.",
        "conf.whatsapp": "Message us on WhatsApp", "conf.back": "Back to home",

        "footer.contact": "Contact", "footer.follow": "Follow us", "footer.company": "Company",
        "footer.privacy": "Privacy Policy", "footer.rights": "All rights reserved.",
    },

    # ======================================================================
    "es": {
        "lang.label": "Idioma",
        "nav.home": "Inicio", "nav.services": "Servicios", "nav.about": "Quiénes Somos", "nav.book": "Reservar",
        "nav.login": "Acceder",

        "hero.title_a": "Transporte ejecutivo y", "hero.title_b": "a tu medida",
        "hero.sub": "Choferes profesionales, puntualidad garantizada y atención premium para clientes locales e internacionales.",
        "hero.book_now": "Reservar ahora", "hero.see_services": "Ver servicios",

        "home.fleet_eyebrow": "Nuestra flota", "home.featured": "Servicios destacados",
        "home.featured_lead": "Elige el vehículo ideal para tu traslado y resérvalo en segundos.",
        "common.book": "Reservar", "common.book_name": "Reservar", "common.passengers": "pasajeros",
        "home.diff_eyebrow": "La diferencia", "home.why": "¿Por qué elegirnos?",
        "feat.1.t": "Puntualidad garantizada", "feat.1.d": "Llegamos antes que tú. Tu tiempo es lo primero.",
        "feat.2.t": "Choferes profesionales", "feat.2.d": "Conductores capacitados, discretos y de confianza.",
        "feat.3.t": "Atención internacional", "feat.3.d": "Recibimos clientes de todo el mundo con trato premium.",
        "feat.4.t": "Seguimiento de vuelos", "feat.4.d": "Monitoreamos tu vuelo en tiempo real para ajustarnos.",
        "feat.5.t": "Disponibilidad 24/7", "feat.5.d": "Estamos listos a cualquier hora, todos los días.",
        "feat.6.t": "Vehículos de alta gama", "feat.6.d": "Flota moderna, cómoda y siempre impecable.",
        "cta.title": "¿Listo para tu próximo traslado?",
        "cta.text": "Reserva en línea y recibe confirmación de nuestro equipo en minutos.",

        "services.eyebrow": "Catálogo", "services.title": "Nuestros servicios",
        "services.lead": "Cada servicio incluye chofer profesional. Elige el que mejor se ajuste a tu viaje y resérvalo al instante.",
        "services.capacity": "Capacidad", "services.luggage": "Equipaje", "services.up_to": "hasta",
        "services.suitcases": "maletas", "services.ideal_for": "Ideal para",

        "about.eyebrow": "Quiénes somos", "about.title": "Excelencia en cada trayecto",
        "about.lead_1": "nace para ofrecer una experiencia de transporte premium en",
        "about.lead_2": ", donde la puntualidad, la seguridad y la discreción no son un extra: son el estándar.",
        "about.history_h": "Nuestra historia",
        "about.history_p": "Comenzamos con una idea simple: que moverse por la ciudad pudiera sentirse tan cómodo y confiable como viajar en primera clase. Hoy acompañamos a ejecutivos, familias y viajeros internacionales con un servicio pensado en cada detalle.",
        "about.mission_h": "Misión",
        "about.mission_p": "Brindar traslados seguros, puntuales y de alta calidad, superando las expectativas de cada cliente en cada viaje.",
        "about.vision_h": "Visión",
        "about.vision_p": "Ser la empresa de transporte ejecutivo de referencia en la región, reconocida por su excelencia operativa y su trato humano.",
        "about.values_eyebrow": "Lo que nos define", "about.values_title": "Nuestros valores",
        "value.1.t": "Puntualidad", "value.1.d": "Respetamos tu tiempo como si fuera el nuestro.",
        "value.2.t": "Seguridad", "value.2.d": "Vehículos revisados y conductores certificados.",
        "value.3.t": "Discreción", "value.3.d": "Confidencialidad total en cada servicio.",
        "value.4.t": "Hospitalidad", "value.4.d": "Un trato cálido y profesional de principio a fin.",

        "res.eyebrow": "Reserva en línea", "res.title": "Solicita tu traslado",
        "res.lead": "Completa el formulario y nuestro equipo confirmará tu reserva en menos de 30 minutos.",
        "res.step1": "1 · Servicio", "res.service_label": "Tipo de servicio *", "res.service_ph": "Selecciona un vehículo…",
        "res.pax_short": "pax",
        "res.step2": "2 · Trayecto", "res.date": "Fecha de servicio *", "res.time": "Hora de recogida *",
        "res.pickup": "Punto de recogida *", "res.pickup_choose": "— Elegir un lugar frecuente —",
        "res.pickup_ph": "Hotel, edificio, aeropuerto o dirección…",
        "res.my_location": "Mi ubicación", "res.my_location_loading": "Obteniendo…",
        "res.my_location_done": "✓ Ubicación lista",
        "res.pickup_hint": "Elige un lugar frecuente, escribe la dirección o usa tu ubicación actual.",
        "res.destination": "Destino *", "res.dest_ph": "Hotel, edificio, aeropuerto o dirección…",
        "res.flight_no": "Número de vuelo", "res.flight_ph": "Ej. AV 8520",
        "res.airline": "Aerolínea", "res.airline_ph": "Ej. Avianca",
        "res.passengers": "Número de pasajeros *", "res.luggage": "Número de maletas",
        "res.hint_pax": "Máximo {n} pasajeros para este vehículo.", "res.hint_luggage": "Hasta {n} maletas.",
        "res.step3": "3 · Tus datos", "res.fullname": "Nombre completo *", "res.whatsapp": "WhatsApp *",
        "res.phone_ph": "300 000 0000", "res.email": "Correo", "res.email_ph": "tucorreo@ejemplo.com",
        "res.doc_type": "Tipo de documento *", "res.doc_num": "Número de documento",
        "res.comments": "Comentarios adicionales", "res.comments_ph": "Silla para bebé, equipaje especial, instrucciones…",
        "res.submit": "Confirmar reserva",
        "res.note": "* Campos obligatorios. Al enviar, recibiremos tu solicitud y te contactaremos para confirmar.",

        "err.name": "El nombre debe tener al menos 3 caracteres.",
        "err.phone": "El teléfono / WhatsApp es obligatorio.",
        "err.date_req": "La fecha de servicio es obligatoria.",
        "err.date_past": "La fecha no puede ser en el pasado.",
        "err.date_invalid": "Fecha inválida.",
        "err.time": "La hora de recogida es obligatoria.",
        "err.pickup": "El punto de recogida es obligatorio.",
        "err.destination": "El destino es obligatorio.",

        "conf.title": "¡Tu reserva fue recibida!",
        "conf.lead": "Te contactaremos en menos de 30 minutos para confirmar los detalles de tu traslado.",
        "conf.whatsapp": "Escríbenos por WhatsApp", "conf.back": "Volver al inicio",

        "footer.contact": "Contacto", "footer.follow": "Síguenos", "footer.company": "Empresa",
        "footer.privacy": "Política de Privacidad", "footer.rights": "Todos los derechos reservados.",
    },

    # ======================================================================
    "de": {
        "lang.label": "Sprache",
        "nav.home": "Start", "nav.services": "Leistungen", "nav.about": "Über uns", "nav.book": "Buchen",
        "nav.login": "Anmelden",

        "hero.title_a": "Exklusiver &", "hero.title_b": "Transport nach Maß",
        "hero.sub": "Professionelle Chauffeure, garantierte Pünktlichkeit und erstklassiger Service für lokale und internationale Kunden.",
        "hero.book_now": "Jetzt buchen", "hero.see_services": "Leistungen ansehen",

        "home.fleet_eyebrow": "Unsere Flotte", "home.featured": "Top-Leistungen",
        "home.featured_lead": "Wählen Sie das ideale Fahrzeug für Ihren Transfer und buchen Sie in Sekunden.",
        "common.book": "Buchen", "common.book_name": "Buchen:", "common.passengers": "Passagiere",
        "home.diff_eyebrow": "Der Unterschied", "home.why": "Warum wir?",
        "feat.1.t": "Garantierte Pünktlichkeit", "feat.1.d": "Wir sind vor Ihnen da. Ihre Zeit zählt zuerst.",
        "feat.2.t": "Professionelle Chauffeure", "feat.2.d": "Geschulte, diskrete und vertrauenswürdige Fahrer.",
        "feat.3.t": "Internationaler Service", "feat.3.d": "Wir empfangen Kunden aus aller Welt mit Premium-Service.",
        "feat.4.t": "Flugverfolgung", "feat.4.d": "Wir verfolgen Ihren Flug in Echtzeit, um uns anzupassen.",
        "feat.5.t": "Verfügbar rund um die Uhr", "feat.5.d": "Wir sind jederzeit für Sie da, jeden Tag.",
        "feat.6.t": "Hochwertige Fahrzeuge", "feat.6.d": "Eine moderne, komfortable und stets makellose Flotte.",
        "cta.title": "Bereit für Ihren nächsten Transfer?",
        "cta.text": "Buchen Sie online und erhalten Sie innerhalb von Minuten eine Bestätigung unseres Teams.",

        "services.eyebrow": "Katalog", "services.title": "Unsere Leistungen",
        "services.lead": "Jede Leistung beinhaltet einen professionellen Chauffeur. Wählen Sie die passende für Ihre Reise und buchen Sie sofort.",
        "services.capacity": "Kapazität", "services.luggage": "Gepäck", "services.up_to": "bis zu",
        "services.suitcases": "Koffer", "services.ideal_for": "Ideal für",

        "about.eyebrow": "Über uns", "about.title": "Exzellenz auf jeder Fahrt",
        "about.lead_1": "wurde gegründet, um ein Premium-Transporterlebnis zu bieten in",
        "about.lead_2": ", wo Pünktlichkeit, Sicherheit und Diskretion kein Extra sind — sie sind der Standard.",
        "about.history_h": "Unsere Geschichte",
        "about.history_p": "Wir begannen mit einer einfachen Idee: dass die Fortbewegung in der Stadt so komfortabel und zuverlässig sein kann wie eine Reise in der ersten Klasse. Heute begleiten wir Führungskräfte, Familien und internationale Reisende mit einem bis ins Detail durchdachten Service.",
        "about.mission_h": "Mission",
        "about.mission_p": "Sichere, pünktliche und hochwertige Transfers anzubieten und die Erwartungen jedes Kunden auf jeder Fahrt zu übertreffen.",
        "about.vision_h": "Vision",
        "about.vision_p": "Das führende Unternehmen für Executive-Transport in der Region zu sein, anerkannt für operative Exzellenz und menschliche Nähe.",
        "about.values_eyebrow": "Was uns ausmacht", "about.values_title": "Unsere Werte",
        "value.1.t": "Pünktlichkeit", "value.1.d": "Wir respektieren Ihre Zeit, als wäre es unsere eigene.",
        "value.2.t": "Sicherheit", "value.2.d": "Geprüfte Fahrzeuge und zertifizierte Fahrer.",
        "value.3.t": "Diskretion", "value.3.d": "Absolute Vertraulichkeit bei jedem Service.",
        "value.4.t": "Gastfreundschaft", "value.4.d": "Herzlicher, professioneller Service von Anfang bis Ende.",

        "res.eyebrow": "Online-Buchung", "res.title": "Fordern Sie Ihren Transfer an",
        "res.lead": "Füllen Sie das Formular aus und unser Team bestätigt Ihre Buchung innerhalb von 30 Minuten.",
        "res.step1": "1 · Leistung", "res.service_label": "Art der Leistung *", "res.service_ph": "Fahrzeug auswählen…",
        "res.pax_short": "Pers.",
        "res.step2": "2 · Fahrt", "res.date": "Datum *", "res.time": "Abholzeit *",
        "res.pickup": "Abholort *", "res.pickup_choose": "— Häufigen Ort wählen —",
        "res.pickup_ph": "Hotel, Gebäude, Flughafen oder Adresse…",
        "res.my_location": "Mein Standort", "res.my_location_loading": "Wird ermittelt…",
        "res.my_location_done": "✓ Standort bereit",
        "res.pickup_hint": "Wählen Sie einen häufigen Ort, geben Sie die Adresse ein oder nutzen Sie Ihren aktuellen Standort.",
        "res.destination": "Ziel *", "res.dest_ph": "Hotel, Gebäude, Flughafen oder Adresse…",
        "res.flight_no": "Flugnummer", "res.flight_ph": "z. B. AV 8520",
        "res.airline": "Fluggesellschaft", "res.airline_ph": "z. B. Avianca",
        "res.passengers": "Anzahl der Passagiere *", "res.luggage": "Anzahl der Koffer",
        "res.hint_pax": "Maximal {n} Passagiere für dieses Fahrzeug.", "res.hint_luggage": "Bis zu {n} Koffer.",
        "res.step3": "3 · Ihre Daten", "res.fullname": "Vollständiger Name *", "res.whatsapp": "WhatsApp *",
        "res.phone_ph": "300 000 0000", "res.email": "E-Mail", "res.email_ph": "name@beispiel.com",
        "res.doc_type": "Dokumentart *", "res.doc_num": "Dokumentnummer",
        "res.comments": "Zusätzliche Hinweise", "res.comments_ph": "Babysitz, Sondergepäck, Anweisungen…",
        "res.submit": "Buchung bestätigen",
        "res.note": "* Pflichtfelder. Nach dem Absenden erhalten wir Ihre Anfrage und kontaktieren Sie zur Bestätigung.",

        "err.name": "Der Name muss mindestens 3 Zeichen haben.",
        "err.phone": "Telefon / WhatsApp ist erforderlich.",
        "err.date_req": "Das Datum ist erforderlich.",
        "err.date_past": "Das Datum darf nicht in der Vergangenheit liegen.",
        "err.date_invalid": "Ungültiges Datum.",
        "err.time": "Die Abholzeit ist erforderlich.",
        "err.pickup": "Der Abholort ist erforderlich.",
        "err.destination": "Das Ziel ist erforderlich.",

        "conf.title": "Ihre Buchung ist eingegangen!",
        "conf.lead": "Wir kontaktieren Sie innerhalb von 30 Minuten, um die Details Ihres Transfers zu bestätigen.",
        "conf.whatsapp": "Schreiben Sie uns auf WhatsApp", "conf.back": "Zurück zur Startseite",

        "footer.contact": "Kontakt", "footer.follow": "Folgen Sie uns", "footer.company": "Unternehmen",
        "footer.privacy": "Datenschutz", "footer.rights": "Alle Rechte vorbehalten.",
    },

    # ======================================================================
    "zh": {
        "lang.label": "语言",
        "nav.home": "首页", "nav.services": "服务", "nav.about": "关于我们", "nav.book": "预订",
        "nav.login": "登录",

        "hero.title_a": "尊享与", "hero.title_b": "专属定制接送",
        "hero.sub": "专业司机、准时保障，为本地及国际客户提供高端贴心服务。",
        "hero.book_now": "立即预订", "hero.see_services": "查看服务",

        "home.fleet_eyebrow": "我们的车队", "home.featured": "精选服务",
        "home.featured_lead": "选择最适合您行程的车辆，几秒钟即可完成预订。",
        "common.book": "预订", "common.book_name": "预订", "common.passengers": "位乘客",
        "home.diff_eyebrow": "与众不同", "home.why": "为何选择我们？",
        "feat.1.t": "准时保障", "feat.1.d": "我们比您更早到达，您的时间至上。",
        "feat.2.t": "专业司机", "feat.2.d": "训练有素、谨慎可靠的司机。",
        "feat.3.t": "国际服务", "feat.3.d": "以高端服务接待来自世界各地的客户。",
        "feat.4.t": "航班追踪", "feat.4.d": "实时监控您的航班并随时调整。",
        "feat.5.t": "全天候服务", "feat.5.d": "全年无休，随时为您待命。",
        "feat.6.t": "高端车辆", "feat.6.d": "现代、舒适、始终一尘不染的车队。",
        "cta.title": "准备好您的下一次出行了吗？",
        "cta.text": "在线预订，我们的团队将在几分钟内为您确认。",

        "services.eyebrow": "服务目录", "services.title": "我们的服务",
        "services.lead": "每项服务均含专业司机。选择最适合您行程的服务，即刻预订。",
        "services.capacity": "载客量", "services.luggage": "行李", "services.up_to": "最多",
        "services.suitcases": "件行李", "services.ideal_for": "适合",

        "about.eyebrow": "关于我们", "about.title": "每段旅程都追求卓越",
        "about.lead_1": "致力于在",
        "about.lead_2": "提供高端出行体验，准时、安全与谨慎并非额外服务，而是我们的标准。",
        "about.history_h": "我们的故事",
        "about.history_p": "我们始于一个简单的理念：在城市中出行也能像头等舱一样舒适可靠。如今，我们以注重每个细节的服务陪伴企业高管、家庭及国际旅客。",
        "about.mission_h": "使命",
        "about.mission_p": "提供安全、准时、高品质的接送服务，在每次行程中超越客户的期待。",
        "about.vision_h": "愿景",
        "about.vision_p": "成为本地区领先的高端出行公司，以卓越运营与人性化服务著称。",
        "about.values_eyebrow": "我们的特质", "about.values_title": "我们的价值观",
        "value.1.t": "准时", "value.1.d": "我们珍视您的时间，如同自己的时间。",
        "value.2.t": "安全", "value.2.d": "经过检验的车辆与持证司机。",
        "value.3.t": "谨慎", "value.3.d": "每项服务都绝对保密。",
        "value.4.t": "热情服务", "value.4.d": "自始至终的热情与专业。",

        "res.eyebrow": "在线预订", "res.title": "预约您的接送",
        "res.lead": "填写表单，我们的团队将在 30 分钟内确认您的预订。",
        "res.step1": "1 · 服务", "res.service_label": "服务类型 *", "res.service_ph": "请选择车辆…",
        "res.pax_short": "位",
        "res.step2": "2 · 行程", "res.date": "服务日期 *", "res.time": "接送时间 *",
        "res.pickup": "上车地点 *", "res.pickup_choose": "— 选择常用地点 —",
        "res.pickup_ph": "酒店、楼宇、机场或地址…",
        "res.my_location": "我的位置", "res.my_location_loading": "获取中…",
        "res.my_location_done": "✓ 位置已获取",
        "res.pickup_hint": "可选择常用地点、输入地址，或使用您的当前位置。",
        "res.destination": "目的地 *", "res.dest_ph": "酒店、楼宇、机场或地址…",
        "res.flight_no": "航班号", "res.flight_ph": "例如 AV 8520",
        "res.airline": "航空公司", "res.airline_ph": "例如 Avianca",
        "res.passengers": "乘客人数 *", "res.luggage": "行李件数",
        "res.hint_pax": "此车辆最多 {n} 位乘客。", "res.hint_luggage": "最多 {n} 件行李。",
        "res.step3": "3 · 您的信息", "res.fullname": "姓名 *", "res.whatsapp": "WhatsApp *",
        "res.phone_ph": "300 000 0000", "res.email": "邮箱", "res.email_ph": "you@example.com",
        "res.doc_type": "证件类型 *", "res.doc_num": "证件号码",
        "res.comments": "其他备注", "res.comments_ph": "婴儿座椅、特殊行李、说明…",
        "res.submit": "确认预订",
        "res.note": "* 为必填项。提交后我们将收到您的请求并与您联系确认。",

        "err.name": "姓名至少需 3 个字符。",
        "err.phone": "电话 / WhatsApp 为必填项。",
        "err.date_req": "服务日期为必填项。",
        "err.date_past": "日期不能为过去的日期。",
        "err.date_invalid": "日期无效。",
        "err.time": "接送时间为必填项。",
        "err.pickup": "上车地点为必填项。",
        "err.destination": "目的地为必填项。",

        "conf.title": "已收到您的预订！",
        "conf.lead": "我们将在 30 分钟内与您联系，确认接送详情。",
        "conf.whatsapp": "通过 WhatsApp 联系我们", "conf.back": "返回首页",

        "footer.contact": "联系方式", "footer.follow": "关注我们", "footer.company": "公司",
        "footer.privacy": "隐私政策", "footer.rights": "版权所有。",
    },
}


def get_t(lang):
    """Devuelve una función t(clave) para el idioma dado, con respaldo en inglés."""
    base = TRANSLATIONS.get(lang, TRANSLATIONS[DEFAULT_LANG])
    fallback = TRANSLATIONS[DEFAULT_LANG]

    def t(key):
        return base.get(key, fallback.get(key, key))

    return t
