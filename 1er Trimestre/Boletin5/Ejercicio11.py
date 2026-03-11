###### ejercicio 11 #####
"""
Codificar un programa que solicite un número y visualice la tabla de multiplicar de ese
número. El programa seguirá pidiendo números hasta que el usuario pulse el número cero.
"""
while True:
    numero = int(input("Introduce un número (0 para salir): "))
    if numero == 0:
        print("Programa terminado.")
        break
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)