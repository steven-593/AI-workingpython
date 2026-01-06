# simulate_data.py
import random, csv, datetime
import math

def simulate_row(day_idx):
    # temperatura (°C) fluctuación diaria y estacional
    base_temp = 18 + 10 * math.sin(day_idx * 2*math.pi / 365)  # temporada anual
    daily_temp = base_temp + random.gauss(0, 3)
    # ventas: función simple: ventas = a * temp + ruido, con saturación
    a = 12
    ventas = max(0, int(a * (daily_temp - 10) + random.gauss(0, 20)))
    return {
        "timestamp": (datetime.datetime.now() - datetime.timedelta(days=365-day_idx)).isoformat(),
        "temperature": round(daily_temp, 2),
        "sales": ventas
    }

# generar CSV de ejemplo con 365 días
with open("historical_icecream.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["timestamp","temperature","sales"])
    writer.writeheader()
    for i in range(365):
        writer.writerow(simulate_row(i))
print("historical_icecream.csv creado")
