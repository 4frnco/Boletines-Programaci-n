###### ejercicio 2 #####
"""
Ejercicio 2: Preguntar los números
ganadores de la lotería primitiva,
almacenarlos en una lista y mostrarlos
ordenados de menor a mayor
"""

numeros = []
print("Introduce os números gañadores da lotería primitiva:")
for i in range(6):
    numero = int(input("Número " + str(i+1) + ": "))
    numeros.append(numero)

numeros.sort()
print("Números ordenados:", numeros)