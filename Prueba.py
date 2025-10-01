"""def oper_lista():
    Esta función realiza varias operaciones con una lista de números:
    - Calcula la suma de todos los números.
    - Calcula la suma de numeros positivos y negativos por separado.
    - Encuentra el numero máximo y minimo de la lista.
    - Revisa que todos los numeros de la lista sean únicos.
    - Te indica si la lista tiene más numeros posistivos o negativos.
    
    lista = [3, -5, 2, -8, 6, -3, 2, 9, -1, 4, -7, 5]

    def menu_operaciones():
        print("\nMenú de operaciones:")
        print("1. Suma total de la lista")
        print("2. Suma de números positivos y negativos por separado")
        print("3. Número máximo y mínimo de la lista")
        print("4. Verificar si todos los números son únicos")
        print("5. Comparar cantidad de números positivos y negativos")
        print("6. Salir")

    menu_operaciones()  # Imprime el menú solo una vez
    while True:
        opcion = input("\nSeleccione la operación a realizar: ")

        match opcion:
            case '1':
                print(f"\nSuma total de la lista: {sum(lista)}")
            case '2':
                suma_positivos = sum(x for x in lista if x > 0)
                suma_negativos = sum(x for x in lista if x < 0)
                print(f"\nSuma de números positivos: {suma_positivos}")
                print(f"Suma de números negativos: {suma_negativos}")
            case '3':
                print(f"\nNúmero máximo de la lista: {max(lista)}")
                print(f"Número mínimo de la lista: {min(lista)}")
            case '4':
                if len(lista) == len(set(lista)):
                    print("\nTodos los números son únicos.")
                else:
                    print("\nHay números repetidos en la lista.")
            case '5':
                positivos = sum(1 for x in lista if x > 0)
                negativos = sum(1 for x in lista if x < 0)
                if positivos > negativos:
                    print("\nHay más números positivos que negativos.")
                elif negativos > positivos:
                    print("\nHay más números negativos que positivos.")
                else:
                    print("\nHay igual cantidad de números positivos y negativos.")
            case '6':
                print("\nSaliendo del menú.")
                break
            case _:
                print("\nOpción no válida. Intente de nuevo.")
oper_lista()"""

# Programa de gestión de tareas con funciones globales, locales y no locales
tareas = []  # Variable global para la lista de tareas

def add_task(task):
    """Agrega una nueva tarea a la lista global de tareas."""
    tareas.append(task)
    print(f"Tarea '{task}' agregada.")

def remove_task(task):
    """Elimina una tarea de la lista global de tareas, si existe."""
    if task in tareas:
        tareas.remove(task)
        print(f"Tarea '{task}' eliminada.")
    else:
        print(f"La tarea '{task}' no existe.")

def list_tasks():
    """Enumera todas las tareas almacenadas en la lista global de tareas."""
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        print("Tareas pendientes:")
        for i, t in enumerate(tareas, 1):
            print(f"{i}. {t}")

def task_manager():
    """Administra las operaciones de agregar, eliminar, listar y modificar tareas."""
    def modify_task():
        """Modifica la primera tarea en la lista de tareas (no local)."""
        if tareas:
            print(f"Tarea actual: {tareas[0]}")
            nueva = input("Ingrese el nuevo valor para la primera tarea: ")
            tareas[0] = nueva
            print("Primera tarea modificada.")
        else:
            print("No hay tareas para modificar.")

    while True:
        print("\n--- MENÚ DE TAREAS ---")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Mostrar lista de tareas")
        print("4. Modificar primera tarea")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            task = input("Ingrese la nueva tarea: ")
            add_task(task)
        elif opcion == '2':
            task = input("Ingrese la tarea a eliminar: ")
            remove_task(task)
        elif opcion == '3':
            list_tasks()
        elif opcion == '4':
            modify_task()
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")
if __name__ == "__main__":
    task_manager()