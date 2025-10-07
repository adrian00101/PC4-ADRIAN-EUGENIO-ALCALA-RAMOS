import sqlite3

# Crear base de datos y tabla
conexion = sqlite3.connect('base.db')
cursor = conexion.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS sunat_info (
    fecha TEXT,
    compra REAL,
    venta REAL
)''')

# Insertar datos ficticios (tipo de cambio por mes)
data = [
    ('2023-01-02', 3.80, 3.85),
    ('2023-02-01', 3.78, 3.83),
    ('2023-03-01', 3.77, 3.82),
    ('2023-04-01', 3.76, 3.81),
    ('2023-05-01', 3.75, 3.80),
    ('2023-06-01', 3.74, 3.79),
    ('2023-07-01', 3.73, 3.78),
    ('2023-08-01', 3.72, 3.77),
    ('2023-09-01', 3.71, 3.76),
    ('2023-10-01', 3.70, 3.75),
    ('2023-11-01', 3.69, 3.74),
    ('2023-12-01', 3.68, 3.73),
]

cursor.executemany("INSERT INTO sunat_info VALUES (?, ?, ?)", data)
conexion.commit()
conexion.close()

print("✅ Base de datos creada correctamente con datos de ejemplo.")
