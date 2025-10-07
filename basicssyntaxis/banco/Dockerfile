# Imagen base con Python
FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY banco.py /app/

# (Opcional) Si tienes dependencias, descomenta estas líneas:
# COPY requirements.txt /app/
# RUN pip install --no-cache-dir -r requirements.txt

# Comando por defecto al ejecutar el contenedor
CMD ["python", "banco.py"]
