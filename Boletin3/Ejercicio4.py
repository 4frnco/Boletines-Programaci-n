###### ejercicio 4 #####
"""
Conocidos, el nombre y el peso de dos personas, el programa
escribirá por consola los datos de la persona que pesa más y la
diferencia de peso entre ellas.
"""
persona1 = input("Dime tu nombre persona1: ")
peso1 = float(input("Dime tu peso persona1: "))

persona2 = input("Dime tu nombre persona2: ")
peso2 = float(input("Dime tu peso persona2: "))

if peso1 > peso2:
    print("Al parecer", persona1, "pesa mas que el otro sujeto y le saca", peso1 - peso2, "de diferencia")

elif peso1 < peso2:
    print("Al parecer", persona2, "pesa mas que el otro sujeto y le saca", peso2 - peso1, "kilogramos de diferencia")

else:
    print("Al parecer", persona1,"y", persona2, "pesan lo mismo")