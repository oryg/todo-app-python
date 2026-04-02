## Task Manager API (FastAPI)

API REST desarrollada con FastAPI para la gestión de tareas, implementando operaciones CRUD completas, validación de datos y una estructura modular escalable.

---

## Tecnologías utilizadas

* Python 3
* FastAPI
* Pydantic
* Uvicorn
* JSON (persistencia simple)

---

## Funcionalidades

* Crear tareas
* Listar tareas con identificador único
* Marcar tareas como completadas
* Eliminar tareas
* Validación de datos con Pydantic
* Respuestas estructuradas mediante `response_model`

---

## Estructura del proyecto

```text
todo_list/
│
├── app/
│   ├── __init__.py
│   ├── api.py
│   ├── main.py
│   ├── models.py
│   ├── tarea.py
│   ├── ui.py
│
├── data/
│   ├── tareas.json
│   ├── .gitkeep
│
├── .gitignore
├── README.md
├── requirements.txt
```

---

## Instalación y ejecución

1. Clonar el repositorio:

```bash
git clone https://github.com/oryg/todo-app-python.git
cd todo-app-python
```

2. Crear entorno virtual:

```bash
python -m venv venv
```

3. Activar entorno:

Windows:

```bash
venv\Scripts\activate
```

4. Instalar dependencias:

```bash
pip install -r requirements.txt
```

5. Ejecutar servidor:

```bash
uvicorn app.api:app --reload
```

---

## Endpoints principales

| Método | Endpoint                    | Descripción                |
| ------ | --------------------------- | -------------------------- |
| GET    | /tareas                     | Obtener todas las tareas   |
| POST   | /tareas/agg                 | Crear nueva tarea          |
| PUT    | /tareas/act/{indice}        | Actualizar estado de tarea |
| DELETE | /tareas/del/{indice}        | Eliminar tarea             |

---

## Documentación interactiva

Disponible en:

```text
http://127.0.0.1:8000/docs
```

---

## Posibles mejoras

* Integración con base de datos (PostgreSQL / MongoDB)
* Implementación de autenticación
* Tests automatizados con pytest
* Dockerización del proyecto
* Deploy en la nube

---

## Autor

Orlando Yanes
GitHub: https://github.com/oryg
