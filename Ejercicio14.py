###### ejercicio 14 #####
"""
Pedir una cadena que contenga un número entero largo y mostrarlo con separaciones de miles.
Ejemplo: si se ingresa 1234567890, debe mostrar 1.234.567.890
"""
def formato_miles():
    numero_str = input("Escribe un número entero largo: ")
    resultado = ""
    contador = 0
    for i in range(len(numero_str) - 1, -1, -1):
        if contador == 3:
            resultado = "." + resultado
            contador = 0
        resultado = numero_str[i] + resultado
        contador += 1
    print("Número con formato de miles:", resultado)


if __name__ == "__main__":
    formato_miles()
