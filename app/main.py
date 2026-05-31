from fastapi import FastAPI
import os

app = FastAPI(title="Microservicio DevOps - Python")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Evaluacion Parcial 2 - DevOps Activa"}

@app.get("/health")
def health_check():
    file_env = os.getenv("DATABASE_URL", "No configurada")
    return {
        "status": "healthy",
        "database_status": "connected" if "postgres" in file_env else "isolated"
    }
