from pydantic import BaseModel, StrictStr

class EstadoTarea(BaseModel):
    completada: bool

class Tarea(BaseModel):
    nombre: StrictStr

class TareaSalida(BaseModel):
    id: int
    nombre: StrictStr
    completada: bool

