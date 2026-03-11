###### ejercicio 2 #####
"""
Escribir un programa en el que se tecleen dos números. Si el
primero es mayor o igual que el segundo, visualizaremos la
resta. En cualquier caso visualizaremos la suma.
"""
primer_numero = float(input("Dime un numero: "))
segundo_numero = float(input("Dime un numero: "))

if primer_numero >= segundo_numero:
    print(primer_numero - segundo_numero)

print(primer_numero + segundo_numero)