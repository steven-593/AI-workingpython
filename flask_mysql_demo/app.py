from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Habilitar CORS para peticiones cliente-servidor

# Configuración de seguridad
app.secret_key = os.environ.get('SECRET_KEY', 'secret_key_123')

# Configuración de MySQL
# Puedes usar variables de entorno para mayor seguridad
MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '')
MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
MYSQL_PORT = os.environ.get('MYSQL_PORT', '3306')
MYSQL_DB = os.environ.get('MYSQL_DB', 'students_db')

# URI de conexión MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_size': 10,
    'pool_recycle': 3600,
    'pool_pre_ping': True,
}

db = SQLAlchemy(app)

# Modelo de la base de datos
class Estudiante(db.Model):
    __tablename__ = 'estudiantes'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    carrera = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'<Estudiante {self.nombre}>'
    
    def to_dict(self):
        """Convertir el objeto a diccionario para API REST"""
        return {
            'id': self.id,
            'nombre': self.nombre,
            'carrera': self.carrera,
            'edad': self.edad
        }

# Crear las tablas en la base de datos
with app.app_context():
    try:
        db.create_all()
        
        # Agregar datos iniciales si la tabla está vacía
        if Estudiante.query.count() == 0:
            estudiante1 = Estudiante(nombre="Ana López", carrera="Informática", edad=21)
            estudiante2 = Estudiante(nombre="Carlos Ruiz", carrera="Electrónica", edad=23)
            db.session.add(estudiante1)
            db.session.add(estudiante2)
            db.session.commit()
            print("✅ Base de datos inicializada con datos de ejemplo")
    except Exception as e:
        print(f"❌ Error al conectar con MySQL: {e}")
        print("Asegúrate de que MySQL esté ejecutándose y la base de datos exista")

# 🏠 Página principal
@app.route('/')
def home():
    try:
        estudiantes = Estudiante.query.all()
        return render_template('index.html', estudiantes=estudiantes)
    except Exception as e:
        flash(f'❌ Error al cargar estudiantes: {str(e)}', 'error')
        return render_template('index.html', estudiantes=[])

# ➕ Crear estudiante
@app.route('/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            carrera = request.form['carrera']
            edad = request.form['edad']
            
            nuevo_estudiante = Estudiante(nombre=nombre, carrera=carrera, edad=edad)
            db.session.add(nuevo_estudiante)
            db.session.commit()
            
            flash('✅ Estudiante agregado correctamente', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            db.session.rollback()
            flash(f'❌ Error al agregar estudiante: {str(e)}', 'error')
    
    return render_template('create.html')

# ✏️ Editar estudiante
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    try:
        estudiante = Estudiante.query.get_or_404(id)
        
        if request.method == 'POST':
            estudiante.nombre = request.form['nombre']
            estudiante.carrera = request.form['carrera']
            estudiante.edad = request.form['edad']
            
            db.session.commit()
            
            flash('📝 Estudiante actualizado correctamente', 'success')
            return redirect(url_for('home'))
        
        return render_template('edit.html', id=id, estudiante=estudiante)
    except Exception as e:
        db.session.rollback()
        flash(f'❌ Error al editar estudiante: {str(e)}', 'error')
        return redirect(url_for('home'))

# 🗑️ Eliminar estudiante
@app.route('/delete/<int:id>')
def delete_user(id):
    try:
        estudiante = Estudiante.query.get(id)
        
        if estudiante:
            db.session.delete(estudiante)
            db.session.commit()
            flash('🗑️ Estudiante eliminado', 'success')
        else:
            flash('⚠️ Estudiante no encontrado', 'warning')
    except Exception as e:
        db.session.rollback()
        flash(f'❌ Error al eliminar estudiante: {str(e)}', 'error')
    
    return redirect(url_for('home'))


# ====== API REST para peticiones cliente-servidor ======

@app.route('/api/estudiantes', methods=['GET'])
def api_get_estudiantes():
    """Obtener todos los estudiantes (formato JSON)"""
    try:
        estudiantes = Estudiante.query.all()
        return {
            'success': True,
            'data': [e.to_dict() for e in estudiantes]
        }, 200
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }, 500

@app.route('/api/estudiantes/<int:id>', methods=['GET'])
def api_get_estudiante(id):
    """Obtener un estudiante por ID"""
    try:
        estudiante = Estudiante.query.get_or_404(id)
        return {
            'success': True,
            'data': estudiante.to_dict()
        }, 200
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }, 404

@app.route('/api/estudiantes', methods=['POST'])
def api_create_estudiante():
    """Crear un nuevo estudiante"""
    try:
        data = request.get_json()
        
        nuevo_estudiante = Estudiante(
            nombre=data['nombre'],
            carrera=data['carrera'],
            edad=data['edad']
        )
        db.session.add(nuevo_estudiante)
        db.session.commit()
        
        return {
            'success': True,
            'message': 'Estudiante creado correctamente',
            'data': nuevo_estudiante.to_dict()
        }, 201
    except Exception as e:
        db.session.rollback()
        return {
            'success': False,
            'error': str(e)
        }, 400

@app.route('/api/estudiantes/<int:id>', methods=['PUT'])
def api_update_estudiante(id):
    """Actualizar un estudiante"""
    try:
        estudiante = Estudiante.query.get_or_404(id)
        data = request.get_json()
        
        estudiante.nombre = data.get('nombre', estudiante.nombre)
        estudiante.carrera = data.get('carrera', estudiante.carrera)
        estudiante.edad = data.get('edad', estudiante.edad)
        
        db.session.commit()
        
        return {
            'success': True,
            'message': 'Estudiante actualizado correctamente',
            'data': estudiante.to_dict()
        }, 200
    except Exception as e:
        db.session.rollback()
        return {
            'success': False,
            'error': str(e)
        }, 400

@app.route('/api/estudiantes/<int:id>', methods=['DELETE'])
def api_delete_estudiante(id):
    """Eliminar un estudiante"""
    try:
        estudiante = Estudiante.query.get_or_404(id)
        db.session.delete(estudiante)
        db.session.commit()
        
        return {
            'success': True,
            'message': 'Estudiante eliminado correctamente'
        }, 200
    except Exception as e:
        db.session.rollback()
        return {
            'success': False,
            'error': str(e)
        }, 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)