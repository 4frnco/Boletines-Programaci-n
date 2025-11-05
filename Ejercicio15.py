###### ejercicio 15i #####
"""
Pedir una cadena y devolver la primera letra de cada palabra.
Ejemplo: 'Universal Serial Bus' -> 'USB'
"""
def primeras_letras():
    cadena = input("Escribe una cadena de caracteres: ")
    palabras = cadena.split()
    resultado = ""
    for palabra in palabras:
        resultado += palabra[0]
    print("Resultado:", resultado)


###### ejercicio 15ii #####
"""
Pedir una cadena y devolver una cadena con la primera letra de cada palabra en mayúscula.
Ejemplo: 'república arxentina' -> 'República Arxentina'
"""
def capitalizar_palabras():
    cadena = input("Escribe una cadena de caracteres: ")
    palabras = cadena.split()
    resultado = []
    for palabra in palabras:
        resultado.append(palabra.capitalize())
    print("Resultado:", " ".join(resultado))


###### ejercicio 15iii #####
"""
Pedir una cadena y devolver las palabras que comiencen con la letra 'A' (o 'a').
Ejemplo: 'Antes de abrir' -> 'Antes abrir'
"""
def palabras_con_a():
    cadena = input("Escribe una cadena de caracteres: ")
    palabras = cadena.split()
    resultado = []
    for palabra in palabras:
        if palabra.lower().startswith('a'):
            resultado.append(palabra)
    print("Resultado:", " ".join(resultado))


if __name__ == "__main__":
    primeras_letras()
    capitalizar_palabras()
    palabras_con_a()
