"""Conexión y utilidades de la base de datos SQLite."""

import sqlite3
from flask import g, current_app


def get_db():
    """Devuelve la conexión SQLite de la petición actual (la crea si no existe)."""
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"],
            detect_types=sqlite3.PARSE_DECLTYPES,
        )
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db(app):
    """Crea las tablas a partir de schema.sql si aún no existen."""
    import os

    with app.app_context():
        db = sqlite3.connect(app.config["DATABASE"])
        schema_path = os.path.join(app.config["BASE_DIR"], "schema.sql")
        with open(schema_path, "r", encoding="utf-8") as f:
            db.executescript(f.read())
        db.commit()
        db.close()


def init_app(app):
    """Registra el cierre de la conexión al final de cada petición."""
    app.teardown_appcontext(close_db)
