from fastapi import FastAPI
from pydantic import BaseModel, StrictStr
from app import tarea
from app.tarea import cargar_tareas, agregar_tarea, eliminar_tarea, completar_tarea, guardar_tareas

class EstadoTarea(BaseModel):
    completada: bool

class Tarea(BaseModel):
    nombre: StrictStr
app = FastAPI()

#Home page
@app.get("/")
def home():
    return {"mensaje": "Bienvenido a la API de tareas"}

# Obtener todas las tareas
@app.get("/tareas")
def obtener_tareas():
    tareas = cargar_tareas()
    resultado= []
    for i, tarea in enumerate(tareas):       
        #Caso 1: tarea es un dict
        if isinstance(tarea,dict):
            nombre = tarea.get("nombre", "")
            completada = tarea.get("completada", False)
        #Caso 2: string con "(completada)"
        elif isinstance(tarea, str):
            completada = "(completada)" in tarea
            nombre = tarea.replace(" (completada)", "")
            if nombre.startswith("{"):
                try:
                    import ast 
                    data = ast.literal_eval(tarea)
                    nombre = data.get("nombre", nombre)
                    completada = data.get("completada", completada)
                except:
                    pass
            else:
                nombre = str(tarea)
                completada = False
        resultado.append({
            "id": i,
            "nombre": nombre,
            "completada": completada
        })
    return resultado

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
def actualizar_tarea(indice: int):
    tareas = cargar_tareas()

    if 0 <= indice < len(tareas):
        tareas[indice]["completada"] = True
        guardar_tareas(tareas)

        return {"mensaje": "Tarea actualizada"}
    
    return {"error": "Índice inválido"}


