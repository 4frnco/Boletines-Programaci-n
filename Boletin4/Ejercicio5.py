###### ejercicio 5 #####
"""
El DNI tiene una parte numérica de 8 dígitos seguido de una letra que
se obtiene a partir del número de la siguiente forma:

letra = número DNI % 23.

Basándote en esta información, elige la letra a partir de la numeración de
la siguiente tabla:
0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22
T  R  W  A  G  M  Y  F  P  D  X  B  N  J  Z  S  Q  V  H  L  C  K  E

Diseñar una aplicación en la que, dado un número de DNI, calcule la letra
que le corresponde. Observa que un número de 8 dígitos entra dentro
del rango de un tipo int.
"""
numero_dni = int(input("Introduce tu número de DNI (solo números): "))

letras = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]

resto = numero_dni % 23
letra_dni = letras[resto]

print("La letra del DNI es:", letra_dni)
print("DNI completo:", str(numero_dni) + letra_dni)