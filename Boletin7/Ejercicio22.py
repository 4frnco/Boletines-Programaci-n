###### ejercicio 22 #####
"""
Pedir un nombre completo y formatearlo:
- Eliminar los espacios en blanco.
- Poner en mayúscula la primera letra de cada palabra.
- Devolver el nombre completo formateado.
Ejemplo: 'juan perez garcia' -> 'JuanPerezGarcia'
"""
def formatear_nombre():
    nombre_completo = input("Escribe tu nombre completo: ")
    palabras = nombre_completo.split()
    resultado = []
    for palabra in palabras:
        resultado.append(palabra.capitalize())
    nombre_formateado = "".join(resultado)
    print("Resultado:", nombre_formateado)


if __name__ == "__main__":
    formatear_nombre()
