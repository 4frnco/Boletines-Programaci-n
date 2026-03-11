###### ejercicio 9 #####
"""
Calcular la cantidad de números negativos, positivos y ceros que hay en un grupo de 10
números enteros.
"""
negativos = 0
positivos = 0
ceros = 0

for i in range(10):
    num = int(input(f"Introduce el número {i+1}: "))
    if num < 0:
        negativos += 1
    elif num > 0:
        positivos += 1
    else:
        ceros += 1

print("Negativos:", negativos)
print("Positivos:", positivos)
print("Ceros:", ceros)