import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    mean_squared_error,
    classification_report
)
from sklearn.preprocessing import LabelEncoder
import joblib

# =========================
# 1. CARGA DEL DATASET
# =========================
df = pd.read_csv("Iris.csv")

print("Primeras filas del dataset:")
print(df.head())

print("\nColumnas del dataset:")
print(df.columns)

# =========================
# 2. SELECCIÓN DE VARIABLES
# =========================
X = df[
    ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]
]

y = df["Species"]

# =========================
# 3. DIVISIÓN DE DATOS (70% / 30%)
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

# Tabla resumen de la división
tabla_division = pd.DataFrame({
    "Conjunto": ["Entrenamiento", "Pruebas", "Total"],
    "Número de muestras": [
        X_train.shape[0],
        X_test.shape[0],
        df.shape[0]
    ],
    "Porcentaje": ["70%", "30%", "100%"]
})

print("\nTabla de división del dataset:")
print(tabla_division)

# =========================
# 4. ENTRENAMIENTO DEL MODELO
# =========================
modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(X_train, y_train)

# =========================
# 5. PREDICCIONES
# =========================
y_pred = modelo.predict(X_test)

# =========================
# 6. EVALUACIÓN DEL MODELO
# =========================

# Métricas de clasificación
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average="weighted")
recall = recall_score(y_test, y_pred, average="weighted")
f1 = f1_score(y_test, y_pred, average="weighted")

# ---- MSE (requiere datos numéricos) ----
encoder = LabelEncoder()
y_test_num = encoder.fit_transform(y_test)
y_pred_num = encoder.transform(y_pred)

mse = mean_squared_error(y_test_num, y_pred_num)

# =========================
# 7. RESULTADOS
# =========================
print("\n📊 RESULTADOS DE LA EVALUACIÓN DEL MODELO")
print("----------------------------------------")
print(f"Precisión (Accuracy): {accuracy:.4f}")
print(f"Precision:            {precision:.4f}")
print(f"Recall:               {recall:.4f}")
print(f"F1-score:             {f1:.4f}")
print(f"Error Cuadrático Medio (MSE): {mse:.4f}")

print("\nReporte de clasificación:")
print(classification_report(y_test, y_pred))

# =========================
# 10. GUARDAR EL MODELO
# =========================

joblib.dump(modelo, "modelo_iris.pkl")
joblib.dump(encoder, "encoder_species.pkl")

print("\n✅ Modelo guardado como 'modelo_iris.pkl'")
print("✅ Encoder guardado como 'encoder_species.pkl'")
