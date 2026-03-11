###### ejercicio 23 #####
"""
Pedir un texto y realizar un análisis simple:
- Contar el número de palabras.
- Contar el número de caracteres.
- Encontrar la palabra más larga.
Mostrar los resultados por pantalla.
"""
def analizar_texto():
    texto = input("Escribe un texto: ")
    palabras = texto.split()

    if not palabras:
        print("No se ingresó ningún texto.")
        return

    num_palabras = len(palabras)
    num_caracteres = len(texto)
    palabra_mas_larga = max(palabras, key=len)

    print("Número de palabras:", num_palabras)
    print("Número de caracteres:", num_caracteres)
    print("Palabra más larga:", palabra_mas_larga)


if __name__ == "__main__":
    analizar_texto()
