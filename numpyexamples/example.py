import numpy as np

# Crear un arreglo de números
arr = np.array([1, 2, 3, 4, 5])
print("Arreglo original:", arr)

# Sumar 5 a cada elemento
arr_sum = arr + 5
print("Arreglo + 5:", arr_sum)

# Multiplicar cada elemento por 2
arr_mult = arr * 2
print("Arreglo * 2:", arr_mult)

# Calcular la media y la suma
print("Media del arreglo:", np.mean(arr))
print("Suma de los elementos:", np.sum(arr))

# Crear una matriz 2x3
matriz = np.array([[1, 2, 3],
                   [4, 5, 6]])
print("Matriz:\n", matriz)

# Transponer la matriz
print("Matriz transpuesta:\n", matriz.T)
