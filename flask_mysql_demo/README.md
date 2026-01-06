# 1. Instalar MySQL y crear la base de datos
mysql -u root -p < setup_mysql.sql

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Configurar .env con tus credenciales

# 4. Ejecutar servidor
python app.py

# 5. Probar cliente (en otra terminal)
python client_example.py