# Basic Student Management Project

Este es un proyecto básico de gestión de estudiantes implementado con Python y Flask. Permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre un archivo CSV que almacena información de estudiantes. Cada estudiante tiene un nombre, curso y nota, y la información se gestiona a través de una interfaz web.

## Características

- **Visualización de estudiantes:** Muestra una lista de estudiantes en la página de inicio.
- **Agregar estudiante:** Permite añadir un nuevo estudiante con su nombre, curso y nota.
- **Editar estudiante:** Modifica la información de un estudiante existente.
- **Eliminar estudiante:** Elimina un estudiante de la lista.
- **Almacenamiento en CSV:** Los datos de estudiantes se guardan en un archivo `registro.csv`.

## Requisitos

- **Python** 3.x
- **Flask** (Instalar usando `pip install flask`)

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/FernadoKitzune/basic-project.git

2.Accede al directorio del proyecto:
  cd basic-project

3.Instala Flask si no lo tienes ya instalado:
  pip install flask

## Estructura del Proyecto
mi_aplicacion.py: Archivo principal que inicia la aplicación Flask.

gestion.py: Contiene las clases Estudiante y RegistroEstudiantes para manejar la lógica de estudiantes.

templates/: Carpeta que contiene las plantillas HTML (archivos index.html, agregar_estudiante.html, editar_estudiante.html).

registro.csv: Archivo CSV en el cual se almacena la información de los estudiantes.

## Ejecucion 

1.Ejecuta el servidor Flask desde la terminal:
  python mi_aplicacion.py

2.Abre tu navegador y accede a:
 http://127.0.0.1:5000.

## Rutas de la Aplicación
/: Página de inicio que muestra la lista de estudiantes.
/agregar: Formulario para agregar un nuevo estudiante.
/editar/<nombre>: Página para editar la información de un estudiante específico.
/eliminar/<nombre>: Ruta para eliminar un estudiante específico.

## Ejemplo de Datos
El archivo registro.csv debe seguir este formato para almacenar correctamente los datos de los estudiantes:
nombre,curso,nota.