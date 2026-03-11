###### ejercicio 13 #####
"""
Solicitar al usuario un número n y dibujar un triángulo de base y altura n. Si el usuario
teclea el número 4 el triángulo sería de la siguiente forma:

-

-  *

-  * *

-  * * *
"""
n = int(input("Introduce la altura del triángulo: "))

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)