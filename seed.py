"""
Carga datos iniciales: la categoría "Transporte" y los 4 servicios del brief.
Se ejecuta solo: python seed.py
Es idempotente (no duplica si ya existen registros).
"""

import sqlite3
from config import Config

SERVICIOS = [
    {
        "nombre": "Sedán Ejecutivo (Toyota Corolla)",
        "descripcion": "Vehículo cómodo para traslados individuales o en pareja. "
                       "Aire acondicionado y agua a bordo.",
        "ideal_para": "Traslados ejecutivos",
        "capacidad_min": 1, "capacidad_max": 3, "max_maletas": 3,
        "imagen": "servicio-sedan.jpg", "orden": 1,
    },
    {
        "nombre": "SUV (Toyota RAV4 / Fortuner)",
        "descripcion": "Camioneta de alta gama para mayor comodidad y espacio. "
                       "Ideal para familias o equipaje voluminoso.",
        "ideal_para": "Familias, aeropuerto",
        "capacidad_min": 1, "capacidad_max": 5, "max_maletas": 5,
        "imagen": "servicio-suv.jpg", "orden": 2,
    },
    {
        "nombre": "Van / Furgoneta",
        "descripcion": "Vehículo tipo furgón para grupos medianos. Ideal para "
                       "equipos de trabajo o grupos de turistas.",
        "ideal_para": "Grupos, tours",
        "capacidad_min": 1, "capacidad_max": 10, "max_maletas": 10,
        "imagen": "servicio-van.jpg", "orden": 3,
    },
    {
        "nombre": "Servicio Móvil / A Domicilio",
        "descripcion": "Servicio flexible bajo solicitud. Se coordina según la "
                       "necesidad del cliente (horario y punto de recogida a convenir).",
        "ideal_para": "Traslados especiales",
        "capacidad_min": 1, "capacidad_max": 8, "max_maletas": 8,
        "imagen": "servicio-movil.jpg", "orden": 4,
    },
]


UBICACIONES = [
    {"nombre": "Aeropuerto José María Córdova (Rionegro)",
     "direccion": "Rionegro, Antioquia", "lat": 6.1645, "lng": -75.4231, "orden": 1},
    {"nombre": "Aeropuerto Olaya Herrera (Medellín)",
     "direccion": "Medellín, Antioquia", "lat": 6.2196, "lng": -75.5905, "orden": 2},
    {"nombre": "Terminal del Norte",
     "direccion": "Medellín, Antioquia", "lat": 6.2776, "lng": -75.5689, "orden": 3},
]


def main():
    db = sqlite3.connect(Config.DATABASE)
    db.execute("PRAGMA foreign_keys = ON")

    # Categoría base
    db.execute(
        "INSERT OR IGNORE INTO categorias (id, nombre, activa) VALUES (1, 'Transporte', 1)"
    )

    # Ubicaciones de ejemplo (solo si la tabla está vacía)
    if db.execute("SELECT COUNT(*) FROM ubicaciones").fetchone()[0] == 0:
        for u in UBICACIONES:
            db.execute(
                """INSERT INTO ubicaciones (nombre, direccion, lat, lng, orden, activo)
                   VALUES (:nombre, :direccion, :lat, :lng, :orden, 1)""",
                u,
            )
        print(f"Insertadas {len(UBICACIONES)} ubicaciones.")

    # Servicios (solo si la tabla está vacía, para no duplicar)
    n = db.execute("SELECT COUNT(*) FROM servicios").fetchone()[0]
    if n == 0:
        for s in SERVICIOS:
            db.execute(
                """INSERT INTO servicios
                   (categoria_id, nombre, descripcion, ideal_para,
                    capacidad_min, capacidad_max, max_maletas, imagen, orden, activo)
                   VALUES (1, :nombre, :descripcion, :ideal_para,
                           :capacidad_min, :capacidad_max, :max_maletas, :imagen, :orden, 1)""",
                s,
            )
        print(f"Insertados {len(SERVICIOS)} servicios.")
    else:
        print(f"Ya existían {n} servicios; no se insertó nada.")

    db.commit()
    db.close()
    print("Seed completado.")


if __name__ == "__main__":
    main()
