###### ejercicio 19 #####
"""
Pedir una cadena compuesta por unos y ceros (número binario)
y mostrar su valor decimal correspondiente.
Ejemplo: '1010' -> 10
"""
def binario_a_decimal():
    binario = input("Escribe un número binario (solo 0 y 1): ")
    try:
        decimal = int(binario, 2)
        print(f"Resultado: el valor decimal de {binario} es {decimal}.")
    except ValueError:
        print("Error: la cadena no es un número binario válido.")


if __name__ == "__main__":
    binario_a_decimal()
