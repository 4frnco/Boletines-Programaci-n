###### ejercicio 7 #####
"""
Ejercicio 7: Pedir una palabra al usuario y mostrar
el número de veces que contiene cada vocal
"""

palabra = input("Introduce unha palabra: ")
vocales = "aeiouáéíóú"
contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0

for letra in palabra.lower():
    if letra == 'a' or letra == 'á':
        contador_a += 1
    elif letra == 'e' or letra == 'é':
        contador_e += 1
    elif letra == 'i' or letra == 'í':
        contador_i += 1
    elif letra == 'o' or letra == 'ó':
        contador_o += 1
    elif letra == 'u' or letra == 'ú':
        contador_u += 1

print("A:", contador_a)
print("E:", contador_e)
print("I:", contador_i)
print("O:", contador_o)
print("U:", contador_u)