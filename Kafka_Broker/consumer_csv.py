# consumer_csv.py
import json, csv
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'icecream.topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

with open("stream_icecream.csv","a", newline="") as f:
    writer = csv.writer(f)
    for msg in consumer:
        ev = msg.value
        writer.writerow([ev['timestamp'], ev['temperature'], ev['sales']])
        print("Guardado en CSV:", ev)
