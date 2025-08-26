# PoC Microservicio FastAPI Dockerizado

## Descripción

Esta es una **prueba de concepto (PoC)** de un microservicio desarrollado en **FastAPI**, dockerizado y desplegado en la nube. El objetivo es demostrar habilidades en:

- Desarrollo de APIs con FastAPI.
- Contenerización con Docker.
- Deploy en la nube usando **Render**.
- Integración con **CI/CD** mediante GitHub Actions (opcional).

El microservicio expone un endpoint simple que devuelve un mensaje de prueba.

---

## Tecnologías utilizadas

- **Python 3**
- **FastAPI**
- **Uvicorn**
- **Docker**
- **Render** (hosting de la aplicación)
- **GitHub** (control de versiones)

---

## Estructura del proyecto

container/
├─ app.py # Microservicio FastAPI
├─ requirements.txt # Dependencias de Python
├─ Dockerfile # Dockerfile para contenerización
└─ .github/workflows/ # Pipeline CI/CD opcional
