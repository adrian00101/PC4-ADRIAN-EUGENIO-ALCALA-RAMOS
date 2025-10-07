# problema2_tablas.py

def crear_tabla():
    try:
        n = int(input("Ingrese un número entero entre 1 y 10: "))
        if n < 1 or n > 10:
            print("Número fuera del rango permitido.")
            return
        
        nombre_archivo = f"tabla-{n}.txt"
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            for i in range(1, 11):
                archivo.write(f"{n} x {i} = {n * i}\n")
        print(f"Archivo '{nombre_archivo}' creado correctamente.")
    except ValueError:
        print("Debe ingresar un número entero válido.")


def mostrar_tabla():
    try:
        n = int(input("Ingrese el número de la tabla que desea mostrar (1 a 10): "))
        nombre_archivo = f"tabla-{n}.txt"
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            print(f"\nTabla del {n}:\n")
            print(archivo.read())
    except FileNotFoundError:
        print(f"El archivo 'tabla-{n}.txt' no existe. Primero debe crearlo.")
    except ValueError:
        print("Debe ingresar un número entero válido.")


def mostrar_linea_especifica():
    try:
        n = int(input("Ingrese el número de la tabla (1 a 10): "))
        m = int(input("Ingrese el número de línea que desea mostrar (1 a 10): "))
        nombre_archivo = f"tabla-{n}.txt"
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            if 1 <= m <= len(lineas):
                print(f"Línea {m}: {lineas[m-1].strip()}")
            else:
                print("Número de línea fuera del rango.")
    except FileNotFoundError:
        print(f"El archivo 'tabla-{n}.txt' no existe. Primero debe crearlo.")
    except ValueError:
        print("Debe ingresar números enteros válidos.")


def menu():
    while True:
        print("\n--- MENÚ TABLAS DE MULTIPLICAR ---")
        print("1. Crear tabla de multiplicar")
        print("2. Mostrar tabla completa")
        print("3. Mostrar una línea específica")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_tabla()
        elif opcion == "2":
            mostrar_tabla()
        elif opcion == "3":
            mostrar_linea_especifica()
        elif opcion == "4":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


# Programa principal
if __name__ == "__main__":
    menu()
