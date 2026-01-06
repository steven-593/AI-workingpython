from flask import Flask, render_template, request
import matplotlib
matplotlib.use('Agg')  # <- necesario para entornos sin interfaz gráfica
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

def calcular_regresion(X, Y):
    n = len(X)
    prom_x = sum(X) / n
    prom_y = sum(Y) / n

    num = sum((X[i] - prom_x) * (Y[i] - prom_y) for i in range(n))
    den = sum((X[i] - prom_x) ** 2 for i in range(n))

    if den == 0:
        return None, None

    m = num / den
    b = prom_y - m * prom_x
    return m, b


@app.route("/", methods=["GET", "POST"])
def index():
    m = None
    b = None
    grafico = None
    error = None

    if request.method == "POST":
        try:
            # --- LEER DATOS DEL FORMULARIO ---
            temps_raw = request.form["temperaturas"]
            ventas_raw = request.form["ventas"]

            X = [float(x.strip()) for x in temps_raw.split(",") if x.strip()]
            Y = [float(y.strip()) for y in ventas_raw.split(",") if y.strip()]

            # Validaciones
            if len(X) != len(Y):
                error = "Las listas deben tener la misma cantidad de elementos."
                return render_template("index.html", m=None, b=None, grafico=None, error=error)

            if len(X) < 2:
                error = "Debes ingresar al menos 2 datos."
                return render_template("index.html", m=None, b=None, grafico=None, error=error)

            # --- REGRESIÓN ---
            m, b = calcular_regresion(X, Y)

            if m is None:
                error = "No se pudo calcular la regresión."
                return render_template("index.html", m=None, b=None, grafico=None, error=error)

            # --- GENERAR GRÁFICO ---
            nombre_img = "grafico.png"
            ruta_img = os.path.join("static", nombre_img)

            plt.figure(figsize=(5,4))
            plt.scatter(X, Y, label="Datos reales", s=80)

            y_pred = [m * xi + b for xi in X]
            plt.plot(X, y_pred, color="red", label="Línea de regresión")

            plt.xlabel("Temperatura")
            plt.ylabel("Ventas")
            plt.legend()
            plt.tight_layout()

            plt.savefig(ruta_img)
            plt.close()

            grafico = nombre_img

        except Exception as e:
            error = "Error: Verifica los datos ingresados."
            print("ERROR INTERNO:", e)  # <-- aquí verás tu error real en consola

    return render_template("index.html", m=m, b=b, grafico=grafico, error=error)


if __name__ == "__main__":
    app.run(debug=True)
