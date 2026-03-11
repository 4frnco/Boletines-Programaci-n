###### ejercicio 11 #####
"""
Ejercicio 11: Pedir números separados por comas,
almacenarlos en una lista y
mostrar su media y desviación típica
"""

entrada = input("Introduce números separados por comas: ")
numeros_str = entrada.split(",")
numeros = []
for num in numeros_str:
    numeros.append(float(num))

suma = 0
for num in numeros:
    suma += num
media = suma / len(numeros)

suma_cuadrados = 0
for num in numeros:
    suma_cuadrados += (num - media) ** 2
desviacion = (suma_cuadrados / len(numeros)) ** 0.5

print("Media:", media)
print("Desviación típica:", desviacion)