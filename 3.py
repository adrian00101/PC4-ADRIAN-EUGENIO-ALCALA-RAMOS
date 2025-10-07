# problema3_contar_lineas.py

def contar_lineas_codigo(ruta_archivo):
    try:
        # Verificar que el archivo tenga extensión .py
        if not ruta_archivo.endswith(".py"):
            print("El archivo no tiene extensión .py")
            return

        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        contador = 0
        for linea in lineas:
            # Quitar espacios en blanco al inicio y final
            linea_limpia = linea.strip()
            # Ignorar líneas vacías o comentarios
            if linea_limpia and not linea_limpia.startswith("#"):
                contador += 1

        print(f"El archivo '{ruta_archivo}' tiene {contador} líneas de código (excluyendo comentarios y líneas en blanco).")

    except FileNotFoundError:
        print("El archivo especificado no existe.")
    except Exception as e:
        print("Ocurrió un error:", e)


# Programa principal
if __name__ == "__main__":
    ruta = input("Ingrese la ruta y nombre del archivo .py: ")
    contar_lineas_codigo(ruta)


#en mi caso utilize esta ruta en mi computadora : C:\Users\Adrián Alcalá\Documents\CURSO DE PYTHON\clase 4\pc4\hola.py
#y mi resultado fue este El archivo 'C:\Users\Adrián Alcalá\Documents\CURSO DE PYTHON\clase 4\pc4\hola.py' tiene 2 líneas de código (excluyendo comentarios y líneas en blanco).