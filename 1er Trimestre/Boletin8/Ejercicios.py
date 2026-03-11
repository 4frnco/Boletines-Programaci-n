###### ejercicio 1 #####
"""
Escribir una función que reciba una tupla de elementos e indique si se
encuentran ordenados de menor a mayor.
"""

def esta_ordenada(tupla):
    for i in range(len(tupla) - 1):
        if tupla[i] > tupla[i + 1]:
            return False
    return True


###### ejercicio 2 #####
"""
Escribir una función que indique si dos fichas de dominó encajan. Las
fichas son recibidas en dos tuplas, por ejemplo: (3,4) y (5,4). La función
devuelve un booleano con el resultado del encaje.
"""

def fichas_encajan(ficha1, ficha2):
    return ficha1[0] == ficha2[0] or ficha1[0] == ficha2[1] or ficha1[1] == ficha2[0] or ficha1[1] == ficha2[1]


###### ejercicio 3 #####
"""
Escribir una función que reciba una tupla con nombres y para cada nombre
imprima una mensaje 'Estimado don/dona Nombre'
"""

def saludo_nombres(nombres):
    for nombre in nombres:
        print("Estimado don/dona", nombre)


###### ejercicio 4 #####
"""
Escribir una función que reciba una tupla con nombres, una posición de
origen p y una cantidad n, e imprima el mensaje anterior (ejercicio 3) para
los n nombres que se encuentran a partir de la posición p.
"""

def saludo_nombres_rango(nombres, p, n):
    for i in range(p, min(p + n, len(nombres))):
        print("Estimado don/dona", nombres[i])


###### ejercicio 5 #####
"""
Modificar las funciones anteriores para que tengan en cuenta el género del
destinatario, para ello, deberán recibir una tupla de tuplas, conteniendo el nombre
y el género, adaptando el mensaje con 'don' o 'dona' dependiendo de este.
"""

def saludo_con_genero(personas):
    for persona in personas:
        nombre, genero = persona
        if genero.lower() == 'hombre':
            print("Estimado don", nombre)
        else:
            print("Estimada dona", nombre)


###### ejercicio 6 #####
"""
Dada una lista de números enteros, escribir una función que:
- Devuelva una lista con todos los que sean primos.
- Devuelva el sumatorio y el promedio de los valores.
- Devuelva una lista con el factorial de cada uno de esos números.
"""

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def operaciones_lista(numeros):
    primos = [n for n in numeros if es_primo(n)]
    sumatorio = sum(numeros)
    promedio = sumatorio / len(numeros)

    factoriales = []
    for n in numeros:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        factoriales.append(fact)

    return primos, sumatorio, promedio, factoriales


###### ejercicio 7 #####
"""
Dada una lista de números enteros y un entero k, escribir una función que:
- Devuelva tres listas, una con los menores, otra con los mayores y otra con los
iguales a k.
- Devuelva una lista con aquellos que son múltiplos de k.
"""

def clasificar_numeros(numeros, k):
    menores = [n for n in numeros if n < k]
    mayores = [n for n in numeros if n > k]
    iguales = [n for n in numeros if n == k]
    multiplos = [n for n in numeros if n % k == 0]

    return menores, mayores, iguales, multiplos


###### ejercicio 8 #####
"""
Escribir una función que reciba una lista de tuplas (Apellido, Nombre,
Inicial_segundo_nombre) y devuelva una lista de cadenas donde cada una
contenga primero el nombre, luego la inicial con un punto, y luego el apellido.
"""

def formatear_nombres(personas):
    resultado = []
    for persona in personas:
        apellido, nombre, inicial = persona
        resultado.append(f"{nombre} {inicial}. {apellido}")
    return resultado


###### ejercicio 9 #####
"""
Escribir una función empaquetar para una lista, donde empaquetar significa
indicar la repetición de valores consecutivos mediante una tupla (valor,
cantidad de repeticiones). Por ejemplo, empaquetar ([1, 1, 1, 3, 5, 1, 1, 3, 3])
debe devolver [(1, 3), (3, 1), (5, 1), (1, 2), (3, 2)].
"""

def empaquetar(lista):
    if not lista:
        return []

    resultado = []
    valor_actual = lista[0]
    contador = 1

    for i in range(1, len(lista)):
        if lista[i] == valor_actual:
            contador += 1
        else:
            resultado.append((valor_actual, contador))
            valor_actual = lista[i]
            contador = 1

    resultado.append((valor_actual, contador))
    return resultado


###### ejercicio 10 #####
"""
Matrices.
- Escribir una función que reciba dos matrices y devuelva la suma.
- Escribir una función que reciba dos matrices y devuelva el producto.
"""

def sumar_matrices(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        return None

    resultado = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz1[0])):
            fila.append(matriz1[i][j] + matriz2[i][j])
        resultado.append(fila)
    return resultado

