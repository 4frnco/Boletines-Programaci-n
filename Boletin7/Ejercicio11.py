###### ejercicio 11a #####
"""
Pedir una cadena e imprimir los dos primeros caracteres.
"""
def primeros_dos():
    cadena = input("Escribe una cadena de caracteres: ")
    print("Los dos primeros caracteres son:", cadena[:2])

###### ejercicio 11b #####
"""
Pedir una cadena e imprimir los tres últimos caracteres.
"""
def ultimos_tres():
    cadena = input("Escribe una cadena de caracteres: ")
    print("Los tres últimos caracteres son:", cadena[-3:])

###### ejercicio 11c #####
"""
Pedir una cadena e imprimirla cada dos caracteres. Ej.: 'recta' -> 'rca'
"""
def cada_dos():
    cadena = input("Escribe una cadena de caracteres: ")
    print("La cadena cada dos caracteres es:", cadena[::2])

###### ejercicio 11d #####
"""
Pedir una cadena e imprimirla en un sentido y en sentido inverso.
Ej.: 'reflexo' -> 'reflexooxelfer'
"""
def sentido_inverso():
    cadena = input("Escribe una cadena de caracteres: ")
    print("La cadena en ambos sentidos es:", cadena + cadena[::-1])

if __name__ == "__main__":
    primeros_dos()
    ultimos_tres()
    cada_dos()
    sentido_inverso()
