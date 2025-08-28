from fastapi import FastAPI  # FastAPI web framewor`k
from pydantic import BaseModel  # For request data validation

app = FastAPI()  # Create FastAPI instance

# ----------------------------
# Root endpoint
# ----------------------------
# Responds to GET / with a simple welcome message
@app.get("/")
def read_root():
    return {"mensaje": "Hello World – a Dockerized FastAPI microservice with a Python 3 backend."}

# ----------------------------
# Dynamic greeting endpoint
# ----------------------------
# Responds to GET /Hi/{nombre} with a personalized message
@app.get("/Hi/{nombre}")
def saludo(nombre: str):
    return {"mensaje": f"Hola, {nombre}! Welcome to my microservice."}

# ----------------------------
# Endpoint with optional query parameters
# ----------------------------
# GET /info?nombre=Name&edad=Age
@app.get("/info")
def info(nombre: str = "Mariano", edad: int = 45):
    return {"name": nombre, "Age": edad, "message": f"Hi {nombre}, you are {edad} years old"}

# ----------------------------
# POST endpoint to process text
# ----------------------------
# Receives JSON like {"texto": "some text"} and returns uppercase version
class Mensaje(BaseModel):
    texto: str

@app.post("/convert")
def procesar(mensaje: Mensaje):
    return {
        "original": mensaje.texto,
        "mayusculas": mensaje.texto.upper()
    }