
#ninguna de las 3 apis funcionan asi que cree  un programa que simulara una api
#y use este comando en la terminal antes de ejercutarlo "py -m pip install requests pymongo"

import sqlite3
import random
from datetime import date, timedelta
from pymongo import MongoClient


# Función que simula la API de SUNAT

def obtener_tipo_cambio_sunat_ficticio():
    """
    Simula los datos de tipo de cambio SUNAT de todo el 2023.
    Genera valores aleatorios realistas entre 3.60 y 3.90
    """
    print("Simulando datos históricos de tipo de cambio 2023...")
    registros = []
    fecha = date(2023, 1, 1)
    fin = date(2023, 12, 31)

    while fecha <= fin:
        compra = round(random.uniform(3.60, 3.85), 3)
        venta = round(compra + random.uniform(0.01, 0.05), 3)
        registros.append({
            "fecha": str(fecha),
            "compra": compra,
            "venta": venta
        })
        fecha += timedelta(days=1)

    print(f"Datos simulados: {len(registros)} registros generados.")
    return registros


# Función para guardar en SQLite

def guardar_en_sqlite(registros):
    conexion = sqlite3.connect("base.db")
    cursor = conexion.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sunat_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            compra REAL,
            venta REAL
        )
    """)
    
    cursor.executemany(
        "INSERT INTO sunat_info (fecha, compra, venta) VALUES (:fecha, :compra, :venta)",
        registros
    )
    
    conexion.commit()
    conexion.close()
    print("Datos guardados en base.db (SQLite).")


# Función para guardar en MongoDB

def guardar_en_mongodb(registros):
    try:
        cliente = MongoClient("mongodb://localhost:27017/")
        db = cliente["base"]
        coleccion = db["sunat_info"]
        coleccion.delete_many({})  # limpiar colección
        coleccion.insert_many(registros)
        print("Datos guardados en MongoDB (base.sunat_info).")
    except Exception as e:
        print(f"No se pudo conectar a MongoDB: {e}")


# Función para mostrar los datos guardados en SQLite

def mostrar_datos_sqlite():
    conexion = sqlite3.connect("base.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT fecha, compra, venta FROM sunat_info LIMIT 10")
    filas = cursor.fetchall()
    conexion.close()

    print("\nEjemplo de registros guardados (primeros 10):")
    for fila in filas:
        print(f"Fecha: {fila[0]} | Compra: {fila[1]} | Venta: {fila[2]}")


# Programa principal

def main():
    registros = obtener_tipo_cambio_sunat_ficticio()
    guardar_en_sqlite(registros)
    guardar_en_mongodb(registros)
    mostrar_datos_sqlite()

if __name__ == "__main__":
    main()
