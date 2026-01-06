import socket
import threading

# ← VERSIÓN CORREGIDA PARA DOCKER (solo cambia estas partes)
def get_local_ip():
    # Dentro de Docker esta es la forma más fiable y rápida
    return socket.gethostbyname(socket.gethostname())

def handle_client(client_socket, address):
    print(f"Cliente conectado: {address}")
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8').strip()
            if not data or data.lower() == "quit":
                break

            num1, num2, operation = data.split(',')
            num1 = float(num1)
            num2 = float(num2)

            if operation == "add":
                result = num1 + num2
            elif operation == "sub":
                result = num1 - num2
            elif operation == "mul":
                result = num1 * num2
            elif operation == "div":
                if num2 == 0:
                    response = "ERROR:División por cero"
                    client_socket.send(response.encode('utf-8'))
                    continue
                result = num1 / num2
            else:
                response = "ERROR:Operación no válida"
                client_socket.send(response.encode('utf-8'))
                continue

            response = f"RESULT:{result}"

        except Exception as e:
            response = "ERROR:Formato incorrecto"
        
        client_socket.send(response.encode('utf-8'))

    print(f"Cliente desconectado: {address}")
    client_socket.close()

# =================== CONFIGURACIÓN PARA DOCKER ===================
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('0.0.0.0', 5001))   # ¡¡OBLIGATORIO en Docker!!
server.listen(5)

# IP solo para mostrar (en Docker normalmente sale 172.17.x.x, pero no importa)
local_ip = get_local_ip()
print(f"SERVIDOR DOCKER LISTO → {local_ip}:5001")
print("Clientes deben conectar a la IP de tu máquina (o localhost si es local)")

# Bucle con daemon=True → evita Broken pipe
try:
    while True:
        client_socket, address = server.accept()
        thread = threading.Thread(
            target=handle_client,
            args=(client_socket, address),
            daemon=True                     # ¡¡CLAVE!!
        )
        thread.start()
except KeyboardInterrupt:
    print("\nServidor detenido.")