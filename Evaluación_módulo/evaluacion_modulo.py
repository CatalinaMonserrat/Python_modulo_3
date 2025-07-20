#importar json para guardar y cargar tareas
import json

#Función para guardar tareas
def guardar_tareas():     
    with open("tareas.json", "w") as archivo:
        json.dump(tareas, archivo)

#Función para cargar tareas al iniciar
def cargar_tareas():
    try:
        with open("tareas.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

#Lista de tareas en blanco
tareas = cargar_tareas()

#Función para agregar tareas
def agregar_tarea():
    nombre = input("Escribe la tarea que deseas agregar: ")
    tarea = {"tarea": nombre, "estado": "pendiente"}
    tareas.append(tarea)
    guardar_tareas()
    print("Tarea agregada correctamente.")

#Función para ver tareas
def ver_tareas():
    for i, tarea in enumerate(tareas):
        print(f"{i + 1}. Tarea: {tarea['tarea']} - Estado: {tarea['estado']}")

#Función para tareas completadas
def marcar_completada_por_indice(indice):
    if 0 <= indice - 1 < len(tareas):
        tareas[indice - 1]["estado"] = "completada"
        guardar_tareas()
        print ("Tarea actualizada")
    else:
        print("Indice no valido")

#Función para eliminar tareas
def eliminar_por_indice(indice):
    if 1 <= indice <= len(tareas):
        tarea_eliminada = tareas.pop(indice - 1)
        guardar_tareas()
        print(f"Tarea '{tarea_eliminada['tarea']}' eliminada.")
    else:
        print("Indice no valido")

#Menu

while True:
    print("\n--- Gestor de Tareas ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")
    print()
    
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        ver_tareas()
    elif opcion == "3":
        ver_tareas()
        indice = int(input("Ingresa el indice de la tarea completada: "))
        marcar_completada_por_indice(indice)
    elif opcion == "4":
        ver_tareas()
        indice = int(input("Ingresa el indice de la tarea a eliminar: "))
        eliminar_por_indice(indice)
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no valida, por favor intente denuevo.")
