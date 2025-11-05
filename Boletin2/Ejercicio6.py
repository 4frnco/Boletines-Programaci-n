############### ejercicio 6 ###############
"""
Realizar el ordinograma correspondiente a un programa que muestre por pantalla el
porcentaje descontado en una compra. Introduciendo, por teclado, el precio de la tarifa y
el precio pagado.
"""
prezo_tarifa = float(input("Introduce o prezo da tarifa: "))
prezo_pagado = float(input("Introduce o prezo pagado: "))

desconto = prezo_tarifa - prezo_pagado
porcentaxe = (desconto / prezo_tarifa) * 100

print("A porcentaxe de desconto é:", porcentaxe, "%")