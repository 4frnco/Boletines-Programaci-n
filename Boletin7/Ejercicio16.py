###### ejercicio 16a #####
"""
Pedir una cadena y devolver solamente las letras consonantes.
Ejemplo: 'algoritmos' -> 'lgrtms'
"""
def solo_consonantes():
    cadena = input("Escribe una cadena de caracteres: ")
    consonantes = ""
    for caracter in cadena:
        if caracter.lower() in "bcdfghjklmnñpqrstvwxyz":
            consonantes += caracter
    print("Resultado:", consonantes)


###### ejercicio 16b #####
"""
Pedir una cadena y devolver solamente las letras vocales.
Ejemplo: 'sen consonantes' -> 'e ooae'
"""
def solo_vocales():
    cadena = input("Escribe una cadena de caracteres: ")
    vocales = ""
    for caracter in cadena:
        if caracter.lower() in "aeiouáéíóú":
            vocales += caracter
    print("Resultado:", vocales)


###### ejercicio 16c #####
"""
Pedir una cadena y sustituir cada vocal por su siguiente vocal.
Ejemplo: 'vestiario' -> 'vostoerou'
"""
def siguiente_vocal():
    cadena = input("Escribe una cadena de caracteres: ")
    vocales = "aeioua"
    resultado = ""
    for caracter in cadena:
        if caracter.lower() in "aeiou":
            indice = vocales.index(caracter.lower())
            nueva_vocal = vocales[indice + 1]
            # Mantener mayúsculas si las hay
            if caracter.isupper():
                nueva_vocal = nueva_vocal.upper()
            resultado += nueva_vocal
        else:
            resultado += caracter
    print("Resultado:", resultado)


if __name__ == "__main__":
    solo_consonantes()
    solo_vocales()
    siguiente_vocal()
