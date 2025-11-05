###### ejercicio 10 #####
"""
Diseñar un programa que calcule el área de un rectángulo cuya base y altura pides por
teclado. Asegúrate que estos valores sean positivos, para eso valida los datos.
"""
base = float(input("Introduce la base del rectángulo: "))
while base <= 0:
    base = float(input("La base debe ser positiva. Introdúcela de nuevo: "))

altura = float(input("Introduce la altura del rectángulo: "))
while altura <= 0:
    altura = float(input("La altura debe ser positiva. Introdúcela de nuevo: "))

area = base * altura
print("El área del rectángulo es:", area)