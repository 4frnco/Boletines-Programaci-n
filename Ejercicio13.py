###### ejercicio 13a #####
"""
Pedir una cadena, un caracter y un límite.
Reemplazar los espacios por el caracter, hasta el número máximo de reemplazos indicado.
"""


def reemplazar_espacios_limite():
    cadena = input("Escribe una cadena de caracteres: ")
    caracter = input("Escribe el caracter para reemplazar los espacios: ")
    limite = int(input("Escribe la cantidad máxima de reemplazos: "))
    print("Resultado:", cadena.replace(" ", caracter, limite))


###### ejercicio 13b #####
"""
Pedir una cadena, un caracter y un límite. 
Insertar el caracter entre letras hasta el número máximo de inserciones indicado.
"""


def insertar_caracter_limite():
    cadena = input("Escribe una cadena de caracteres: ")
    caracter = input("Escribe el caracter que se insertará entre las letras: ")
    limite = int(input("Escribe la cantidad máxima de inserciones: "))

    resultado = ""
    contador = 0
    for i, c in enumerate(cadena):
        resultado += c
        # Solo insertar si no es el último carácter y no se superó el límite
        if i < len(cadena) - 1 and contador < limite:
            resultado += caracter
            contador += 1
    print("Resultado:", resultado)


###### ejercicio 13c #####
"""
Pedir una cadena, un caracter y un límite. 
Reemplazar los dígitos por el caracter hasta el número máximo de reemplazos indicado.
"""


def reemplazar_digitos_limite():
    cadena = input("Escribe una cadena de caracteres: ")
    caracter = input("Escribe el caracter para reemplazar los dígitos: ")
    limite = int(input("Escribe la cantidad máxima de reemplazos: "))

    resultado = ""
    contador = 0
    for c in cadena:
        if c.isdigit() and contador < limite:
            resultado += caracter
            contador += 1
        else:
            resultado += c
    print("Resultado:", resultado)


if __name__ == "__main__":
    reemplazar_espacios_limite()
    insertar_caracter_limite()
    reemplazar_digitos_limite()
