from fastapi import FastAPI # type: ignore
from pydantic import BaseModel # type: ignore

app = FastAPI()

# Endpoint raíz
@app.get("/")
def read_root():
    return {"mensaje": "Hello World – a Dockerized FastAPI microservice with a Python 3 backend."}

# Endpoint dinámico con path parameter
@app.get("/Hi/{nombre}")
def saludo(nombre: str):
    return {"mensaje": f"Hola, {nombre}! Welcome to my microservice."}

# Endpoint con query parameters opcionales
@app.get("/info")
def info(nombre: str = "Mariano", edad: int = 45):
    return {"name": nombre, "Age": edad, "message": f"Hi {nombre}, you are {edad} years old"}

# Modelo Pydantic para POST
class Mensaje(BaseModel):
    texto: str

# Endpoint POST para procesar texto
@app.post("/convert")
def procesar(mensaje: Mensaje):
    return {
        "original": mensaje.texto,
        "mayusculas": mensaje.texto.upper()
    }
