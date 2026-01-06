# realtime_predictor.py
import joblib, json
from kafka import KafkaConsumer

model = joblib.load("linreg_icecream.pkl")
consumer = KafkaConsumer('icecream.topic', bootstrap_servers='localhost:9092', value_deserializer=lambda v: json.loads(v.decode()))

for msg in consumer:
    ev = msg.value
    temp = float(ev['temperature'])
    pred = model.predict([[temp]])
    print("Temp:", temp, "Predicted sales:", int(pred[0]))
