###### ejercicio 5 #####
"""
Ejercicio 5: Almacenar el abecedario
en una lista y crear otra lista
eliminando las letras en posiciones múltiplos de 3
"""

abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
resultado = []
for i in range(len(abecedario)):
    if (i + 1) % 3 != 0:
        resultado.append(abecedario[i])
print(resultado)