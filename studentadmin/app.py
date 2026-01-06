from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from datetime import date

# ========================================
# CONFIGURACIÓN INICIAL
# ========================================
app = Flask(__name__)
CORS(app)  # Permite peticiones desde cliente externo
# Clave secreta (para mensajes flash)
app.secret_key = os.environ.get('SECRET_KEY', 'secret_key_123')
# Configuración de conexión MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flaskuser:12345@localhost/studentdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_size': 10,
    'pool_recycle': 3600,
    'pool_pre_ping': True,
}
# Inicializar SQLAlchemy
db = SQLAlchemy(app)
# ========================================
# MODELO DE BASE DE DATOS
# ========================================
class Estudiante(db.Model):
    __tablename__ = 'students'  # Coincide con la tabla real de MySQL

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    age = db.Column(db.Integer)
    enrollment_date = db.Column(db.Date)
    def __repr__(self):
        return f'<Estudiante {self.name}>'
    def to_dict(self):
        """Convierte el objeto Estudiante en un diccionario JSON"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'age': self.age,
            'enrollment_date': str(self.enrollment_date) if self.enrollment_date else None
        }
# ========================================
# CREAR TABLAS Y DATOS INICIALES
# ========================================
with app.app_context():
    try:
        db.create_all()

        # Agregar datos iniciales si la tabla está vacía
        if Estudiante.query.count() == 0:
            estudiante1 = Estudiante(name="Ana López", email="ana@example.com", age=21, enrollment_date=date.today())
            estudiante2 = Estudiante(name="Carlos Ruiz", email="carlos@example.com", age=23, enrollment_date=date.today())
            db.session.add_all([estudiante1, estudiante2])
            db.session.commit()
            print("✅ Base de datos inicializada con datos de ejemplo")
    except Exception as e:
        print(f"❌ Error al conectar con MySQL: {e}")
        print("Verifica que MySQL esté corriendo y la base 'studentdb' exista.")

# ========================================
# RUTAS WEB
# ========================================

@app.route('/')
def home():
    try:
        estudiantes = Estudiante.query.all()
        return render_template('index.html', estudiantes=estudiantes)
    except Exception as e:
        flash(f'❌ Error al cargar estudiantes: {str(e)}', 'error')
        return render_template('index.html', estudiantes=[])

@app.route('/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            age = request.form['age']
            enrollment_date = date.today()

            nuevo_estudiante = Estudiante(
                name=name,
                email=email,
                age=age,
                enrollment_date=enrollment_date
            )
            db.session.add(nuevo_estudiante)
            db.session.commit()

            flash('✅ Estudiante agregado correctamente', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            db.session.rollback()
            flash(f'❌ Error al agregar estudiante: {str(e)}', 'error')
    return render_template('create.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    estudiante = Estudiante.query.get_or_404(id)

    if request.method == 'POST':
        try:
            estudiante.name = request.form['name']
            estudiante.email = request.form['email']
            estudiante.age = request.form['age']
            db.session.commit()
            flash('📝 Estudiante actualizado correctamente', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            db.session.rollback()
            flash(f'❌ Error al editar estudiante: {str(e)}', 'error')
    return render_template('edit.html', estudiante=estudiante)

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

# ========================================
# API REST JSON
# ========================================

@app.route('/api/estudiantes', methods=['GET'])
def api_get_estudiantes():
    try:
        estudiantes = Estudiante.query.all()
        return {'success': True, 'data': [e.to_dict() for e in estudiantes]}, 200
    except Exception as e:
        return {'success': False, 'error': str(e)}, 500

@app.route('/api/estudiantes/<int:id>', methods=['GET'])
def api_get_estudiante(id):
    estudiante = Estudiante.query.get_or_404(id)
    return {'success': True, 'data': estudiante.to_dict()}, 200

@app.route('/api/estudiantes', methods=['POST'])
def api_create_estudiante():
    try:
        data = request.get_json()
        nuevo = Estudiante(
            name=data['name'],
            email=data['email'],
            age=data['age'],
            enrollment_date=date.today()
        )
        db.session.add(nuevo)
        db.session.commit()
        return {'success': True, 'message': 'Estudiante creado correctamente', 'data': nuevo.to_dict()}, 201
    except Exception as e:
        db.session.rollback()
        return {'success': False, 'error': str(e)}, 400

@app.route('/api/estudiantes/<int:id>', methods=['PUT'])
def api_update_estudiante(id):
    try:
        estudiante = Estudiante.query.get_or_404(id)
        data = request.get_json()

        estudiante.name = data.get('name', estudiante.name)
        estudiante.email = data.get('email', estudiante.email)
        estudiante.age = data.get('age', estudiante.age)
        db.session.commit()

        return {'success': True, 'message': 'Estudiante actualizado correctamente', 'data': estudiante.to_dict()}, 200
    except Exception as e:
        db.session.rollback()
        return {'success': False, 'error': str(e)}, 400

@app.route('/api/estudiantes/<int:id>', methods=['DELETE'])
def api_delete_estudiante(id):
    try:
        estudiante = Estudiante.query.get_or_404(id)
        db.session.delete(estudiante)
        db.session.commit()
        return {'success': True, 'message': 'Estudiante eliminado correctamente'}, 200
    except Exception as e:
        db.session.rollback()
        return {'success': False, 'error': str(e)}, 400

# ========================================
# INICIO DE LA APLICACIÓN
# ========================================

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
