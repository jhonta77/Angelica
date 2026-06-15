"""
Configuracion central del sitio.

Los valores editables viven en .env. Este archivo solo carga esos valores y
mantiene los ajustes calculados que dependen de la ubicacion del proyecto.
"""

import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
ENV_PATHS = (
    os.path.join(BASE_DIR, ".env"),
    os.path.join(BASE_DIR, "media", ".env"),
)


def _load_env_file(path):
    if not os.path.exists(path):
        return

    with open(path, encoding="utf-8") as env_file:
        for raw_line in env_file:
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue

            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")

            if key and key not in os.environ:
                os.environ[key] = value


def _env(name, default=""):
    return os.environ.get(name, default)


for env_path in ENV_PATHS:
    _load_env_file(env_path)


class Config:
    NEGOCIO_NOMBRE = _env("NEGOCIO_NOMBRE")
    NEGOCIO_ESLOGAN = _env("NEGOCIO_ESLOGAN")
    NEGOCIO_CIUDAD = _env("NEGOCIO_CIUDAD")

    CONTACTO_TELEFONO = _env("CONTACTO_TELEFONO")
    CONTACTO_EMAIL = _env("CONTACTO_EMAIL")
    WHATSAPP_NUMERO = _env("WHATSAPP_NUMERO")
    INSTAGRAM_URL = _env("INSTAGRAM_URL")

    ADMIN_USUARIO = _env("ADMIN_USUARIO")
    ADMIN_PASSWORD = _env("ADMIN_PASSWORD")
    GOOGLE_MAPS_API_KEY = _env("GOOGLE_MAPS_API_KEY")
    SECRET_KEY = _env("SECRET_KEY", "clave-secreta-cambiala-en-produccion")

    BASE_DIR = BASE_DIR
    DATABASE = _env("DATABASE", os.path.join(BASE_DIR, "angelica.db"))
    MEDIA_DIR = _env("MEDIA_DIR", os.path.join(BASE_DIR, "media"))
    UPLOAD_EXTENSIONES = {"png", "jpg", "jpeg", "webp", "gif"}
    MAX_CONTENT_LENGTH = int(_env("MAX_CONTENT_LENGTH", str(5 * 1024 * 1024)))
