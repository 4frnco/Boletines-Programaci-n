###### ejercicio 3 #####
"""
Utilizar el operador ternario para calcular el valor absoluto de un número
que se solicita al usuario por teclado.
"""
numero = float(input("Dime un número: "))

valor_absoluto = numero if numero >= 0 else -numero

print("El valor absoluto del número es:", valor_absoluto)