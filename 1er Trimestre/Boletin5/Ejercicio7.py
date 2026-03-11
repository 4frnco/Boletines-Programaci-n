###### ejercicio 7 #####
"""
Escribir un programa que imprima por pantalla todas las fichas de dominó, de una por
una y sin repetir.
"""
for i in range(7):
    for j in range(i, 7):
        print(i, "|", j)