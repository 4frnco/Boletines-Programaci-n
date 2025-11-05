###### ejercicio 14 #####
"""
Codificar el programa que solicite 10 números por consola y calcule su suma. Si el
usuario introduce en cualquier momento el número 999, deja de solicitar más números
y presenta el valor de la suma alcanzada hasta ese momento.
"""
suma = 0
contador = 0

while contador < 10:
    num = int(input("Introduce un número (999 para parar): "))
    if num == 999:
        break
    suma += num
    contador += 1

print("La suma total es:", suma)