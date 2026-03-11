################# ejercicio 7 ###################
"""
Realizar el ordinograma y después codificar un programa que reciba como dato de
entrada el valor de una temperatura expresada en grados centígrados y calcule su
equivalente en grados Fahrenheit y grados Kelvin.
"""
temperatura_celsius = float(input("Introduce a temperatura en graos Celsius: "))

temperatura_fahrenheit = temperatura_celsius * 9/5 + 32

temperatura_kelvin = temperatura_celsius + 273.15

print("Temperatura en Fahrenheit:", temperatura_fahrenheit, "°F")
print("Temperatura en Kelvin:", temperatura_kelvin, "K")