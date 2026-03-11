###### ejercicio 4 #####
"""
Escribir un programa que solicite al usuario un número comprendido
entre 1 y 99. El programa tiene que mostrarlo con letras, por ejemplo, para
el 56, mostrará: "Cincuenta y seis".
"""
numero = int(input("Introduce un número entre 1 y 99: "))

if numero < 1 or numero > 99:
    print("Número fuera de rango")
else:
    unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    decenas = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    especiales = ["once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"]

    if numero == 10:
        print("diez")
    elif 11 <= numero <= 19:
        print(especiales[numero - 11])
    else:
        d = numero // 10
        u = numero % 10
        if d == 0:
            print(unidades[u])
        elif u == 0:
            print(decenas[d])
        else:
            print(decenas[d] + " y " + unidades[u])