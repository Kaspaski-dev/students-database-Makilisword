from flask import Flask, render_template, request, redirect, url_for, flash
import csv

app = Flask(__name__)

# Clase Estudiante
class Estudiante:
    def __init__(self, nombre, curso, nota):
        self.nombre = nombre
        self.curso = curso
        self.nota = nota

# Clase RegistroEstudiantes
class RegistroEstudiantes:
    def __init__(self, archivo):
        self.archivo = archivo

    def leer_estudiantes(self):
        estudiantes = []
        try:
            with open(self.archivo, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    estudiantes.append(Estudiante(row['nombre'], row['curso'], row['nota']))
        except FileNotFoundError:
            flash('El archivo no existe. Se creará uno nuevo.')
        except Exception as e:
            flash(f'Error al leer el archivo: {e}')
        return estudiantes

    def agregar_estudiante(self, estudiante):
        with open(self.archivo, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([estudiante.nombre, estudiante.curso, estudiante.nota])

    def editar_estudiante(self, nombre, nuevo_nombre, curso, nota):
        estudiantes = self.leer_estudiantes()
        for est in estudiantes:
            if est.nombre == nombre:
                est.nombre = nuevo_nombre
                est.curso = curso
                est.nota = nota
                break
        self._guardar_estudiantes(estudiantes)

    def eliminar_estudiante(self, nombre):
        estudiantes = self.leer_estudiantes()
        estudiantes = [est for est in estudiantes if est.nombre != nombre]
        self._guardar_estudiantes(estudiantes)

    def _guardar_estudiantes(self, estudiantes):
        with open(self.archivo, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['nombre', 'curso', 'nota'])  # Encabezados
            for est in estudiantes:
                writer.writerow([est.nombre, est.curso, est.nota])

registro = RegistroEstudiantes('registro.csv')

@app.route('/')
def index():
    print("Ruta de inicio accedida")
    estudiantes = registro.leer_estudiantes()
    return render_template('index.html', estudiantes=estudiantes)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        curso = request.form['curso']
        nota = request.form['nota']
        nuevo_estudiante = Estudiante(nombre, curso, nota)
        registro.agregar_estudiante(nuevo_estudiante)
        flash('Estudiante agregado exitosamente')
        return redirect(url_for('index'))
    return render_template('agregar_estudiante.html')

@app.route('/editar/<nombre>', methods=['GET', 'POST'])
def editar(nombre):
    if request.method == 'POST':
        nuevo_nombre = request.form['nombre']
        curso = request.form['curso']
        nota = request.form['nota']
        registro.editar_estudiante(nombre, nuevo_nombre, curso, nota)
        flash('Estudiante actualizado exitosamente')
        return redirect(url_for('index'))
    estudiante = next((e for e in registro.leer_estudiantes() if e.nombre == nombre), None)
    if estudiante:
        return render_template('editar_estudiante.html', estudiante=estudiante)
    else:
        flash('Estudiante no encontrado')
        return redirect(url_for('index'))

@app.route('/eliminar/<nombre>')
def eliminar(nombre):
    registro.eliminar_estudiante(nombre)
    flash('Estudiante eliminado exitosamente')
    return redirect(url_for('index'))

if __name__ == '__main__':
    print("Iniciando servidor Flask...")  
    app.run(debug=True, port=5000)

