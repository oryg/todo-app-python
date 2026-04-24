# Imagen base
FROM python:3.11-slim

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivos
COPY . .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer puerto
EXPOSE 8000

# Comando para ejecutar la app
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]