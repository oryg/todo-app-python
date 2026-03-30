from fastapi import FastAPI
from app.tarea import cargar_tareas, agregar_tarea, eliminar_tarea, completar_tarea, guardar_tareas

app = FastAPI()

#Home page
@app.get("/")
def home():
    return {"mensaje": "Bienvenido a la API de tareas"}

# Obtener todas las tareas
@app.get("/tareas")
def obtener_tareas():
    return cargar_tareas()

# Agregar tarea
@app.post("/tareas")
def crear_tarea(nombre: str):
    tareas = cargar_tareas()
    agregar_tarea(tareas, nombre)
    guardar_tareas(tareas)
    return {"mensaje": "Tarea agregada"}

# Eliminar tarea
@app.delete("/tareas/{indice}")
def borrar_tarea(indice: int):
    tareas = cargar_tareas()
    if eliminar_tarea(tareas, indice):
        guardar_tareas(tareas)
        return {"mensaje": "Tarea eliminada"}
    return {"error": "Índice inválido"}

# Completar tarea
@app.put("/tareas/{indice}")
def completar(indice: int):
    tareas = cargar_tareas()
    if completar_tarea(tareas, indice):
        guardar_tareas(tareas)
        return {"mensaje": "Tarea completada"}
    return {"error": "Índice inválido"}