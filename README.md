# Angelica — Sitio de transporte ejecutivo / VIP

Sitio web con base de datos ligera (SQLite) para una empresa de transporte
ejecutivo en Medellín. Incluye sitio público + formulario de reserva con Google
Maps + panel administrativo con login.

## ✨ Qué incluye

**Sitio público** — multilingüe 🌐 (**inglés** por defecto, + español, alemán y chino)
con selector de idioma en la barra de navegación y botón de inicio de sesión.
- Inicio (landing premium con hero, servicios destacados y "¿por qué elegirnos?")
- Servicios (catálogo de vehículos)
- Quiénes Somos (misión, visión, valores)
- Formulario de reserva con lógica condicional (campos de vuelo si es aeropuerto,
  máximo de pasajeros según vehículo) y autocompletado de direcciones con Maps
- Punto de recogida por **3 vías**: lista de lugares frecuentes (definidos por el
  admin), escritura libre con autocompletado, o **botón "Mi ubicación"** que toma
  el GPS del celular del cliente (geolocalización del navegador)
- Botón flotante de WhatsApp

**Panel admin** (`/admin`)
- Ver todas las reservas con filtros por estado
- Cambiar estado y eliminar reservas
- Crear / editar / eliminar servicios, con subida de fotos a `media/`
- Gestionar **ubicaciones de recogida** frecuentes (aeropuertos, hoteles…) con sus
  coordenadas; aparecen como lista rápida en el formulario del cliente

> **Nota sobre el GPS:** el botón "Mi ubicación" usa la geolocalización del
> navegador. Funciona en `localhost`; en producción **requiere HTTPS** (el dominio
> con certificado SSL). Si hay llave de Maps, las coordenadas se convierten en
> dirección legible con una sola llamada.

## 🚀 Cómo ejecutarlo en local

```powershell
# 1. Entorno virtual (ya creado en venv/)
venv\Scripts\activate

# 2. Instalar dependencias (solo la primera vez)
pip install -r requirements.txt

# 3. Crear tablas y cargar datos de ejemplo (solo la primera vez)
python -c "import app"      # crea la base de datos angelica.db
python seed.py              # carga los 4 servicios del brief

# 4. Arrancar
python app.py
```

Abrir: http://127.0.0.1:5000
Panel: http://127.0.0.1:5000/admin

## ⚙️ Configuración

Los valores editables se cargan desde `.env`, que no se sube al repositorio.
Para crear tu configuración local:

```powershell
copy .env.example .env
```

Edita `.env` para personalizar:
- `NEGOCIO_NOMBRE` → el nombre que aparece en todo el sitio.
- Datos de contacto, WhatsApp e Instagram (footer + botón flotante).
- `ADMIN_USUARIO` / `ADMIN_PASSWORD` → acceso al panel administrativo.
- `GOOGLE_MAPS_API_KEY` → tu llave de Google (opcional).
- `SECRET_KEY` → clave privada de Flask para sesiones.

Idiomas: se editan en `translations.py` (inglés es el principal).

## 🗺️ Google Maps (con ahorro de llamadas)

- Si **no** pones llave: los campos de origen/destino funcionan como texto normal.
  El sitio opera con normalidad.
- Si pones llave: se activa el autocompletado de direcciones. Para **minimizar el
  costo** se usa un *session token* (Google factura por sesión, no por tecla) y las
  coordenadas se **guardan en la reserva** para no volver a consultar la API.
- En Google Cloud habilita: **Maps JavaScript API** y **Places API**.
- Recomendado pasar la llave por variable de entorno: `GOOGLE_MAPS_API_KEY`.

## 🖼️ Imágenes (carpeta `media/`)

Todas las imágenes van en `media/`. Aún no hay fotos reales: ver
[media/_DESCRIPCIONES_IMAGENES.md](media/_DESCRIPCIONES_IMAGENES.md) para saber qué
foto colocar en cada lugar y con qué nombre. Mientras no existan, el sitio muestra
marcadores elegantes (no se rompe). Las fotos de servicios también se suben desde
el panel admin.

## 🗄️ Base de datos

SQLite en `angelica.db` (un solo archivo). Tablas: `categorias`, `servicios`,
`clientes`, `reservas`. El esquema está en [schema.sql](schema.sql). Incluye un
campo `categoria` en servicios y reservas pensado para escalar a futuras
categorías (Enfermeras, Chefs, etc.) sin reescribir.

## ☁️ Despliegue (hosting + dominio)

Funciona en cualquier hosting que corra Python (PythonAnywhere, Render, un VPS…).
En producción:

1. Usa un servidor WSGI real en vez de `python app.py`:
   ```bash
   pip install gunicorn        # Linux
   gunicorn "app:app" --bind 0.0.0.0:8000
   ```
   (En Windows/IIS o PythonAnywhere se configura el WSGI según el proveedor.)
2. Define variables de entorno `SECRET_KEY` y `GOOGLE_MAPS_API_KEY`.
3. En Easypanel, monta volúmenes persistentes para `/app/data` y `/app/media`.
4. Apunta tu dominio al hosting. La llave de Maps va restringida a tu dominio.
5. Cambia `ADMIN_PASSWORD` por una contraseña fuerte.

## 📌 Fuera de alcance (fase futura, según el brief)

Roles múltiples (coordinador/conductor), métricas/KPIs, calendario, exportar a
Excel/PDF, y notificaciones automáticas por email/WhatsApp/Google Calendar.
