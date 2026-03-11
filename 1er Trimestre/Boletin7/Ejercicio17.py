###### ejercicio 17 #####
"""
Pedir una cadena e indicar si se trata de un palíndromo.
Ejemplo: 'anita lava la tina' -> Es un palíndromo.
"""
def es_palindromo():
    cadena = input("Escribe una cadena de caracteres: ")
    cadena_limpia = cadena.replace(" ", "").lower()
    if cadena_limpia == cadena_limpia[::-1]:
        print("Resultado: Es un palíndromo.")
    else:
        print("Resultado: No es un palíndromo.")


if __name__ == "__main__":
    es_palindromo()
