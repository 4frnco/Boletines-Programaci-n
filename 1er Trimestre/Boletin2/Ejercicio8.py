############## ejercicio 8 ###################
"""
Diseñar un programa para el software de una máquina, que convierta una cantidad
entera de dinero, que está presentada en billetes de 100, 20, 5 y monedas de 1 €, en su
equivalente en euros. Por ejemplo 2 billetes de 100€, 3 billetes de 20 €, 6
monedas de 1€ visualizaríamos 266 €.
"""
billete_cien = float(input("Dime cuantos billetes de cien euros tienes: "))
billete_veinte = float(input("Dime cuantos billetes de veinte euros tienes: "))
billete_cinco = float(input("Dime cuantos billetes de cinco euros tienes: "))
moneda_uno = float(input("Dime cuantas monedas de un euro tienes: "))

multicien = (billete_cien * 100)
multiveinte = (billete_veinte * 20)
multicinco = (billete_cinco * 5)
multiuno = (moneda_uno * 1)

sumatotal = (multicien + multiveinte + multicinco + multiuno)

print("El total de dinero que tienes es:", sumatotal)