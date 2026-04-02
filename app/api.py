from fastapi import FastAPI
from app import tarea
from app.tarea import cargar_tareas, agregar_tarea, eliminar_tarea, completar_tarea, guardar_tareas
from app.models import Tarea, EstadoTarea, TareaSalida

app = FastAPI()

#Home page
@app.get("/")
def home():
    return {"mensaje": "Bienvenido a la API de tareas"}

# Obtener todas las tareas
@app.get("/tareas", response_model=list[TareaSalida])
def obtener_tareas():
    tareas = cargar_tareas()
    
    return [
        {
            "id": i,
            "nombre": tarea["nombre"],
            "completada": tarea["completada"]
        }
        for i, tarea in enumerate(tareas)
    ]

# Agregar tarea
@app.post("/tareas/agg")
def crear_tarea(tarea: Tarea):
    tareas = cargar_tareas()
    agregar_tarea(tareas, tarea.nombre)
    guardar_tareas(tareas)
    return {"mensaje": "Tarea agregada"}

# Eliminar tarea
@app.delete("/tareas/del/{indice}")
def borrar_tarea(indice: int):
    tareas = cargar_tareas()

    if 0<= indice < len(tareas):
        tarea = tareas[indice]

        estado="completada" if tarea["completada"] else "sin completar"

        eliminar_tarea(tareas, indice)
        guardar_tareas(tareas)

        return {
            "mensaje": f"Tarea '{tarea['nombre']} ({estado})' eliminada"
        }
    return {"error": "Índice inválido"}

# Completar tarea
@app.put("/tareas/act/{indice}")
def actualizar_tarea(indice: int, estado: EstadoTarea):
    tareas = cargar_tareas()

    if 0 <= indice < len(tareas):
        tareas[indice]["completada"] = estado.completada
        guardar_tareas(tareas)

        return {"mensaje": "Tarea actualizada"}
    
    return {"error": "Índice inválido"}


