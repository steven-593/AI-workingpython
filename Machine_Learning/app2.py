import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    mean_squared_error
)
from sklearn.preprocessing import LabelEncoder

# 1. Cargar el dataset CSV con Pandas
df = pd.read_csv("Iris.csv")

# 2. Verificar columnas
print("Columnas del dataset:")
print(df.columns)

# 3. Variables independientes (features)
X = df[
    ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]
]

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

# 6. Crear y entrenar el modelo
modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(X_train, y_train)

# 7. Predicciones
y_pred = modelo.predict(X_test)

# =========================
# 8. EVALUACIÓN DEL MODELO
# =========================

# Precisión, Recall y F1-score (clasificación)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average="weighted")
recall = recall_score(y_test, y_pred, average="weighted")
f1 = f1_score(y_test, y_pred, average="weighted")

# ---- MSE (requiere valores numéricos) ----
encoder = LabelEncoder()
y_test_num = encoder.fit_transform(y_test)
y_pred_num = encoder.transform(y_pred)

mse = mean_squared_error(y_test_num, y_pred_num)

# 9. Mostrar resultados
print("\n📊 Resultados de la evaluación del modelo")
print("----------------------------------------")
print(f"Precisión (Accuracy): {accuracy:.4f}")
print(f"Precision:            {precision:.4f}")
print(f"Recall:               {recall:.4f}")
print(f"F1-score:             {f1:.4f}")
print(f"Error cuadrático medio (MSE): {mse:.4f}")
