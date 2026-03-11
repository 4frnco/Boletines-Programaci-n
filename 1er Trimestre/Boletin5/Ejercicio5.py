###### ejercicio 5 #####
"""
Escribir un programa que reciba un número n por parámetro e imprima los primeros n
números triangulares, junto con su índice. Los números triangulares se obtienen
mediante la suma de los números naturales desde 1 hasta n.
"""
n = int(input("Introduce cuántos números triangulares quieres: "))

print("Usando la fórmula:")
for i in range(1, n+1):
    triangular = i * (i + 1) // 2  # // para obtener entero
    print(i, "-", triangular)