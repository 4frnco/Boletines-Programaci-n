# Ejercicico 2 - Boletín 11

"""
Ler un ficheiro de texto e contar cantas veces aparece cada palabra.
Solicita ao usuario o nome dun ficheiro .txt.

Mostra a frecuencia de cada palabra (ignorando maiúsculas/minúsculas e signos de puntuación).

Gárdase un resumo nun novo ficheiro resumo_palabras.txt.

"""

import string

# pide o nome do txt
nome_ficheiro = input("Introduce o nome do ficheiro .txt: ")

try:
    # abrir e ler o ficheiro
    with open(nome_ficheiro, "r", encoding="utf-8") as ficheiro:
        texto = ficheiro.read()

    # pasar todo a minúsculas
    texto = texto.lower()

    # eliminar signos de puntuación
    for signo in string.punctuation:
        texto = texto.replace(signo, "")

    # separar palabras
    palabras = texto.split()

    # contar frecuencia
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    # muestra resultados
    print("\nFrecuencia de palabras:")
    for palabra, conta in frecuencia.items():
        print(palabra, ":", conta)

    # gardar resumo nun ficheiro novo
    with open("ejercicio2_resumo_palabras", "w", encoding="utf-8") as resumo:
        for palabra, conta in frecuencia.items():
            resumo.write(f"{palabra}: {conta}\n")

    print("\nResumo gardado en 'ejercicio2_resumo_palabras.txt'.")

except FileNotFoundError:
    print("O ficheiro non existe.")


