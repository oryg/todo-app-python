import os
import json

base_dir = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_dir, "data", "tareas.json")


def agregar_tarea(tareas, tarea):
    tareas.append({
        "nombre": tarea,
        "completada": False
    })
    
def cargar_tareas():
    try:
        with open(file_path, "r") as archivo:      
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_tareas(tareas):
    with open(file_path, "w") as archivo:
        json.dump(tareas, archivo, indent=4)

def eliminar_tarea(tareas, indice):
    if 0 <= indice < len(tareas):
        tareas.pop(indice)
        return True
    return False

def completar_tarea(tareas, indice):
    if 0 <= indice < len(tareas):
        tareas[indice]["completada"] = True
        return True
    return False