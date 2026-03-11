###### ejercicio 12a #####
"""
Pedir una cadena y un caracter. Reemplazar todos los espacios por ese caracter.
Ej.: 'meu arquivo de texto.txt' y '_' -> 'meu_arquivo_de_texto.txt'
"""
def reemplazar_espacios():
    cadena = input("Escribe una cadena de caracteres: ")
    caracter = input("Escribe el caracter para reemplazar los espacios: ")
    print("Resultado:", cadena.replace(" ", caracter))


###### ejercicio 12b #####
"""
Pedir una cadena y un caracter. Insertar el caracter entre cada letra.
Ej.: 'separar' y ',' -> 's,e,p,a,r,a,r'
"""
def insertar_caracter():
    cadena = input("Escribe una cadena de caracteres: ")
    caracter = input("Escribe el caracter que se insertará entre las letras: ")
    print("Resultado:", caracter.join(cadena))


###### ejercicio 12c #####
"""
Pedir una cadena y un caracter. Reemplazar todos los dígitos por ese caracter.
Ej.: 'súa clave é: 1540' y 'X' -> 'súa clave é: XXXX'
"""
def reemplazar_digitos():
    cadena = input("Escribe una cadena de caracteres: ")
    caracter = input("Escribe el caracter para reemplazar los dígitos: ")
    resultado = ""
    for c in cadena:
        if c.isdigit():
            resultado += caracter
        else:
            resultado += c
    print("Resultado:", resultado)


###### ejercicio 12d #####
"""
Pedir una cadena y un caracter. Insertar el caracter cada 3 dígitos.
Ej.: '2552552550' y '.' -> '255.255.255.0'
"""
def insertar_cada_tres():
    cadena = input("Escribe una cadena de caracteres: ")
    caracter = input("Escribe el caracter para insertar cada 3 dígitos: ")
    resultado = ""
    for i in range(0, len(cadena), 3):
        resultado += cadena[i:i + 3] + caracter
    print("Resultado:", resultado[:-1])


if __name__ == "__main__":
    reemplazar_espacios()
    insertar_caracter()
    reemplazar_digitos()
    insertar_cada_tres()
