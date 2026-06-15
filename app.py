"""
Aplicación Flask — Transporte ejecutivo / VIP.

Sitio público (Inicio, Servicios, Quiénes Somos, Reserva) + panel admin con
login para ver/borrar reservas y administrar los servicios ofrecidos.

Ejecutar:
    python app.py
"""

import os
import sqlite3
from functools import wraps
from datetime import datetime

from flask import (
    Flask, render_template, request, redirect, url_for, flash,
    session, send_from_directory, abort,
)
from werkzeug.utils import secure_filename

from config import Config
import database
from translations import TRANSLATIONS, LANGS, DEFAULT_LANG, get_t

ESTADOS = ["pendiente", "confirmada", "en_curso", "completada", "cancelada"]
TIPOS_DOCUMENTO = ["CC", "Pasaporte", "ID Extranjero", "NIT"]


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    os.makedirs(app.config["MEDIA_DIR"], exist_ok=True)

    database.init_app(app)
    database.init_db(app)

    # Hace que el nombre del negocio y datos de contacto estén disponibles
    # en TODAS las plantillas sin pasarlos manualmente.
    @app.context_processor
    def inject_negocio():
        return {
            "NEGOCIO": {
                "nombre": app.config["NEGOCIO_NOMBRE"],
                "eslogan": app.config["NEGOCIO_ESLOGAN"],
                "ciudad": app.config["NEGOCIO_CIUDAD"],
                "telefono": app.config["CONTACTO_TELEFONO"],
                "email": app.config["CONTACTO_EMAIL"],
                "whatsapp": app.config["WHATSAPP_NUMERO"],
                "instagram": app.config["INSTAGRAM_URL"],
            },
            "GOOGLE_MAPS_API_KEY": app.config["GOOGLE_MAPS_API_KEY"],
            "anio_actual": datetime.now().year,
        }

    # Inyecta el sistema de traducción (idioma actual + función t)
    @app.context_processor
    def inject_i18n():
        lang = session.get("lang", DEFAULT_LANG)
        if lang not in TRANSLATIONS:
            lang = DEFAULT_LANG
        return {"t": get_t(lang), "current_lang": lang, "LANGS": LANGS}

    # ---- Cambiar de idioma ------------------------------------------------
    @app.route("/lang/<code>")
    def set_lang(code):
        if code in TRANSLATIONS:
            session["lang"] = code
        return redirect(request.referrer or url_for("index"))

    # ---- Servir imágenes desde la carpeta /media --------------------------
    @app.route("/media/<path:filename>")
    def media(filename):
        return send_from_directory(app.config["MEDIA_DIR"], filename)

    # ======================================================================
    #  SITIO PÚBLICO
    # ======================================================================
    @app.route("/")
    def index():
        db = database.get_db()
        servicios = db.execute(
            "SELECT * FROM servicios WHERE activo = 1 ORDER BY orden, id"
        ).fetchall()
        return render_template("index.html", servicios=servicios)

    @app.route("/servicios")
    def servicios():
        db = database.get_db()
        servicios = db.execute(
            "SELECT * FROM servicios WHERE activo = 1 ORDER BY orden, id"
        ).fetchall()
        return render_template("servicios.html", servicios=servicios)

    @app.route("/quienes-somos")
    def quienes_somos():
        return render_template("quienes_somos.html")

    @app.route("/reservar", methods=["GET", "POST"])
    def reservar():
        db = database.get_db()
        servicios = db.execute(
            "SELECT * FROM servicios WHERE activo = 1 ORDER BY orden, id"
        ).fetchall()
        ubicaciones = db.execute(
            "SELECT * FROM ubicaciones WHERE activo = 1 ORDER BY orden, nombre"
        ).fetchall()

        if request.method == "POST":
            errores = _validar_reserva(request.form, get_t(session.get("lang", DEFAULT_LANG)))
            if errores:
                for e in errores:
                    flash(e, "error")
                return render_template(
                    "reservar.html", servicios=servicios, ubicaciones=ubicaciones,
                    tipos_documento=TIPOS_DOCUMENTO, datos=request.form,
                    preseleccion=request.form.get("servicio_id", ""),
                )

            # Cliente
            cur = db.execute(
                """INSERT INTO clientes
                   (nombre, tipo_documento, documento, prefijo_pais, telefono, email)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (
                    request.form["nombre"].strip(),
                    request.form.get("tipo_documento", "CC"),
                    request.form.get("documento", "").strip(),
                    request.form.get("prefijo_pais", "+57").strip(),
                    request.form["telefono"].strip(),
                    request.form.get("email", "").strip(),
                ),
            )
            cliente_id = cur.lastrowid

            # Nombre textual del servicio (para conservarlo aunque se borre)
            servicio_id = request.form.get("servicio_id") or None
            servicio_nombre = ""
            if servicio_id:
                row = db.execute(
                    "SELECT nombre FROM servicios WHERE id = ?", (servicio_id,)
                ).fetchone()
                if row:
                    servicio_nombre = row["nombre"]

            db.execute(
                """INSERT INTO reservas
                   (categoria_id, cliente_id, servicio_id, servicio_nombre,
                    fecha_servicio, hora_recogida, punto_recogida, recogida_lat, recogida_lng,
                    destino, destino_lat, destino_lng, num_pasajeros, num_maletas,
                    numero_vuelo, aerolinea, comentarios, estado)
                   VALUES (1, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'pendiente')""",
                (
                    cliente_id, servicio_id, servicio_nombre,
                    request.form["fecha_servicio"], request.form["hora_recogida"],
                    request.form["punto_recogida"].strip(),
                    _to_float(request.form.get("recogida_lat")),
                    _to_float(request.form.get("recogida_lng")),
                    request.form["destino"].strip(),
                    _to_float(request.form.get("destino_lat")),
                    _to_float(request.form.get("destino_lng")),
                    _to_int(request.form.get("num_pasajeros"), 1),
                    _to_int(request.form.get("num_maletas"), 0),
                    request.form.get("numero_vuelo", "").strip(),
                    request.form.get("aerolinea", "").strip(),
                    request.form.get("comentarios", "").strip(),
                ),
            )
            db.commit()
            return redirect(url_for("reserva_confirmada"))

        return render_template(
            "reservar.html", servicios=servicios, ubicaciones=ubicaciones,
            tipos_documento=TIPOS_DOCUMENTO, datos={},
            preseleccion=request.args.get("servicio", ""),
        )

    @app.route("/reserva-confirmada")
    def reserva_confirmada():
        return render_template("reserva_confirmada.html")

    # ======================================================================
    #  PANEL ADMINISTRATIVO
    # ======================================================================
    @app.route("/admin/login", methods=["GET", "POST"])
    def admin_login():
        if request.method == "POST":
            usuario = request.form.get("usuario", "")
            password = request.form.get("password", "")
            if (usuario == app.config["ADMIN_USUARIO"]
                    and password == app.config["ADMIN_PASSWORD"]):
                session["admin"] = True
                return redirect(url_for("admin_reservas"))
            flash("Usuario o contraseña incorrectos.", "error")
        return render_template("admin/login.html")

    @app.route("/admin/logout")
    def admin_logout():
        session.pop("admin", None)
        return redirect(url_for("admin_login"))

    @app.route("/admin")
    @login_required
    def admin_reservas():
        db = database.get_db()
        estado = request.args.get("estado", "")
        if estado in ESTADOS:
            reservas = db.execute(
                """SELECT r.*, c.nombre AS cliente_nombre, c.telefono, c.prefijo_pais,
                          c.documento, c.tipo_documento, c.email
                   FROM reservas r JOIN clientes c ON c.id = r.cliente_id
                   WHERE r.estado = ? ORDER BY r.fecha_servicio DESC, r.hora_recogida DESC""",
                (estado,),
            ).fetchall()
        else:
            reservas = db.execute(
                """SELECT r.*, c.nombre AS cliente_nombre, c.telefono, c.prefijo_pais,
                          c.documento, c.tipo_documento, c.email
                   FROM reservas r JOIN clientes c ON c.id = r.cliente_id
                   ORDER BY r.fecha_servicio DESC, r.hora_recogida DESC"""
            ).fetchall()

        conteos = {e: 0 for e in ESTADOS}
        for row in db.execute("SELECT estado, COUNT(*) n FROM reservas GROUP BY estado"):
            conteos[row["estado"]] = row["n"]

        return render_template(
            "admin/reservas.html", reservas=reservas, estados=ESTADOS,
            filtro_estado=estado, conteos=conteos, total=sum(conteos.values()),
        )

    @app.route("/admin/reserva/<int:rid>/estado", methods=["POST"])
    @login_required
    def admin_reserva_estado(rid):
        nuevo = request.form.get("estado")
        if nuevo not in ESTADOS:
            abort(400)
        db = database.get_db()
        db.execute("UPDATE reservas SET estado = ? WHERE id = ?", (nuevo, rid))
        db.commit()
        flash("Estado actualizado.", "ok")
        return redirect(request.referrer or url_for("admin_reservas"))

    @app.route("/admin/reserva/<int:rid>/eliminar", methods=["POST"])
    @login_required
    def admin_reserva_eliminar(rid):
        db = database.get_db()
        db.execute("DELETE FROM reservas WHERE id = ?", (rid,))
        db.commit()
        flash("Reserva eliminada.", "ok")
        return redirect(url_for("admin_reservas"))

    # ---- Administración de servicios --------------------------------------
    @app.route("/admin/servicios")
    @login_required
    def admin_servicios():
        db = database.get_db()
        servicios = db.execute(
            "SELECT * FROM servicios ORDER BY orden, id"
        ).fetchall()
        return render_template("admin/servicios.html", servicios=servicios)

    @app.route("/admin/servicios/nuevo", methods=["GET", "POST"])
    @login_required
    def admin_servicio_nuevo():
        if request.method == "POST":
            return _guardar_servicio(None)
        return render_template("admin/servicio_form.html", servicio=None)

    @app.route("/admin/servicios/<int:sid>/editar", methods=["GET", "POST"])
    @login_required
    def admin_servicio_editar(sid):
        db = database.get_db()
        servicio = db.execute("SELECT * FROM servicios WHERE id = ?", (sid,)).fetchone()
        if not servicio:
            abort(404)
        if request.method == "POST":
            return _guardar_servicio(sid)
        return render_template("admin/servicio_form.html", servicio=servicio)

    @app.route("/admin/servicios/<int:sid>/eliminar", methods=["POST"])
    @login_required
    def admin_servicio_eliminar(sid):
        db = database.get_db()
        db.execute("DELETE FROM servicios WHERE id = ?", (sid,))
        db.commit()
        flash("Servicio eliminado.", "ok")
        return redirect(url_for("admin_servicios"))

    def _guardar_servicio(sid):
        """Crea o actualiza un servicio. sid=None => crear."""
        db = database.get_db()
        f = request.form
        imagen = f.get("imagen_actual", "")

        archivo = request.files.get("imagen")
        if archivo and archivo.filename:
            nombre = _guardar_imagen(archivo)
            if nombre:
                imagen = nombre
            else:
                flash("Formato de imagen no permitido (usa jpg, png o webp).", "error")

        valores = (
            f.get("nombre", "").strip(),
            f.get("descripcion", "").strip(),
            f.get("ideal_para", "").strip(),
            _to_int(f.get("capacidad_min"), 1),
            _to_int(f.get("capacidad_max"), 4),
            _to_int(f.get("max_maletas"), 3),
            imagen,
            1 if f.get("activo") else 0,
            _to_int(f.get("orden"), 0),
        )

        if sid is None:
            db.execute(
                """INSERT INTO servicios
                   (categoria_id, nombre, descripcion, ideal_para, capacidad_min,
                    capacidad_max, max_maletas, imagen, activo, orden)
                   VALUES (1, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                valores,
            )
            flash("Servicio creado.", "ok")
        else:
            db.execute(
                """UPDATE servicios SET nombre=?, descripcion=?, ideal_para=?,
                   capacidad_min=?, capacidad_max=?, max_maletas=?, imagen=?,
                   activo=?, orden=? WHERE id=?""",
                valores + (sid,),
            )
            flash("Servicio actualizado.", "ok")
        db.commit()
        return redirect(url_for("admin_servicios"))

    # ---- Administración de ubicaciones de recogida -------------------------
    @app.route("/admin/ubicaciones")
    @login_required
    def admin_ubicaciones():
        db = database.get_db()
        ubicaciones = db.execute(
            "SELECT * FROM ubicaciones ORDER BY orden, nombre"
        ).fetchall()
        return render_template("admin/ubicaciones.html", ubicaciones=ubicaciones)

    @app.route("/admin/ubicaciones/nueva", methods=["GET", "POST"])
    @login_required
    def admin_ubicacion_nueva():
        if request.method == "POST":
            return _guardar_ubicacion(None)
        return render_template("admin/ubicacion_form.html", ubicacion=None)

    @app.route("/admin/ubicaciones/<int:uid>/editar", methods=["GET", "POST"])
    @login_required
    def admin_ubicacion_editar(uid):
        db = database.get_db()
        ubicacion = db.execute("SELECT * FROM ubicaciones WHERE id = ?", (uid,)).fetchone()
        if not ubicacion:
            abort(404)
        if request.method == "POST":
            return _guardar_ubicacion(uid)
        return render_template("admin/ubicacion_form.html", ubicacion=ubicacion)

    @app.route("/admin/ubicaciones/<int:uid>/eliminar", methods=["POST"])
    @login_required
    def admin_ubicacion_eliminar(uid):
        db = database.get_db()
        db.execute("DELETE FROM ubicaciones WHERE id = ?", (uid,))
        db.commit()
        flash("Ubicación eliminada.", "ok")
        return redirect(url_for("admin_ubicaciones"))

    def _guardar_ubicacion(uid):
        db = database.get_db()
        f = request.form
        valores = (
            f.get("nombre", "").strip(),
            f.get("direccion", "").strip(),
            _to_float(f.get("lat")),
            _to_float(f.get("lng")),
            1 if f.get("activo") else 0,
            _to_int(f.get("orden"), 0),
        )
        if uid is None:
            db.execute(
                """INSERT INTO ubicaciones (nombre, direccion, lat, lng, activo, orden)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                valores,
            )
            flash("Ubicación creada.", "ok")
        else:
            db.execute(
                """UPDATE ubicaciones SET nombre=?, direccion=?, lat=?, lng=?,
                   activo=?, orden=? WHERE id=?""",
                valores + (uid,),
            )
            flash("Ubicación actualizada.", "ok")
        db.commit()
        return redirect(url_for("admin_ubicaciones"))

    def _guardar_imagen(archivo):
        ext = archivo.filename.rsplit(".", 1)[-1].lower() if "." in archivo.filename else ""
        if ext not in app.config["UPLOAD_EXTENSIONES"]:
            return None
        base = secure_filename(archivo.filename.rsplit(".", 1)[0]) or "servicio"
        nombre = f"{base}-{int(datetime.now().timestamp())}.{ext}"
        archivo.save(os.path.join(app.config["MEDIA_DIR"], nombre))
        return nombre

    return app


# --------------------------------------------------------------------------
#  Helpers
# --------------------------------------------------------------------------
def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not session.get("admin"):
            return redirect(url_for("admin_login"))
        return view(*args, **kwargs)
    return wrapped


def _validar_reserva(form, t):
    errores = []
    if len((form.get("nombre") or "").strip()) < 3:
        errores.append(t("err.name"))
    if not (form.get("telefono") or "").strip():
        errores.append(t("err.phone"))
    if not (form.get("fecha_servicio") or "").strip():
        errores.append(t("err.date_req"))
    else:
        try:
            if datetime.strptime(form["fecha_servicio"], "%Y-%m-%d").date() < datetime.now().date():
                errores.append(t("err.date_past"))
        except ValueError:
            errores.append(t("err.date_invalid"))
    if not (form.get("hora_recogida") or "").strip():
        errores.append(t("err.time"))
    if not (form.get("punto_recogida") or "").strip():
        errores.append(t("err.pickup"))
    if not (form.get("destino") or "").strip():
        errores.append(t("err.destination"))
    return errores


def _to_float(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _to_int(v, default=0):
    try:
        return int(v)
    except (TypeError, ValueError):
        return default


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
