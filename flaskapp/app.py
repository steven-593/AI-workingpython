from flask import Flask, render_template, jsonify

app = Flask(__name__)

# === DICCIONARIO DE USUARIOS ===
usuarios = {
    "Steven": 22,
    "María": 25
}

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para ver usuarios
@app.route('/usuarios')
def mostrar_usuarios():
    return render_template('user.html', usuarios=usuarios)

# API para obtener el saludo dinámico
@app.route('/saludo/<nombre>')
def saludo(nombre):
    return jsonify({"mensaje": f"✨ ¡Hola, {nombre}! Bienvenido a tu aplicación Flask."})

# API que devuelve usuarios en JSON (opcional)
@app.route('/api/usuarios')
def api_usuarios():
    return jsonify(usuarios)

if __name__ == '__main__':
    app.run(debug=True)
