# Basic Student Management Project

This is a basic student management project implemented with Python and Flask. It allows CRUD (Create, Read, Update, Delete) operations on a CSV file that stores student information. Each student has a name, course, and grade, and the information is managed through a web interface.
## Features

-. **Student View:** Displays a list of students on the home page.
-. **Add Student:** Allows adding a new student with their name, course, and grade.
-. **Edit Student:** Modifies the information of an existing student.
-. **Delete Student:** Removes a student from the list.
-. **CSV Storage:** Student data is saved in a registro.csv file
## Requirements

- **Python** 3.x
- **Flask** (Install using pip install flask)
## Installation

  1. Clone the repository:
    
    git clone https://github.com/Kaspaski-dev/students-database-Makilisword.git


2.Access the project directory:
  cd basic-project

3.Install Flask if you haven't done so already:
  pip install flask

## Project Structure

mi_aplicacion.py: Main file that starts the Flask application.

gestion.py: Contains the Student and StudentRecord classes to handle student logic.

templates/: Folder that contains the HTML templates (files index.html, agregar_estudiante.html, editar_estudiante.html).

registro.csv: CSV file where student information is stored.

## Execution 

1.Run the Flask server from the terminal:
  python mi_aplicacion.py

2.Open your browser and go to:
 http://127.0.0.1:5000.

## Here’s the translation
/: Home page that displays the list of students.
/agregar: Form to add a new student.
/editar/<name>: Page to edit the information of a specific student.
/eliminar/<name>: Route to delete a specific student.

## Example Data
The registro.csv file must follow this format to correctly store student data: 
name,course,grade.