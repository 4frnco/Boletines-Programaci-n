###### ejercicio 18a #####
"""
Pedir dos cadenas e indicar si la segunda es una subcadena de la primera.
Ejemplo: 'subcadea' y 'cadea' -> 'cadea' es una subcadena de 'subcadea'.
"""
def es_subcadena():
    cadena1 = input("Escribe la primera cadena: ")
    cadena2 = input("Escribe la segunda cadena: ")
    if cadena2 in cadena1:
        print(f"Resultado: '{cadena2}' es una subcadena de '{cadena1}'.")
    else:
        print(f"Resultado: '{cadena2}' NO es una subcadena de '{cadena1}'.")


###### ejercicio 18b #####
"""
Pedir dos cadenas y devolver la que sea anterior en orden alfabético.
Ejemplo: 'kde' y 'gnome' -> 'gnome'
"""
def anterior_alfabetico():
    cadena1 = input("Escribe la primera cadena: ")
    cadena2 = input("Escribe la segunda cadena: ")
    if cadena1 < cadena2:
        print(f"Resultado: '{cadena1}' es anterior alfabéticamente.")
    elif cadena2 < cadena1:
        print(f"Resultado: '{cadena2}' es anterior alfabéticamente.")
    else:
        print("Resultado: Ambas cadenas son iguales.")


if __name__ == "__main__":
    es_subcadena()
    anterior_alfabetico()
