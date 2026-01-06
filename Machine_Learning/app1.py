import pandas as pd
from sklearn.model_selection import train_test_split

# 1. Cargar el dataset CSV con Pandas
df = pd.read_csv("Iris.csv")

# 2. Verificar columnas (opcional)
print("Columnas del dataset:")
print(df.columns)

# 3. Variables independientes (features)
X = df[[
    "SepalLengthCm",
    "SepalWidthCm",
    "PetalLengthCm",
    "PetalWidthCm"
]]

# 4. Variable dependiente (label)
y = df["Species"]

# 5. División 70% entrenamiento - 30% prueba
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

# 6. Crear tabla resumen de la división de datos
tabla_division = pd.DataFrame({
    "Conjunto": ["Entrenamiento", "Pruebas", "Total"],
    "Número de muestras": [
        X_train.shape[0],
        X_test.shape[0],
        df.shape[0]
    ],
    "Porcentaje": ["70%", "30%", "100%"]
})

# 7. Mostrar tabla
print("\nTabla de división del dataset:")
print(tabla_division)
