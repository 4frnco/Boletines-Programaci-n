###### ejercicio 3 #####
"""
Codificar el programa que al teclear un número por teclado,
muestre por consola el signo "+" si el número es positivo, el signo
"-" si es negativo y "0" si es cero.
"""
numeroclave = float(input("Dime un numero: "))

if numeroclave > 0:
    print("Tu número es +")

elif numeroclave < 0:
    print("Tu número es -")

else:
    print("Tu número es 0")