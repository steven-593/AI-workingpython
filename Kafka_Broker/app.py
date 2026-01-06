from flask import Flask, jsonify, request
from kafka import KafkaProducer
import json
import random

app = Flask(__name__)

# Inicializar productor Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

@app.route('/enviar', methods=['POST'])
def enviar_datos():
    """
    Envía datos de helados: temperatura y ventas.
    Si no envías nada, los genera aleatorios.
    """

    contenido = request.json

    # Si no mandan datos, generamos automáticamente
    temperatura = contenido.get("temperatura", round(random.uniform(20, 35), 2))
    ventas = contenido.get("ventas", random.randint(30, 120))

    data = {
        "temperatura": temperatura,
        "ventas": ventas
    }

    # Envío a Kafka
    producer.send("Registro", value=data)
    producer.flush()

    return jsonify({
        "mensaje": "Datos enviados correctamente",
        "topic": "Registro",
        "data": data
    }), 200


@app.route('/')
def index():
    return "Producer Flask funcionando — Topic: Registro"


if __name__ == "__main__":
    app.run(port=5001, debug=True)
