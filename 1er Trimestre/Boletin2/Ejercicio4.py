############# ejercicio 4 ##########
"""
Diseñar un ordinograma que lea 2 números y calcule la suma, después la resta, a
continuación el producto y por último el cociente. Muestra el resultado de cada
operación.
"""
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

suma = numero1 + numero2
resta = numero1 - numero2
producto = numero1 * numero2

if numero2 != 0:
    cociente = numero1 / numero2
else:
    cociente = "Error: no se puede dividir entre cero"

print("Suma:", suma)
print("Resta:", resta)
print("Producto:", producto)
print("Cociente:", cociente)