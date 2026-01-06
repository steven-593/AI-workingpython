# consumer_sqlite.py
import json, sqlite3
from kafka import KafkaConsumer

conn = sqlite3.connect("icecream.db")
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    temperature REAL,
    sales INTEGER
)
""")
conn.commit()

consumer = KafkaConsumer(
    'icecream.topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

for msg in consumer:
    ev = msg.value
    c.execute("INSERT INTO sales (timestamp, temperature, sales) VALUES (?, ?, ?)",
              (ev['timestamp'], ev['temperature'], ev['sales']))
    conn.commit()
    print("Insertado en SQLite:", ev)
