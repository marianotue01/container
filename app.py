from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Endpoint raíz
@app.get("/")
def read_root():
    return {"mensaje": "Hola mundo desde el microservicio Dockerizado"}

# Endpoint dinámico con path parameter
@app.get("/saludo/{nombre}")
def saludo(nombre: str):
    return {"mensaje": f"Hola, {nombre}! Bienvenido a mi microservicio."}

# Endpoint con query parameters opcionales
@app.get("/info")
def info(nombre: str = "Mariano", edad: int = 45):
    return {"nombre": nombre, "edad": edad, "mensaje": f"Hola {nombre}, tenés {edad} años"}

# Modelo Pydantic para POST
class Mensaje(BaseModel):
    texto: str

# Endpoint POST para procesar texto
@app.post("/procesar")
def procesar(mensaje: Mensaje):
    return {
        "original": mensaje.texto,
        "mayusculas": mensaje.texto.upper()
    }
