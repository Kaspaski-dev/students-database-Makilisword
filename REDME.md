# Proyecto de Gestión de Estudiantes

Este es un proyecto de aplicación web desarrollado con Flask que permite gestionar un registro de estudiantes. La aplicación permite agregar, editar y eliminar estudiantes, así como visualizar su información.

## Características

- **Agregar Estudiantes:** Permite añadir nuevos estudiantes al registro con su nombre, curso y nota.
- **Editar Estudiantes:** Permite actualizar la información de los estudiantes existentes.
- **Eliminar Estudiantes:** Permite eliminar estudiantes del registro.
- **Visualización:** Muestra una lista de estudiantes registrados con su información.

## Tecnologías Utilizadas

- [Flask](https://flask.palletsprojects.com/en/3.0.x/) - Un microframework para Python que permite crear aplicaciones web.
- [HTML/CSS](https://www.w3schools.com/html/) - Para la estructura y diseño de las páginas web.
- [CSV](https://docs.python.org/3/library/csv.html) - Para almacenar los datos de los estudiantes en un archivo CSV.

## Requisitos

- Python 3.x
- Flask 3.0.x
- Librerías adicionales que se pueden instalar con `pip`.

## Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd BASIC_PROJECT

   Crear un entorno virtual (opcional, pero recomendado):
   python -m venv venv

**Activar el entorno virtual**
En Windows: venv\Scripts\activate
En macOS/Linux: source venv/bin/activate

**Instalar las dependencias**
pip install Flask

**Ejecutar la aplicación:**
export FLASK_APP=mi_aplicacion  # En Windows usar: set FLASK_APP=mi_aplicacion
export FLASK_ENV=development      # En Windows usar: set FLASK_ENV=development
flask run


