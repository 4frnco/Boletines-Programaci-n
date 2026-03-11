###### ejercicio 3 #####
"""
Ejercicio 3: Almacenar números del 1 al 10 en una lista y mostrarlos
en orden inverso separados por comas
"""

numeros = list(range(1, 11))
numeros.reverse()
resultado = ""
for i in range(len(numeros)):
    resultado += str(numeros[i])
    if i < len(numeros) - 1:
        resultado += ", "
print(resultado)