def multiplicar_matrices(matriz1, matriz2):
    if len(matriz1[0]) != len(matriz2):
        return None

    resultado = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz2[0])):
            suma = 0
            for k in range(len(matriz2)):
                suma += matriz1[i][k] * matriz2[k][j]
            fila.append(suma)
        resultado.append(fila)
    return resultado


###### ejercicio 11 #####
"""
Plegado de un texto. Escribir una función que reciba un texto y una
longitud y devuelva una lista de cadenas de como máximo esa longitud. Las
líneas deben cortarse correctamente en los espacios (sin cortar las palabras).
"""

def plegar_texto(texto, longitud_maxima):
    palabras = texto.split()
    lineas = []
    linea_actual = ""

    for palabra in palabras:
        if len(linea_actual) + len(palabra) + 1 <= longitud_maxima:
            if linea_actual:
                linea_actual += " " + palabra
            else:
                linea_actual = palabra
        else:
            if linea_actual:
                lineas.append(linea_actual)
            if len(palabra) <= longitud_maxima:
                linea_actual = palabra
            else:
                lineas.append(palabra[:longitud_maxima])
                linea_actual = palabra[longitud_maxima:]

    if linea_actual:
        lineas.append(linea_actual)

    return lineas


###### MENÚ INTERACTIVO #####

def menu():
    while True:
        print("\nSelecciona un ejercicio para ejecutar (1-11) o 0 para salir:")
        print("1. Comprobar si una tupla está ordenada")
        print("2. Comprobar si fichas de dominó encajan")
        print("3. Saludo a nombres")
        print("4. Saludo a nombres en rango")
        print("5. Saludo con género")
        print("6. Operaciones con lista de números")
        print("7. Clasificación de números según k")
        print("8. Formatear nombres")
        print("9. Empaquetar lista")
        print("10. Operaciones con matrices")
        print("11. Plegado de texto")
        opcion = input("Opción: ")

        if opcion == "0":
            break
        elif opcion == "1":
            tupla = tuple(map(int, input("Introduce la tupla separada por comas: ").split(",")))
            print(esta_ordenada(tupla))
        elif opcion == "2":
            ficha1 = tuple(map(int, input("Ficha 1 (num1,num2): ").split(",")))
            ficha2 = tuple(map(int, input("Ficha 2 (num1,num2): ").split(",")))
            print(fichas_encajan(ficha1, ficha2))
        elif opcion == "3":
            nombres = tuple(input("Introduce los nombres separados por comas: ").split(","))
            saludo_nombres(nombres)
        elif opcion == "4":
            nombres = tuple(input("Introduce los nombres separados por comas: ").split(","))
            p = int(input("Posición de inicio: "))
            n = int(input("Cantidad de nombres: "))
            saludo_nombres_rango(nombres, p, n)
        elif opcion == "5":
            personas = []
            cantidad = int(input("Cantidad de personas: "))
            for _ in range(cantidad):
                nombre = input("Nombre: ")
                genero = input("Género (hombre/mujer): ")
                personas.append((nombre, genero))
            saludo_con_genero(personas)
        elif opcion == "6":
            numeros = list(map(int, input("Introduce los números separados por comas: ").split(",")))
            primos, suma, promedio, factoriales = operaciones_lista(numeros)
            print("Primos:", primos)
            print("Suma:", suma)
            print("Promedio:", promedio)
            print("Factoriales:", factoriales)
        elif opcion == "7":
            numeros = list(map(int, input("Introduce los números separados por comas: ").split(",")))
            k = int(input("Introduce el número k: "))
            menores, mayores, iguales, multiplos = clasificar_numeros(numeros, k)
            print("Menores:", menores)
            print("Mayores:", mayores)
            print("Iguales:", iguales)
            print("Múltiplos de k:", multiplos)
        elif opcion == "8":
            personas = []
            cantidad = int(input("Cantidad de personas: "))
            for _ in range(cantidad):
                apellido = input("Apellido: ")
                nombre = input("Nombre: ")
                inicial = input("Inicial segundo nombre: ")
                personas.append((apellido, nombre, inicial))
            print(formatear_nombres(personas))
        elif opcion == "9":
            lista = list(map(int, input("Introduce la lista separada por comas: ").split(",")))
            print(empaquetar(lista))
        elif opcion == "10":
            filas = int(input("Número de filas de la matriz: "))
            columnas = int(input("Número de columnas de la matriz: "))
            print("Matriz 1:")
            matriz1 = [list(map(int, input(f"Fila {i+1}: ").split())) for i in range(filas)]
            print("Matriz 2:")
            matriz2 = [list(map(int, input(f"Fila {i+1}: ").split())) for i in range(filas)]
            print("Suma:")
            print(sumar_matrices(matriz1, matriz2))
            print("Producto:")
            print(multiplicar_matrices(matriz1, matriz2))
        elif opcion == "11":
            texto = input("Introduce el texto: ")
            longitud = int(input("Longitud máxima de línea: "))
            print(plegar_texto(texto, longitud))
        else:
            print("Opción no válida.")

# Ejecutar el menú
menu()
