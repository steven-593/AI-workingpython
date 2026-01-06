from flask import Flask, render_template, request
import pandas as pd
import joblib
import os
import matplotlib
matplotlib.use('Agg') # Para que funcione en servidor sin interfaz gráfica
import matplotlib.pyplot as plt
import io
import base64
import seaborn as sns

app = Flask(__name__)

# Cargar el modelo exportado anteriormente
ruta_modelo = 'model/salary_model.pkl'
modelo = joblib.load(ruta_modelo)
df_datos = pd.read_csv('salarydataset.csv').dropna()

# Función para cargar cargos dinámicamente (BONUS +5 pts)
def obtener_puestos():
    return sorted(df_datos['Job Title'].unique().tolist())

def crear_grafico(exp_usuario, salario_predicho):
    plt.figure(figsize=(8, 6))
    
    # Mostrar una muestra de los datos reales para la línea de tendencia
    muestra = df_datos.sample(n=min(1000, len(df_datos)))
    sns.regplot(data=muestra, x='Years of Experience', y='Salary', 
                scatter_kws={'alpha':0.2, 'color':'gray', 's':10}, 
                line_kws={'color':'blue', 'label':'Tendencia del Mercado'})
    
    # Resaltar la posición del usuario en el gráfico
    plt.scatter(exp_usuario, salario_predicho, color='red', s=150, edgecolors='black', 
                label='Tu Predicción', zorder=5)
    
    plt.title('Análisis de Regresión: Experiencia vs Salario', fontsize=14)
    plt.xlabel('Años de Experiencia', fontsize=12)
    plt.ylabel('Salario Anual ($)', fontsize=12)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)

    # Convertir gráfico a imagen para HTML
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)
    imagen_base64 = base64.b64encode(buffer.getvalue()).decode()
    plt.close()
    return imagen_base64

@app.route('/')
def inicio():
    return render_template('index.html', puestos=obtener_puestos())

@app.route('/predecir', methods=['POST'])
def predecir():
    # Captura de datos del formulario
    exp = float(request.form['experiencia'])
    edad = float(request.form['edad'])
    genero = request.form['genero']
    educacion = request.form['educacion']
    puesto = request.form['puesto']

    # Crear el DataFrame para el Pipeline
    datos_entrada = pd.DataFrame({
        'Age': [edad],
        'Gender': [genero],
        'Education Level': [educacion],
        'Job Title': [puesto],
        'Years of Experience': [exp]
    })

    # Realizar predicción
    prediccion = modelo.predict(datos_entrada)[0]
    
    # Generar gráfico dinámico
    grafico = crear_grafico(exp, prediccion)

    return render_template('index.html', 
                           puestos=obtener_puestos(), 
                           resultado=f"{prediccion:,.2f}",
                           url_grafico=grafico)

if __name__ == '__main__':
    app.run(debug=True)