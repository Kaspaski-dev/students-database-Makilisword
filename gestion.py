import csv 

def leer_estudiantes(archivo="registro.csv"):
    estudiantes = []
    try:
        with open(archivo, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)  # Usar DictReader para simplificar el manejo de datos
            for row in reader:
                estudiantes.append(row)  # Cada fila ya es un diccionario
    except FileNotFoundError:
        print("Error: El archivo no fue encontrado.")
    return estudiantes

def agregar_estudiante(nombre, curso, nota, archivo="registro.csv"):
    with open(archivo, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([nombre, curso, nota])  # Escribir en el CSV

def editar_estudiante(nombre, nuevo_nombre, curso, nota, archivo="registro.csv"):
    estudiantes = leer_estudiantes(archivo)
    for estudiante in estudiantes:
        if estudiante['nombre'] == nombre:  # Cambia 'Nombre' a 'nombre'
            estudiante['nombre'] = nuevo_nombre
            estudiante['curso'] = curso
            estudiante['nota'] = nota
            break
    # Escribir los cambios en el archivo
    with open(archivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['nombre', 'curso', 'nota'])  # Cambia 'Nombre' a 'nombre'
        writer.writeheader()  # Escribir encabezado
        writer.writerows(estudiantes)  # Escribir todas las filas a la vez

def eliminar_estudiante(nombre, archivo="registro.csv"):
    estudiantes = leer_estudiantes(archivo)
    estudiantes = [e for e in estudiantes if e['nombre'] != nombre]  # Cambia 'Nombre' a 'nombre'
    # Escribir los cambios en el archivo
    with open(archivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['nombre', 'curso', 'nota'])  # Cambia 'Nombre' a 'nombre'
        writer.writeheader()  # Escribir encabezado
        writer.writerows(estudiantes)  # Escribir todas las filas a la vez
