################## ejercicio 9 ################
"""
Realizar un algoritmo y codificar el programa correspondiente que lea, desde el teclado,
una cantidad entera en euros y muestre, por pantalla, su desglose en billetes de
100, 20, 5 y monedas de 1 €.
"""
cantidad = int(input("Introduce una cantidad entera en euros: "))

billete100 = cantidad // 100
resto = cantidad % 100

billete20 = resto // 20
resto = resto % 20

billete5 = resto // 5
moneda1 = resto % 5

print("Desglose da cantidade:")
print("Billetes de 100€:", billete100)
print("Billetes de 20€:", billete20)
print("Billetes de 5€:", billete5)
print("Monedas de 1€:", moneda1)