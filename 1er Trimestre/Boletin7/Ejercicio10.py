###### ejercicio 10 #####
"""
Escribir un método que dado un objeto de la clase str cuente diferentes tipos de caracteres.
En particular, el método deberá imprimir el número de letras, dígitos y espacios en blanco
de la cadena. Hacer un programa que calcule la cadena: «Ola, son alumno de DAM1,
e son programador desde o 2025».
"""
def contar_caracteres(cadena):
    letras = 0
    digitos = 0
    espacios = 0
    for caracter in cadena:
        if caracter.isalpha():
            letras += 1
        elif caracter.isdigit():
            digitos += 1
        elif caracter.isspace():
            espacios += 1
    print("Letras:", letras)
    print("Dígitos:", digitos)
    print("Espacios:", espacios)

texto = "Ola, son alumno de DAM1, e son programador desde o 2025"
contar_caracteres(texto)