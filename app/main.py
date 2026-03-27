from tarea import cargar_tareas
from ui import completar_tarea_ui, eliminar_tarea_ui, agregar_tarea_ui, ver_tareas_ui
import os
def clean_console():
    os.system('cls' if os.name == 'nt' else 'clear')

tareas = cargar_tareas()

print(type(tareas))

while True:
    clean_console()
    print(" ------- MENU -------")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")

    opcion = input("Seleccione una opción: \n")
    clean_console()

    if opcion == "1":
        agregar_tarea_ui(tareas)

    elif opcion == "2":
        ver_tareas_ui(tareas)
    
    elif opcion == "3":
        completar_tarea_ui(tareas)
    
    elif opcion == "4":
        eliminar_tarea_ui(tareas)
   
    elif opcion == "5":
        print("Saliendo del programa...")
        break 

    else:
        print("Opción inválida, por favor seleccione una opción del menú.") 