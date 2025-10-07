import pandas as pd
import sqlite3
from pymongo import MongoClient

def obtener_tipo_cambio():
    conexion = sqlite3.connect('base.db')
    query = "SELECT fecha, compra, venta FROM sunat_info"
    df = pd.read_sql_query(query, conexion)
    conexion.close()
    return df

def leer_ventas():
    df = pd.read_csv('ventas.csv')
    df['fecha'] = pd.to_datetime(df['fecha']).dt.date
    return df

def solarizar_ventas(df_ventas, df_cambio):
    df_cambio['fecha'] = pd.to_datetime(df_cambio['fecha']).dt.date
    df_merged = pd.merge(df_ventas, df_cambio, on='fecha', how='left')
    df_merged['precio_soles'] = df_merged['precio_usd'] * df_merged['venta']
    df_total = df_merged.groupby('producto')['precio_soles'].sum().reset_index()
    return df_total

def guardar_en_mongo(df_resultado):
    try:
        cliente = MongoClient('mongodb://localhost:27017/')
        db = cliente['ventas_db']
        coleccion = db['ventas_solarizadas']
        coleccion.delete_many({})
        coleccion.insert_many(df_resultado.to_dict('records'))
        print("✅ Datos guardados en MongoDB (colección: ventas_solarizadas)")
        cliente.close()
    except Exception as e:
        print("⚠ No se pudo conectar a MongoDB, mostrando datos solo en consola.")

def mostrar_resultados(df):
    print("\n=== TOTAL VENTAS SOLARIZADAS ===")
    print(df)

def main():
    print("Leyendo tipo de cambio desde base.db ...")
    tipo_cambio = obtener_tipo_cambio()
    print("Leyendo archivo ventas.csv ...")
    ventas = leer_ventas()
    print("Procesando y solarizando precios ...")
    resultado = solarizar_ventas(ventas, tipo_cambio)
    mostrar_resultados(resultado)
    guardar_en_mongo(resultado)

if __name__ == "__main__":
    main()