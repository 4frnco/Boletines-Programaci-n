###### ejercicio 5 #####
"""
Dados 3 números que se suponen distintos, indicar cuál es el
mayor.
"""
numero1 = float(input("Dime tu primer numero: "))
numero2 = float(input("Dime tu segundo numero: "))
numero3 = float(input("Dime tu tercer numero: "))

if numero1 > numero2 and numero1 > numero3:
    print("En este caso", numero1 ,"que fue el primer numero es el mayor")

elif numero2 > numero1 and numero2 > numero3:
    print("En este caso", numero2 ,"que fue el segundo numero es el mayor")

elif numero3 > numero1 and numero3 > numero2:
    print("En este caso", numero3 ,"que fue el tercer numero es el mayor")

else:
    print("Los tres numeros que escribiste son iguales")