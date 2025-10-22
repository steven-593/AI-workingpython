# Imagen base de Python
FROM python:3.12-slim

# Evitar preguntas interactivas al instalar paquetes
ENV DEBIAN_FRONTEND=noninteractive

# Crear carpeta de trabajo
WORKDIR /app

# Copiar archivo del servidor
COPY server.py .

# Instalar dependencias si tuvieras
# RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto que usará el servidor
EXPOSE 5000

# Comando para ejecutar el servidor
CMD ["python3", "server.py"]
