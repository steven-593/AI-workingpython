# eda_model.py
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("stream_icecream.csv", names=["timestamp","temperature","sales"], parse_dates=["timestamp"])
print(df.describe())
print(df.corr())

# Visualizar temperatura vs ventas
plt.scatter(df['temperature'], df['sales'])
plt.xlabel("Temperatura (°C)")
plt.ylabel("Ventas (unidades)")
plt.title("Ventas vs Temperatura")
plt.show()

# Agregar features útiles
df['hour'] = df['timestamp'].dt.hour
df['dayofweek'] = df['timestamp'].dt.dayofweek
