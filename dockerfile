# Imagen base de Python
FROM python:3.11-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar dependencias e instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el contenido de la carpeta containers
COPY . .

# Exponer el puerto de FastAPI
EXPOSE 8000

# Comando para levantar la app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
