###### ejercicio 2 #####
"""
Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
Recordad que la fórmula para la conversión es: F = 9/5 * C + 32.
"""
fahrenheit = float(input("Introduce la temperatura en grados Fahrenheit: "))

celsius = (fahrenheit - 32) * 5 / 9

print(fahrenheit, "grados Fahrenheit son", celsius, "grados Celsius")