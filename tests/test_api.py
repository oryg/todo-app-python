from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)

def test_get_tareas():
    response = client.get("/tareas")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_crear_tarea():
    response = client.post("/tareas/agg", json={"nombre": "Test tarea"})

    assert response.status_code == 200
    assert response.json()["mensaje"] == "Tarea agregada"

def test_actualizar_tarea():
    client.post("/tareas/agg", json= {"nombre": "Actualizar tarea"})

    tareas = client.get("/tareas").json()
    
    indice = len(tareas) - 1
    
    response = client.put(f"/tareas/act/{indice}", json={"completada": True})

    assert response.status_code == 200
    assert "actualizada" in response.json()["mensaje"]

def test_eliminar_tarea():
    client.post("/tareas/agg", json={"nombre": "Eliminar tarea"})

    tareas= client.get("/tareas").json()
    last_id = tareas[-1]["id"]

    response = client.delete(f"/tareas/del/{last_id}")

    assert response.status_code == 200
    assert "eliminada" in response.json()["mensaje"]