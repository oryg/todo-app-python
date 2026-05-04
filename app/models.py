from pydantic import BaseModel, StrictStr
from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class Tarea(Base):
    __tablename__ = "tareas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    completada = Column(Boolean, default=False)
class EstadoTarea(BaseModel):
    completada: bool
class CrearTarea(BaseModel):
    nombre: StrictStr
class TareaSalida(BaseModel):
    id: int
    nombre: StrictStr
    completada: bool

    class Config:
        from_attributes = True
