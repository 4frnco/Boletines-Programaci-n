###### ejercicio 6 #####
"""
Escribir un programa que tome una cantidad m de valores ingresados por el usuario,
a cada uno le calcule el factorial e imprima el resultado junto con el número de orden
correspondiente.
"""
m = int(input("¿Cuántos números quieres ingresar? "))

for i in range(1, m + 1):
    numero = int(input("Introduce el número " + str(i) + ": "))

    factorial = 1
    for j in range(1, numero + 1):
        factorial *= j

    print("El factorial del número", numero, "(", i, "º número ) es:", factorial)