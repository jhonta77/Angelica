-- ============================================================================
--  Esquema de la base de datos (SQLite)
--  Diseñado con un campo "categoria" en servicios y reservas para poder
--  agregar a futuro otras categorías (Enfermeras, Chefs, etc.) sin reescribir.
-- ============================================================================

PRAGMA foreign_keys = ON;

-- ----------------------------------------------------------------------------
-- Categorías de servicio (escalabilidad). Fase 1: solo "Transporte".
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS categorias (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre    TEXT NOT NULL UNIQUE,
    activa    INTEGER NOT NULL DEFAULT 1
);

-- ----------------------------------------------------------------------------
-- Servicios ofrecidos (los vehículos/tipos de servicio). Editables en admin.
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS servicios (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    categoria_id  INTEGER NOT NULL DEFAULT 1,
    nombre        TEXT NOT NULL,
    descripcion   TEXT NOT NULL DEFAULT '',
    ideal_para    TEXT NOT NULL DEFAULT '',
    capacidad_min INTEGER NOT NULL DEFAULT 1,
    capacidad_max INTEGER NOT NULL DEFAULT 4,
    max_maletas   INTEGER NOT NULL DEFAULT 3,
    imagen        TEXT NOT NULL DEFAULT '',   -- nombre de archivo dentro de /media
    es_aeropuerto INTEGER NOT NULL DEFAULT 0, -- informativo
    activo        INTEGER NOT NULL DEFAULT 1,
    orden         INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY (categoria_id) REFERENCES categorias (id)
);

-- ----------------------------------------------------------------------------
-- Ubicaciones frecuentes de recogida (lista gestionada por el administrador).
-- El cliente puede elegir una de estas en el formulario de reserva; sus
-- coordenadas quedan cacheadas y no requieren llamadas a la API de Google.
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ubicaciones (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre    TEXT NOT NULL,                 -- ej. "Aeropuerto José María Córdova"
    direccion TEXT NOT NULL DEFAULT '',      -- dirección completa / referencia
    lat       REAL,
    lng       REAL,
    activo    INTEGER NOT NULL DEFAULT 1,
    orden     INTEGER NOT NULL DEFAULT 0
);

-- ----------------------------------------------------------------------------
-- Clientes (se crean/actualizan automáticamente al recibir una reserva)
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS clientes (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre         TEXT NOT NULL,
    tipo_documento TEXT NOT NULL DEFAULT 'CC',  -- CC / Pasaporte / ID Extranjero / NIT
    documento      TEXT NOT NULL DEFAULT '',
    prefijo_pais   TEXT NOT NULL DEFAULT '+57',
    telefono       TEXT NOT NULL,               -- WhatsApp
    email          TEXT NOT NULL DEFAULT '',
    creado_en      TEXT NOT NULL DEFAULT (datetime('now','localtime'))
);

-- ----------------------------------------------------------------------------
-- Reservas (el núcleo). Guarda la "ruta seleccionada" (origen/destino) con
-- coordenadas cacheadas para no volver a llamar a la API de Google.
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS reservas (
    id                INTEGER PRIMARY KEY AUTOINCREMENT,
    categoria_id      INTEGER NOT NULL DEFAULT 1,
    cliente_id        INTEGER NOT NULL,
    servicio_id       INTEGER,
    servicio_nombre   TEXT NOT NULL DEFAULT '', -- copia textual por si se borra el servicio
    fecha_servicio    TEXT NOT NULL,
    hora_recogida     TEXT NOT NULL,
    punto_recogida    TEXT NOT NULL,
    recogida_lat      REAL,
    recogida_lng      REAL,
    destino           TEXT NOT NULL,
    destino_lat       REAL,
    destino_lng       REAL,
    num_pasajeros     INTEGER NOT NULL DEFAULT 1,
    num_maletas       INTEGER NOT NULL DEFAULT 0,
    numero_vuelo      TEXT NOT NULL DEFAULT '',
    aerolinea         TEXT NOT NULL DEFAULT '',
    comentarios       TEXT NOT NULL DEFAULT '',
    valor_cobrado     REAL,
    estado            TEXT NOT NULL DEFAULT 'pendiente', -- pendiente/confirmada/en_curso/completada/cancelada
    creado_en         TEXT NOT NULL DEFAULT (datetime('now','localtime')),
    FOREIGN KEY (categoria_id) REFERENCES categorias (id),
    FOREIGN KEY (cliente_id)   REFERENCES clientes (id),
    FOREIGN KEY (servicio_id)  REFERENCES servicios (id) ON DELETE SET NULL
);

CREATE INDEX IF NOT EXISTS idx_reservas_fecha  ON reservas (fecha_servicio);
CREATE INDEX IF NOT EXISTS idx_reservas_estado ON reservas (estado);
