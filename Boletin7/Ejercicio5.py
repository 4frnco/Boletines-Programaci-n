###### ejercicio 5 #####
"""
Contar las vocales y las consonantes del String "Python Python Python".
¡Cuidado con los espacios!
"""
texto = "Python Python Python"
vocales = 0
consoantes = 0
for caracter in texto:
    if caracter.lower() in "aeiouáéíóú":
        vocales += 1
    elif caracter.isalpha():
        consoantes += 1
print("Vocales:", vocales)
print("Consonantes:", consoantes)