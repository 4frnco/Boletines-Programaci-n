###### ejercicio 3 #####
"""
Utilizar el programa anterior para generar una tabla de conversión de temperaturas,
desde 0º F hasta 120º F, de 10 en 10.
"""
fahrenheit = 0

celsius = (fahrenheit - 32) * 5 / 9

while fahrenheit <= 120:
    print(fahrenheit, "grados Fahrenheit son", celsius, "grados Celsius")
    fahrenheit += 10