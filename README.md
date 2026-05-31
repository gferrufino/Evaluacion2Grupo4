# Evaluacion2Grupo4

# Evaluación Parcial 2 - Ingeniería DevOps

Este proyecto consiste en un microservicio contenerizado construido con **FastAPI (Python)** y orquestado junto a una base de datos **PostgreSQL**, automatizado completamente mediante un pipeline de CI/CD en **GitHub Actions**.

## Estructura de la Solución

* `/app`: Código fuente del microservicio y pruebas unitarias (`pytest`).
* `Dockerfile`: Configuración de contenerización optimizada mediante *Multi-stage builds*.
* `docker-compose.yml`: Orquestación multicapa de servicios con políticas de *Healthcheck*.
* `.github/workflows/ci-cd.yml`: Pipeline automatizado de Integración y Despliegue Continuo.
* `.snyk`: Archivo de gobernanza y gestión de políticas de seguridad.

---

## 📈 Garantía de Calidad y Trazabilidad (IE4)

### 1. Calidad del Código y Pruebas (IE2)
La calidad del entregable se asegura de manera automatizada en el Job `unit-tests`. Cada cambio en el código fuente debe pasar obligatoriamente por pruebas unitarias automatizadas ejecutadas con  `pytest`. Si un cambio rompe los endpoints básicos el pipeline se detiene de inmediato.

### 2. Gobernanza y Seguridad (IE3)
Se implementa un **Quality Gate** utilizando **Snyk** (`--severity-threshold=high`). Ante vulnerabilidades críticas de dependencias, el pipeline bloquea el flujo de entrega.

### 3. Trazabilidad Absoluta
La trazabilidad se garantiza mediante el etiquetado dinámico de las imágenes Docker utilizando el identificador único del commit de Git:
```bash