from tarea import agregar_tarea, guardar_tareas, eliminar_tarea, completar_tarea

import os
def clean_console():
    os.system('cls' if os.name == 'nt' else 'clear')
              

def agregar_tarea_ui(tareas):
    tarea = input("Ingrese la tarea: \n")
    agregar_tarea(tareas, tarea)
    guardar_tareas(tareas)


def eliminar_tarea_ui(tareas):
    if not tareas:
        print("\n No hay tareas para eliminar.")
        input("\n Presione Enter para continuar...")
        return
    
    for i, tarea in enumerate(tareas):
        estado = "✓" if tarea["completada"] else "✗"
        print(f"{i}. {tarea['nombre']} [{estado}]")
        
    try:
        indice = int(input("\n Ingrese el índice de la tarea a eliminar: "))

        if 0 <= indice < len(tareas):

            while True:
                clean_console()
                print(f"\n Seguro de eliminar la tarea: {tareas[indice]['nombre']} ?")
                confirmacion = input("\n Escriba 'y' para confirmar o 'n' para cancelar: ").lower()
                clean_console()

                if confirmacion == "y":
                    eliminar_tarea(tareas, indice)
                    guardar_tareas(tareas)
                    print("\n Tarea eliminada.")
                    input("\n Presione Enter para continuar...")
                    break

                elif confirmacion == "n":
                    print("\n Eliminación cancelada.")
                    input("\n Presione Enter para continuar...")
                    break

                else:
                    print("\n Por favor, ingrese 'y' o 'n'.")

        else:
            print("\n Índice inválido.")
            input("\n Presione Enter para continuar...")

    except ValueError:
        print("\n Debes ingresar un número.")
        input("\n Presione Enter para continuar...")

        
def ver_tareas_ui(tareas):
    print (" ----- TAREAS PENDIENTES -----")
    if not tareas:
        print("\n No hay tareas pendientes.")
        input("\n Presione Enter para continuar...")
    else:
        for i, tarea in enumerate(tareas, start=1):
            estado = "✓" if tarea["completada"] else "✗"
            print(f"{i}. [{estado}] {tarea['nombre']}")
        input("\n Presione Enter para continuar...")

def completar_tarea_ui(tareas):
    if not tareas:
        print ("\n No hay tareas para completar.")
        input("\n Presione Enter para continuar...")
        return
    for i, tarea in enumerate (tareas, start=1):
        estado = "✓" if tarea["completada"] else "✗"
        print(f"{i}. [{estado}] {tarea['nombre']}")
    try:
        indice = int(input("\n Ingrese el número de la tarea completada:")) -1
        if completar_tarea(tareas, indice):
            guardar_tareas(tareas)
            print("\n Tarea marcada como completada.")
        else:
            print("\n Número de tarea inválido.")
    except ValueError:
        print("\n Debes ingresar un número.")
        input("\n Presione Enter para continuar...")
        return

    input("\n Presione Enter para continuar...")    
    
