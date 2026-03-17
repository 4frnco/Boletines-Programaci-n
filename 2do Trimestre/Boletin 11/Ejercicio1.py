import os


def engadir_nota():
    """Engade unha nova nota ao ficheiro."""
    nota = input("Introduce a túa nota: ")
    with open("notas.txt", "a", encoding="utf-8") as ficheiro:
        ficheiro.write(nota + "\n")
    print("Nota gardada correctamente.\n")


def listar_notas():
    """Lista todas as notas gardadas."""
    if not os.path.exists("notas.txt"):
        print("Non hai notas gardadas.\n")
        return

    with open("notas.txt", "r", encoding="utf-8") as ficheiro:
        notas = ficheiro.readlines()

    if not notas:
        print("Non hai notas gardadas.\n")
        return

    print("\n=== NOTAS GARDADAS ===")
    for i, nota in enumerate(notas, 1):
        print(f"{i}. {nota.strip()}")
    print()


def buscar_notas():
    """Busca notas que conteñan unha palabra clave."""
    if not os.path.exists("notas.txt"):
        print("Non hai notas gardadas.\n")
        return

    palabra = input("Introduce a palabra clave: ").lower()

    with open("notas.txt", "r", encoding="utf-8") as ficheiro:
        notas = ficheiro.readlines()

    encontradas = []
    for nota in notas:
        if palabra in nota.lower():
            encontradas.append(nota.strip())

    if encontradas:
        print(f"\nNotas que conteñen '{palabra}':")
        for nota in encontradas:
            print(f"- {nota}")
    else:
        print(f"Non se atoparon notas con '{palabra}'.")
    print()


def menu_principal():
    """Menú principal do programa."""
    while True:
        print("=== XESTOR DE NOTAS PERSOAIS ===")
        print("1. Engadir nova nota")
        print("2. Listar todas as notas")
        print("3. Buscar notas por palabra clave")
        print("4. Saír")

        opcion = input("Selecciona unha opción (1-4): ")

        if opcion == "1":
            engadir_nota()
        elif opcion == "2":
            listar_notas()
        elif opcion == "3":
            buscar_notas()
        elif opcion == "4":
            print("Saíndo do programa...")
            break
        else:
            print("Opción non válida. Inténtao de novo.\n")


if __name__ == "__main__":
    menu_principal()