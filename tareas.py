tareas = []

def agregar_tarea(tarea):
    tareas.append({"tarea": tarea, "completada": False})

def mostrar_tareas():
    for i, tarea in enumerate(tareas, 1):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        print(f"{i}. {tarea['tarea']} - {estado}")

def completar_tarea(numero_tarea):
    if 0 < numero_tarea <= len(tareas):
        tareas[numero_tarea - 1]["completada"] = True

def eliminar_tarea(tarea):
    for i, t in enumerate(tareas):
        if t["tarea"] == tarea:
            tareas.pop(i)
            print(f"La tarea {tarea} se ha eliminado")
        else:
            print(f"no se encontro la tarea {tarea}")
    
    #if tarea in tareas:
    #    indice=tareas.index(tarea)
    ##    tareas.pop(indice)
    #    print(f"La tarea {tarea} se ha eliminado")
    #else:
    #    print("no se encontro la tarea")

# Ejemplo de uso
while True:
    print("\n1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        tarea = input("Escribe la tarea: ")
        agregar_tarea(tarea)
    elif opcion == "2":
        mostrar_tareas()
    elif opcion == "3":
        mostrar_tareas()
        numero_tarea = int(input("Número de tarea a completar: "))
        completar_tarea(numero_tarea)
    elif opcion == "4":
        tarea=input("Escribe la tarea a eliminar: ")
        eliminar_tarea(tarea)
    elif opcion == "5":
        break
    else:
        print("Opción no válida.")