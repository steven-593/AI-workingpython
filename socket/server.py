import socket
import threading

def get_local_ip():
    """Obtiene la IP local de la máquina."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("172.18.0.1", 80))  # Conecta a un servidor externo para obtener la IP local
        return s.getsockname()[0]
    except Exception:
        return "No se pudo obtener la IP (usa ipconfig/ifconfig manualmente)"

def handle_client(client_socket, address):
    """Maneja las solicitudes de un cliente en un hilo separado."""
    print(f"Cliente conectado: {address}")
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8').strip()
            if not data or data == "quit":
                break
            num1, num2, operation = data.split(',')
            num1, num2 = float(num1), float(num2)
            if operation == "add":
                result = num1 + num2
                response = f"RESULT:{result}"
            elif operation == "sub":
                result = num1 - num2
                response = f"RESULT:{result}"
            elif operation == "mul":
                result = num1 * num2
                response = f"RESULT:{result}"
            elif operation == "div":
                if num2 == 0:
                    response = "ERROR:División por cero"
                else:
                    result = num1 / num2
                    response = f"RESULT:{result}"
            else:
                response = "ERROR:Operación no válida"
        except (ValueError, IndexError):
            response = "ERROR:Formato de solicitud incorrecto"
        client_socket.send(response.encode('utf-8'))
    print(f"Cliente desconectado: {address}")
    client_socket.close()

# Configuración del servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 5000))  # Escucha en todas las interfaces
server.listen(5)
local_ip = get_local_ip()
print(f"Servidor escuchando en {local_ip}:5000 (comparte esta IP con los clientes)")

# Bucle principal para aceptar conexiones
while True:
    client_socket, address = server.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
    client_thread.start()