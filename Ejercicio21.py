###### ejercicio 21 #####
"""
Pedir una contraseña y validar que cumpla las condiciones:
- Mínimo 8 caracteres
- Al menos una mayúscula
- Al menos una minúscula
- Al menos un número
La función mostrará si la contraseña es válida o no.
"""


def validar_contrasinal():
    contrasinal = input("Escribe una contraseña: ")

    if len(contrasinal) < 8:
        print("Resultado: No es válida (debe tener al menos 8 caracteres).")
        return
    if not any(c.isupper() for c in contrasinal):
        print("Resultado: No es válida (debe contener al menos una mayúscula).")
        return
    if not any(c.islower() for c in contrasinal):
        print("Resultado: No es válida (debe contener al menos una minúscula).")
        return
    if not any(c.isdigit() for c in contrasinal):
        print("Resultado: No es válida (debe contener al menos un número).")
        return

    print("Resultado: Contraseña válida ✅")


if __name__ == "__main__":
    validar_contrasinal()
