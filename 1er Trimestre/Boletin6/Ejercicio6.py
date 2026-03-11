###### ejercicio 6 #####
"""
Ejercicio 6: Pedir una palabra al usuario
y mostrar si es un palíndromo
(se lee igual al derecho y al revés)
"""

palabra = input("Introduce unha palabra: ")
palabra_limpia = palabra.replace(" ", "").lower()
if palabra_limpia == palabra_limpia[::-1]:
    print("É un palíndromo")
else:
    print("Non é un palíndromo")