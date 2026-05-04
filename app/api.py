from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Tarea 
from app.tarea import cargar_tareas, agregar_tarea, eliminar_tarea, guardar_tareas
from app.models import Tarea, EstadoTarea, TareaSalida, CrearTarea
from app.database import engine
from app.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

#Home page
@app.get("/")
def home():
    return {"mensaje": "Bienvenido a la API de tareas"}

# Obtener todas las tareas
@app.get("/tareas", response_model=list[TareaSalida])
def obtener_tareas(db: Session = Depends(get_db)):
    tareas = db.query(Tarea).all()
    return tareas

# Agregar tarea
@app.post("/tareas/agg")
def crear_tarea(tarea: CrearTarea, db: Session = Depends(get_db)):
    nueva_tarea = Tarea(nombre=tarea.nombre)
    db.add(nueva_tarea)
    db.commit()
    db.refresh(nueva_tarea)
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


