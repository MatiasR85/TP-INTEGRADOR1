# Librerias
import random
import time

# Algoritmo de Ordenamientos
# 1. Ordenamiento burbuja (Bubble Sort)
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# 2. Ordenamiento Rápido (Quicksort). Para Listas grandes
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0]
        less = [x for x in lista[1:] if x <= pivot]
        greater = [x for x in lista[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    
# Algoritmos de Búsqueda
# 1. Búsqueda Lineal
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

# 2.1 Búsqueda Binaria
def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# 2.2 Búsqueda Binaria Recursiva
def busqueda_binaria_recursiva(lista, objetivo, izquierda, derecha):
    if izquierda > derecha:
        return -1
    medio = (izquierda + derecha) // 2
    if lista[medio] == objetivo:
        return medio
    elif lista[medio] < objetivo:
        return busqueda_binaria_recursiva(lista, objetivo, medio + 1, derecha)
    else:
        return busqueda_binaria_recursiva(lista, objetivo, izquierda, medio - 1)




# Inicio del programa
print("- Alumnos de Tecnicatura Universitaria en Programación")
op = input("Ingrese su opción (1: Legajos Alumnos Programacion I, 2: Legajos Alumnos Tecnicatura, 3: Legajos Alumnos Universidad): ")

if op == "1":
    # Generación de legajos únicos y eleccion de un objetivo
    legajos = random.sample(range(100, 10000), 200)         # Genera 200 legajos únicos entre 100 y 9999
    
    

    bubble_sort(legajos)                                    # Aplica el ordenamiento burbuja

    # Eleccion de legajos a buscar
    buscar_legajo = [
        random.choice(legajos),         # Elige un elemento al azar
        legajos[-1],                    # Elige un elemento al final de la lista
        legajos[0],                     # Elige un elemento al inicio de la lista
        legajos[len(legajos) // 2],     # Elige un elemento en el medio de la lista
        max(legajos) + 1                # Agrega un legajo que no está en la lista para probar la búsqueda fallida
    ]

    for i in range(len(buscar_legajo)):
        print(f"* Legajos a buscar: {buscar_legajo[i]}")                # Imprime los legajos generados
        # Busqueda Lineal
        t0 = time.perf_counter()                                   # Inicia el cronómetro
        resultado_lineal = busqueda_lineal(legajos, buscar_legajo[i])
        t1 = time.perf_counter()                                   # Detiene el cronómetro
        tiempo_lineal = t1 - t0
        print(f"- Búsqueda Lineal → índice: {resultado_lineal}, tiempo: {tiempo_lineal:.8f} s")

        # Búsqueda Binaria
        t0 = time.perf_counter()                                # Inicia el cronómetro
        resultado_binaria = busqueda_binaria(legajos, buscar_legajo[i])
        t1 = time.perf_counter()                                # Detiene el cronómetro
        tiempo_binaria = t1 - t0
        print(f"- Búsqueda Binaria → índice: {resultado_binaria}, tiempo: {tiempo_binaria:.8f} s")

        # Búsqueda Binaria Recursiva
        t0 = time.perf_counter()                                # Inicia el cronómetro
        resultado_binaria_recursiva = busqueda_binaria_recursiva(legajos, buscar_legajo[i], 0, len(legajos) - 1)
        t1 = time.perf_counter()                                # Detiene el cronómetro
        tiempo_binaria_recursiva = t1 - t0
        print(f"- Búsqueda Binaria Recursiva → índice: {resultado_binaria_recursiva}, tiempo: {tiempo_binaria_recursiva:.8f} s \n")
    
elif op == "2":
    # Generación de legajos únicos y eleccion de un objetivo
    legajos = random.sample(range(100, 100000), 20000)       # Genera 20000 legajos únicos entre 100 y 99999
    
    #Ordenamiento Rápido
    t0 = time.perf_counter()                                 # Inicia el cronómetro  
    legajos= quicksort(legajos)                                      
    t1 = time.perf_counter()                                 # Detiene el cronómetro     
    tiempo_quicksort = t1 - t0
    print(f"Tiempo de ordenamiento rápido: {tiempo_quicksort:.8f} s")

    # Eleccion de legajos a buscar
    buscar_legajo = [
        random.choice(legajos),         # Elige un elemento al azar
        legajos[-1],                    # Elige un elemento al final de la lista
        legajos[0],                     # Elige un elemento al inicio de la lista
        legajos[len(legajos) // 2],     # Elige un elemento en el medio de la lista
        max(legajos) + 1                # Agrega un legajo que no está en la lista para probar la búsqueda fallida
    ]
    
    for i in range(len(buscar_legajo)):
        print(f"* Legajos a buscar: {buscar_legajo[i]}")                # Imprime los legajos generados
        # Busqueda Lineal
        t0 = time.perf_counter()                                   # Inicia el cronómetro
        resultado_lineal = busqueda_lineal(legajos, buscar_legajo[i])
        t1 = time.perf_counter()                                   # Detiene el cronómetro
        tiempo_lineal = t1 - t0
        print(f"- Búsqueda Lineal → índice: {resultado_lineal}, tiempo: {tiempo_lineal:.8f} s")

        # Búsqueda Binaria
        t0 = time.perf_counter()                                # Inicia el cronómetro
        resultado_binaria = busqueda_binaria(legajos, buscar_legajo[i])
        t1 = time.perf_counter()                                # Detiene el cronómetro
        tiempo_binaria = t1 - t0
        print(f"- Búsqueda Binaria → índice: {resultado_binaria}, tiempo: {tiempo_binaria:.8f} s")

        # Búsqueda Binaria Recursiva
        t0 = time.perf_counter()                                # Inicia el cronómetro
        resultado_binaria_recursiva = busqueda_binaria_recursiva(legajos, buscar_legajo[i], 0, len(legajos) - 1)
        t1 = time.perf_counter()                                # Detiene el cronómetro
        tiempo_binaria_recursiva = t1 - t0
        print(f"- Búsqueda Binaria Recursiva → índice: {resultado_binaria_recursiva}, tiempo: {tiempo_binaria_recursiva:.8f} s \n")

elif op == "3":
    # Generación de legajos únicos 200000 legajos únicos entre 100 y 499999 
    legajos = random.sample(range(100, 500000), 200000)            

    
    #Ordenamiento Rápido
    t0 = time.perf_counter()                                 # Inicia el cronómetro  
    legajos= quicksort(legajos)                                      
    t1 = time.perf_counter()                                 # Detiene el cronómetro     
    tiempo_quicksort = t1 - t0
    print(f"Tiempo de ordenamiento rápido: {tiempo_quicksort:.8f} s")

    # Eleccion de un legajo
    buscar_legajo = [
        random.choice(legajos),         # Elige un elemento al azar
        legajos[-1],                    # Elige un elemento al final de la lista
        legajos[0],                     # Elige un elemento al inicio de la lista
        legajos[len(legajos) // 2],     # Elige un elemento en el medio de la lista
        max(legajos) + 1                # Agrega un legajo que no está en la lista para probar la búsqueda fallida
    ]

    for i in range(len(buscar_legajo)):
        print(f"* Legajos a buscar: {buscar_legajo[i]}")                # Imprime los legajos generados
        # Busqueda Lineal
        t0 = time.perf_counter()                                   # Inicia el cronómetro
        resultado_lineal = busqueda_lineal(legajos, buscar_legajo[i])
        t1 = time.perf_counter()                                   # Detiene el cronómetro
        tiempo_lineal = t1 - t0
        print(f"- Búsqueda Lineal → índice: {resultado_lineal}, tiempo: {tiempo_lineal:.8f} s")

        # Búsqueda Binaria
        t0 = time.perf_counter()                                # Inicia el cronómetro
        resultado_binaria = busqueda_binaria(legajos, buscar_legajo[i])
        t1 = time.perf_counter()                                # Detiene el cronómetro
        tiempo_binaria = t1 - t0
        print(f"- Búsqueda Binaria → índice: {resultado_binaria}, tiempo: {tiempo_binaria:.8f} s")

        # Búsqueda Binaria Recursiva
        t0 = time.perf_counter()                                # Inicia el cronómetro
        resultado_binaria_recursiva = busqueda_binaria_recursiva(legajos, buscar_legajo[i], 0, len(legajos) - 1)
        t1 = time.perf_counter()                                # Detiene el cronómetro
        tiempo_binaria_recursiva = t1 - t0
        print(f"- Búsqueda Binaria Recursiva → índice: {resultado_binaria_recursiva}, tiempo: {tiempo_binaria_recursiva:.8f} s \n")

else:
    print("Opción no válida")