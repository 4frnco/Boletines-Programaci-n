###### ejercicio 20i #####
"""
Pedir una cadena y un caracter, y devolver una nueva cadena formada
exclusivamente por el caracter, con la misma longitud que la cadena original.
Ejemplo: 'python' y '*' -> '******'
"""
def nueva_cadena_caracter():
    cadena = input("Escribe una cadena de caracteres: ")
    caracter = input("Escribe el caracter con el que se formará la nueva cadena: ")
    resultado = caracter * len(cadena)
    print("Resultado:", resultado)


###### ejercicio 20ii #####
"""
Pedir una cadena y un caracter, y devolver una nueva cadena en la que
solo aparecen el caracter encontrado y guiones en las demás posiciones.
Ejemplo: 'banana' y 'a' -> '-a-a-a'
"""
def encontrar_caracter():
    cadena = input("Escribe una cadena de caracteres: ")
    caracter = input("Escribe el caracter que deseas buscar: ")
    resultado = ""
    for c in cadena:
        if c == caracter:
            resultado += c
        else:
            resultado += "-"
    print("Resultado:", resultado)


if __name__ == "__main__":
    nueva_cadena_caracter()
    encontrar_caracter()
