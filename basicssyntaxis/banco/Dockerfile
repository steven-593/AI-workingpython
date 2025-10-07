# Usar Python 3.10 slim
FROM python:3.10-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el proyecto completo
COPY . .

# Instalar dependencias si tienes requirements.txt
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# Comando por defecto para ejecutar tu script
CMD ["python", "banco.py"]

