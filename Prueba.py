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

"""# Programa de gestión de tareas con funciones globales, locales y no locales
tareas = []  # Variable global para la lista de tareas

def add_task(task):
    Agrega una nueva tarea a la lista global de tareas.
    tareas.append(task)
    print(f"Tarea '{task}' agregada.")

def remove_task(task):
    Elimina una tarea de la lista global de tareas, si existe.
    if task in tareas:
        tareas.remove(task)
        print(f"Tarea '{task}' eliminada.")
    else:
        print(f"La tarea '{task}' no existe.")

def list_tasks():
    Enumera todas las tareas almacenadas en la lista global de tareas.
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        print("Tareas pendientes:")
        for i, t in enumerate(tareas, 1):
            print(f"{i}. {t}")

def task_manager():
    Administra las operaciones de agregar, eliminar, listar y modificar tareas.
    def modify_task():
    Modifica la primera tarea en la lista de tareas (no local).
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
    task_manager()"""

# Programa de operaciones sobre una lista de cadenas con menú y funciones
def print_by_letter(strings):
    """Busca e imprime todas las cadenas que comienzan con una letra pedida al usuario."""
    letra = input("Introduce la letra inicial: ")
    print(f"Cadenas que comienzan con '{letra}':")
    for s in strings:
        if s.startswith(letra):
            print(s)

def count_substring(strings):
    """Cuenta e imprime cuántas cadenas contienen una subcadena pedida al usuario."""
    sub = input("Introduce la subcadena a buscar: ")
    count = sum(sub in s for s in strings)
    print(f"{count} cadenas contienen la subcadena '{sub}'")

def longest_and_shortest(strings):
    """Dice qué cadena es la más larga y cuál la más corta, junto con su longitud."""
    if not strings:
        print("La lista está vacía.")
        return
    longest = max(strings, key=len)
    shortest = min(strings, key=len)
    print(f"Cadena más larga: '{longest}' ({len(longest)} caracteres)")
    print(f"Cadena más corta: '{shortest}' ({len(shortest)} caracteres)")

def check_identity(strings):
    """Comprueba si dos cadenas son el mismo objeto en memoria usando 'is'."""
    if len(strings) < 2:
        print("No hay suficientes cadenas para comparar.")
        return
    i = int(input(f"Introduce el índice de la primera cadena (1-{len(strings)}): ")) - 1
    j = int(input(f"Introduce el índice de la segunda cadena (1-{len(strings)}): ")) - 1
    if 0 <= i < len(strings) and 0 <= j < len(strings):
        if strings[i] is strings[j]:
            print("Son el mismo objeto en memoria.")
        else:
            print("No son el mismo objeto en memoria.")
    else:
        print("Índices no válidos.")

def check_length_gt_10(strings):
    """Comprueba si alguna cadena tiene más de 10 caracteres."""
    for s in strings:
        if len(s) > 10:
            print(f"La cadena '{s}' tiene más de 10 caracteres.")
            break
    else:
        print("Ninguna cadena tiene más de 10 caracteres.")

def principal():
    """Funcion principal que maneja el menú y las operaciones sobre la lista de cadenas."""
    strings = []
    n = int(input("¿Cuántas cadenas quieres introducir?: "))
    for i in range(n):
        strings.append(input(f"Introduce la cadena {i+1}: "))

    menu = ("\nMenú de operaciones:\n"
            "1. Imprimir cadenas que comiencen con una letra\n"
            "2. Contar cadenas que contienen una subcadena\n"
            "3. Encontrar la cadena más larga y más corta\n"
            "4. Verificar si dos cadenas son el mismo objeto (is)\n"
            "5. Verificar si alguna cadena tiene más de 10 caracteres\n"
            "6. Salir")
    print(menu)
    while True:
        opcion = input("\nSelecciona una opción: ")
        match opcion:
            case '1':
                print_by_letter(strings)
            case '2':
                count_substring(strings)
            case '3':
                longest_and_shortest(strings)
            case '4':
                check_identity(strings)
            case '5':
                check_length_gt_10(strings)
            case '6':
                print("Saliendo del programa.")
                break
            case _ :
                print("Opción no válida.")
if __name__ == "__main__":
    principal()