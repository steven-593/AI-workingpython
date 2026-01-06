from flask import Flask, render_template, request, redirect, url_for
import joblib
import numpy as np

app = Flask(__name__)

# Cargar modelo
model = joblib.load('iris_logistic_model.pkl')

@app.route('/')
def index():
    prediction = request.args.get('prediction')
    return render_template('index.html', prediction=prediction)

@app.route('/predict', methods=['POST'])
def predict():
    sepal_length = float(request.form['sepal_length'])
    sepal_width = float(request.form['sepal_width'])
    petal_length = float(request.form['petal_length'])
    petal_width = float(request.form['petal_width'])

    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    resultado = model.predict(features)[0]

    # Redirige y limpia el formulario
    return redirect(url_for('index', prediction=resultado))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
