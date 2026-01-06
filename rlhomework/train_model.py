import pandas as pd
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

def entrenar_modelo():
    # 1. Cargar el dataset
    if not os.path.exists('salarydataset.csv'):
        print("Error: No se encontró el archivo 'salarydataset.csv'")
        return
    
    df = pd.read_csv('salarydataset.csv')

    # 2. Limpieza de datos (Manejo de valores nulos)
    df.dropna(subset=['Salary'], inplace=True)
    df['Education Level'] = df['Education Level'].replace({
        "Bachelor's": "Bachelor's Degree",
        "Master's": "Master's Degree",
        "phD": "PhD"
    })

    # 3. Definir variables
    X = df[['Age', 'Gender', 'Education Level', 'Job Title', 'Years of Experience']]
    y = df['Salary']

    # 4. Pipeline de Preprocesamiento (Requisito de la rúbrica)
    columnas_numericas = ['Age', 'Years of Experience']
    columnas_categoricas = ['Gender', 'Education Level', 'Job Title']

    transformador_numerico = Pipeline(steps=[
        ('imputador', SimpleImputer(strategy='median')),
        ('escalador', StandardScaler())
    ])

    transformador_categorico = Pipeline(steps=[
        ('imputador', SimpleImputer(strategy='most_frequent')),
        ('codificador', OneHotEncoder(handle_unknown='ignore'))
    ])

    preprocesador = ColumnTransformer(transformers=[
        ('num', transformador_numerico, columnas_numericas),
        ('cat', transformador_categorico, columnas_categoricas)
    ])

    # 5. División de datos (80% entrenamiento / 20% prueba)
    X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 6. Comparación de Modelos (BONUS +5 pts)
    print("--- Evaluando Modelos ---")
    
    # Regresión Lineal
    modelo_lr = Pipeline(steps=[('pre', preprocesador), ('reg', LinearRegression())])
    modelo_lr.fit(X_entrenamiento, y_entrenamiento)
    pred_lr = modelo_lr.predict(X_prueba)
    print(f"Regresión Lineal -> MAE: {mean_absolute_error(y_prueba, pred_lr):.2f}, R2: {r2_score(y_prueba, pred_lr):.4f}")

    # Random Forest
    modelo_rf = Pipeline(steps=[('pre', preprocesador), ('reg', RandomForestRegressor(random_state=42))])
    modelo_rf.fit(X_entrenamiento, y_entrenamiento)
    pred_rf = modelo_rf.predict(X_prueba)
    print(f"Random Forest     -> MAE: {mean_absolute_error(y_prueba, pred_rf):.2f}, R2: {r2_score(y_prueba, pred_rf):.4f}")

    # 7. Guardar/Exportar el mejor modelo (Persistencia)
    if not os.path.exists('model'):
        os.makedirs('model')
    
    joblib.dump(modelo_rf, 'model/salary_model.pkl')
    print("\n✅ Modelo exportado correctamente a 'model/salary_model.pkl'")

if __name__ == "__main__":
    entrenar_modelo()