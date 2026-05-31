# Etapa 1: Constructor
FROM python:3.11-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Instalamos las dependencias en un directorio global del sistema
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Etapa 2: Imagen Final de Producción
FROM python:3.11-slim

WORKDIR /app

# Copiamos las dependencias instaladas desde la etapa anterior
COPY --from=builder /install /usr/local

# Copiamos el código de la aplicación
COPY ./app ./app

# Configuración de seguridad: Usuario sin privilegios
RUN useradd -u 1000 -m devopsuser && chown -R devopsuser:devopsuser /app
USER 1000

EXPOSE 8000

# Comando de ejecución usando la ruta global limpia
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
