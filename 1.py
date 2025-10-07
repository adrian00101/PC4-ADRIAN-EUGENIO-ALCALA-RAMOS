# problema1_temperaturas.py

# Abrir el archivo de entrada y leer los datos
with open("temperaturas.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()

# Crear listas para almacenar las temperaturas
temperaturas = []

# Recorrer las líneas y procesar cada una
for linea in lineas:
    partes = linea.strip().split(",")
    if len(partes) == 2:
        fecha, temp = partes
        try:
            temperatura = float(temp)
            temperaturas.append(temperatura)
        except ValueError:
            pass  # Ignorar líneas con valores no numéricos

# Calcular estadísticas
if temperaturas:
    temp_promedio = sum(temperaturas) / len(temperaturas)
    temp_maxima = max(temperaturas)
    temp_minima = min(temperaturas)
else:
    temp_promedio = temp_maxima = temp_minima = None

# Escribir los resultados en un nuevo archivo
with open("resumen_temperaturas.txt", "w", encoding="utf-8") as salida:
    if temperaturas:
        salida.write("Resumen de Temperaturas\n")
        salida.write("-------------------------\n")
        salida.write(f"Temperatura promedio: {temp_promedio:.2f} °C\n")
        salida.write(f"Temperatura máxima: {temp_maxima:.2f} °C\n")
        salida.write(f"Temperatura mínima: {temp_minima:.2f} °C\n")
    else:
        salida.write("No se encontraron datos válidos en el archivo.\n")

print("Archivo resumen_temperaturas.txt creado con éxito.")
