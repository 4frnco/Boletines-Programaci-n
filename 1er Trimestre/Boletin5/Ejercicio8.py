###### ejercicio 8 #####
"""
Modificar el programa anterior para que pueda generar fichas de un juego que puede tener
números de 0 a n.
"""
n = int(input("Introduce el número máximo del dominó: "))

for i in range(n + 1):
    for j in range(i, n + 1):
        print(i, "|", j)