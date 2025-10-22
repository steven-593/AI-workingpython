from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "secret_key_123"

# Configuración de la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estudiantes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de la base de datos
class Estudiante(db.Model):
    __tablename__ = 'estudiantes'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    carrera = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'<Estudiante {self.nombre}>'

# Crear las tablas en la base de datos
with app.app_context():
    db.create_all()
    
    # Agregar datos iniciales si la tabla está vacía
    if Estudiante.query.count() == 0:
        estudiante1 = Estudiante(nombre="Ana López", carrera="Informática", edad=21)
        estudiante2 = Estudiante(nombre="Carlos Ruiz", carrera="Electrónica", edad=23)
        db.session.add(estudiante1)
        db.session.add(estudiante2)
        db.session.commit()

# 🏠 Página principal
@app.route('/')
def home():
    estudiantes = Estudiante.query.all()
    return render_template('index.html', estudiantes=estudiantes)

# ➕ Crear estudiante
@app.route('/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        nombre = request.form['nombre']
        carrera = request.form['carrera']
        edad = request.form['edad']
        
        nuevo_estudiante = Estudiante(nombre=nombre, carrera=carrera, edad=edad)
        db.session.add(nuevo_estudiante)
        db.session.commit()
        
        flash('✅ Estudiante agregado correctamente', 'success')
        return redirect(url_for('home'))
    
    return render_template('create.html')

# ✏️ Editar estudiante
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    estudiante = Estudiante.query.get_or_404(id)
    
    if request.method == 'POST':
        estudiante.nombre = request.form['nombre']
        estudiante.carrera = request.form['carrera']
        estudiante.edad = request.form['edad']
        
        db.session.commit()
        
        flash('📝 Estudiante actualizado correctamente', 'success')
        return redirect(url_for('home'))
    
    return render_template('edit.html', id=id, estudiante=estudiante)

# 🗑️ Eliminar estudiante
@app.route('/delete/<int:id>')
def delete_user(id):
    estudiante = Estudiante.query.get(id)
    
    if estudiante:
        db.session.delete(estudiante)
        db.session.commit()
        flash('🗑️ Estudiante eliminado', 'error')
    else:
        flash('⚠️ Estudiante no encontrado', 'warning')
    
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)