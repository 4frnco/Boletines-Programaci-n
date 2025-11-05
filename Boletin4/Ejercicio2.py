###### ejercicio 2 #####
"""
Codificar un programa que, utilizando un menú de opciones, calcule la
superficie de distintos tipos de figuras.

El usuario seleccionará la opción deseada escribiendo la opción.
Según esta, el programa le pedirá los datos necesarios para realizar el
cálculo, visualizará el resultado.

En el caso de pulsar una opción que no tenga el menú visualizar un
mensaje de "Opción incorrecta".

1 - Cuadrado
2 - Triángulo
3 - Círculo
"""
print("Menú de opciones:")
print("1 - Cuadrado")
print("2 - Triángulo")
print("3 - Círculo")

opcion = int(input("Elige una opción (1, 2 o 3): "))

if opcion == 1:
    lado = float(input("Dime la medida del lado del cuadrado: "))
    superficie = lado * lado
    print("La superficie del cuadrado es:", superficie)

elif opcion == 2:
    base = float(input("Dime la base del triángulo: "))
    altura = float(input("Dime la altura del triángulo: "))
    superficie = (base * altura) / 2
    print("La superficie del triángulo es:", superficie)

elif opcion == 3:
    radio = float(input("Dime el radio del círculo: "))
    superficie = 3.1416 * radio ** 2
    print("La superficie del círculo es:", superficie)

else:
    print("Opción incorrecta")