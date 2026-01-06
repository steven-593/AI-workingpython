import pandas as pd
import numpy as np
import os
import joblib

# Importaciones de Scikit-Learn necesarias para el Pipeline
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

def train_salary_model():
    # 1. CARGA DE DATOS
    if not os.path.exists('salarydataset.csv'):
        print("Error: No se encontró el archivo salarydataset.csv")
        return
    
    df = pd.read_csv('salarydataset.csv')

    # 2. LIMPIEZA DE DATOS (Requisito: Handling missing values)
    # Eliminamos filas donde el objetivo (Salary) sea nulo
    df = df.dropna(subset=['Salary'])
    
    # Estandarizamos niveles educativos para evitar duplicados por escritura
    df['Education Level'] = df['Education Level'].replace({
        "Bachelor's": "Bachelor's Degree",
        "Master's": "Master's Degree",
        "phD": "PhD"
    })

    # 3. SELECCIÓN DE VARIABLES (Tal como pide el PDF)
    X = df[['Age', 'Gender', 'Education Level', 'Job Title', 'Years of Experience']]
    y = df['Salary']

    # 4. DEFINICIÓN DEL PIPELINE (Requisito obligatorio: 10 pts)
    # Columnas por tipo
    numeric_features = ['Age', 'Years of Experience']
    categorical_features = ['Gender', 'Education Level', 'Job Title']

    # Transformador para números (Imputación por mediana + Escalado)
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])

    # Transformador para categorías (Imputación por el más frecuente + OneHot)
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    # Preprocesador que combina ambos
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])

    # 5. DIVISIÓN DE DATOS (Requisito: 80% / 20%)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42
    )

    # 6. CREACIÓN DEL MODELO FINAL (Pipeline + Regressor)
    # Se utiliza RandomForestRegressor como permite el PDF
    model_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
    ])

    # 7. ENTRENAMIENTO
    print("Entrenando el modelo...")
    model_pipeline.fit(X_train, y_train)

    # 8. EVALUACIÓN (Requisito: Reportar MAE y R2)
    y_pred = model_pipeline.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("\n" + "="*30)
    print("MÉTRICAS DEL MODELO")
    print("="*30)
    print(f"Error Absoluto Medio (MAE): {mae:.2f}")
    print(f"Coeficiente de determinación (R2): {r2:.4f}")
    print("="*30)

    # 9. PERSISTENCIA (Guardar el modelo)
    if not os.path.exists('model'):
        os.makedirs('model')
    
    joblib.dump(model_pipeline, 'model/salary_model.pkl')
    print("\n✅ Modelo guardado exitosamente en: model/salary_model.pkl")

if __name__ == "__main__":
    train_salary_model()