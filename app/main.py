from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI(title="Microservicio DevOps - Python")

@app.get("/", response_class=HTMLResponse)
def read_root():
    file_env = os.getenv("DATABASE_URL", "No configurada")
    db_status = "CONECTADA" if "postgres" in file_env else "AISLADA"
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>DevOps - Hola Mundo v2</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .card {{
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                padding: 3rem;
                border-radius: 16px;
                box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
                text-align: center;
                border: 1px solid rgba(255, 255, 255, 0.2);
                max-width: 500px;
            }}
            h1 {{
                font-size: 3rem;
                margin-bottom: 0.5rem;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
            }}
            p {{
                font-size: 1.2rem;
                opacity: 0.9;
            }}
            .badge {{
                display: inline-block;
                background: rgba(0, 0, 0, 0.4);
                padding: 0.5rem 1rem;
                border-radius: 50px;
                font-weight: bold;
                font-size: 0.9rem;
                margin-top: 1rem;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Hola Mundo</h1>
            <p>Evaluacion Parcial 2 - Ingenieria DevOps</p>
            <hr style="border: 0; border-top: 1px solid rgba(255,255,255,0.2); margin: 1.5rem 0;">
            <p>Estado de la Infraestructura:</p>
            <div class="badge">Base de Datos: {db_status}</div>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/health")
def health_check():
    file_env = os.getenv("DATABASE_URL", "No configurada")
    return {
        "status": "healthy",
        "database_status": "connected" if "postgres" in file_env else "isolated"
    }
