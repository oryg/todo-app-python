from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Tarea 
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
@app.delete("/tareas/del/{id}")
def borrar_tarea(id: int, db: Session = Depends(get_db)):
    tarea = db.query(Tarea).filter(Tarea.id == id).first()

    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    db.delete(tarea)
    db.commit()

    return {"mensaje":"Tarea Eliminada"}

# Completar tarea
@app.put("/tareas/act/{id}")
def actualizar_tarea(id: int, estado: EstadoTarea, db: Sesion = Depends(get_db)):
    tarea = db.query(Tarea).filter(Tarea.id == id).first()

    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    
    tarea.completada = estado.completada
    db.commit()
    db.refresh(tarea)

    return {"mensaje": "Tarea actualizada"}


