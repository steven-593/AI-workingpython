# ======================================================
#    REGRESIÓN LINEAL + GRAFICADO ASCII SIN LIBRERÍAS
# ======================================================

# Datos originales
X = [20, 25, 30, 35, 40]  #variable independiente input  Es lo que supones que provoca cambios en las ventas.
Y = [50, 55, 65, 70, 80]  #variable dependiente ouput    Depende de la temperatura.

# Promedios
prom_x = sum(X) / len(X)
prom_y = sum(Y) / len(Y)

# Cálculo de pendiente (m) e intercepto (b)
num = 0
den = 0
for i in range(len(X)):
    num += (X[i] - prom_x) * (Y[i] - prom_y)
    den += (X[i] - prom_x) ** 2

m = num / den
b = prom_y - m * prom_x

print("Pendiente m =", m)
print("Intercepto b =", b)
print("\nLínea resultante: y = {:.2f}x + {:.2f}".format(m, b))

# ======================================================
#                GRÁFICA ASCII
# ======================================================

# Crear valores de la línea recta para graficar
def predecir(x):
    return m * x + b

# Se genera una tabla ASCII simulando la gráfica
print("\nGRÁFICA ASCII (X=temperatura, Y=ventas)")
print("----------------------------------------")

# Escala para la gráfica
max_y = max(Y)
min_y = min(Y)

for y in range(max_y, min_y - 1, -5):
    linea = ""
    for x in X:
        y_real = Y[X.index(x)]
        y_linea = round(predecir(x))

        if abs(y_real - y) < 3:
            linea += " ● "     # punto real
        elif abs(y_linea - y) < 3:
            linea += " x "     # punto de la recta
        else:
            linea += "   "     # espacio vacío
    print(str(y).rjust(3), "|", linea)

print("     +" + "---" * len(X))
print("      ", "  ".join([str(x) for x in X]))

#----------------------------------------------------------------------------------------------------------
#INPUT: temperatura (X) variable independiente input  Es lo que supones que provoca cambios en las ventas.

#OUTPUT: ventas (Y) variable dependiente ouput    Depende de la temperatura.

#PREDICCIÓN:
#y​ =1.5x+19
	