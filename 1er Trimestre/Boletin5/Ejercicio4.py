###### ejercicio 4 #####
"""
Escribir un programa que imprima todos los números pares entre dos números que se
le pidan al usuario.
"""
n = int(input("Introduce cuántos números triangulares quieres: "))

print("Usando la fórmula:")
for i in range(1, n+1):
    triangular = i * (i + 1) // 2
    print(i, "-", triangular)