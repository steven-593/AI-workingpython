# producer.py
import json, time, random, datetime
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_event():
    temp = round(random.gauss(25, 4),2)
    sales = max(0, int(12 * (temp - 10) + random.gauss(0,15)))
    return {
        "timestamp": datetime.datetime.now().isoformat(),
        "temperature": temp,
        "sales": sales
    }

if __name__ == "__main__":
    while True:
        event = generate_event()
        producer.send('icecream.topic', event)
        print("Publicado:", event)
        time.sleep(5)  # cada 5s
