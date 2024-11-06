import json
import random
from datetime import datetime

# Lista global de tareas
tareas = []

def add():
    dic = {}
    
    nombre = input("Ingrese nombre de la tarea: ")
    # Generar un ID
    id = random.randint(1, 1000)   
    
    # Asignar datos al diccionario
    dic["nombre"] = nombre
    dic["estado"] = "todo"  #inicio del estado
    dic["id"] = id
    dic["createdAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
    dic["updatedAt"] = dic["createdAt"]  


    
    # Agregar el diccionario a la lista de tareas
    tareas.append(dic)
    
    # Guardar la lista de tareas en un archivo JSON
    save_tasks()


def update():
    # Buscar la tarea por id
    id_input = input("ingrese id del usuario: ")
    found_tarea = False  
    
    for tarea in tareas:
        if tarea["id"] == int(id_input):
            found_tarea = True
            print(f"Tarea encontrada: {tarea['nombre']} - Estado: {tarea['estado']}")
            
            nuevo_estado = input("Ingrese el nuevo estado de la tarea (todo, in-progress, done): ")
            while nuevo_estado not in ["todo", "in-progress", "done"]:
                nuevo_estado = input("Estado inválido, por favor ingrese un estado válido ")
            tarea["estado"] = nuevo_estado  # Actualizando el estado
            tarea["updatedAt"] =   datetime.now().strftime("%Y-%m-%d %H:%M:%S") 

            break
        
    if not found_tarea:
        print("Tarea no encontrada")
        
        # Guardar los cambios en el archivo JSON
    if found_tarea:
        save_tasks()

            
def delete():
    # Buscar la tarea por id
    id_input = input("ingrese id del usuario: ")
    found_tarea = False
    
    for tarea in tareas:
        if tarea["id"] == int(id_input):
            found_tarea = True
            print(f"Tarea encontrada: {tarea['nombre']} - Estado: {tarea['estado']}")
            tareas.remove(tarea)
            print("Tarea eliminada")
            break
        
    if not found_tarea:
        print("Tarea no encontrada")
        
        # Guardar los cambios en el archivo JSON
    if found_tarea:
        save_tasks()
    
            
def list_tasks(estado = None):
    for tarea in tareas:
        print(f"id: {tarea['id']}, Nombre: {tarea['nombre']}, Estado: {tarea['estado']}, Creado: {tarea['createdAt']}, Última actualización: {tarea['updatedAt']}")

def mark_in_progress():
    id_input = input("Ingrese el id de la tarea para marcar como 'en progreso': ")
    for tarea in tareas:
        if tarea["id"] == int(id_input):
            tarea["estado"] = "en progreso"
            tarea["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("Tarea marcada como 'en progreso'")
            break
    else:
        print("Tarea no encontrada")

    save_tasks()

def mark_done():
    id_input = input("Ingrese el de de la tarea para marcar como 'completada': ")
    for tarea in tareas:
        if tarea["id"] == int(id_input):
            tarea["estado"] = "completada"
            tarea["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("Tarea marcada como 'completada'")
            break
    else:
        print("Tarea no encontrada")

    save_tasks()

# Carga la lista de tareas en un archivo JSON
def load_tasks():
    try:
        with open('tareas.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
    
# Guarda la lista de tareas en un archivo JSON
def save_tasks():
    with open('tareas.json', 'w') as archivo:
        json.dump(tareas, archivo)

def main():
    global tareas
    tareas = load_tasks()

    while True:
        print("\nOpciones:")
        print("1. Añadir tarea")
        print("2. Actualizar tarea")
        print("3. Eliminar tarea")
        print("4. Listar todas las tareas")
        print("5. Marcar tarea como en proceso")
        print("6. Marcar tarea como completada")
        print("7. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                add()
            elif opcion == 2:
                update()
            elif opcion == 3:
                delete()
            elif opcion == 4:
                list_tasks()
            elif opcion == 5:
                mark_in_progress()
            elif opcion == 6:
                mark_done()
            elif opcion == 7:
                break
            else:
                print("Numero invalido. Ingresa un numero valido\n")
        except ValueError:
            print("Entrada no valida. Ingresa un número.\n")
