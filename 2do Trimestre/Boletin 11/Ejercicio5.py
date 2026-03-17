import csv
import os


def valor_total_inventario():
    """Calcula o valor total do inventario dende un ficheiro CSV."""
    try:
        with open('produtos.csv', 'r', encoding='utf-8') as ficheiro:
            lector = csv.DictReader(ficheiro)
            total = 0

            print("\n=== DETALLE DO INVENTARIO ===")
            for fila in lector:
                prezo = float(fila['prezo'])
                stock = int(fila['stock'])
                valor = prezo * stock
                total += valor
                print(f"{fila['nome']}: {stock} unidades x {prezo}€ = {valor:.2f}€")

            print(f"\nVALOR TOTAL DO INVENTARIO: {total:.2f}€")

    except FileNotFoundError:
        print("Erro: Non se atopou o ficheiro 'produtos.csv'")
    except Exception as e:
        print(f"Erro ao procesar o ficheiro: {e}")


def existencias_baixas():
    """Crea un ficheiro cos produtos con stock baixo."""
    try:
        with open('produtos.csv', 'r', encoding='utf-8') as ficheiro:
            lector = csv.DictReader(ficheiro)
            produtos_baixos = []

            for fila in lector:
                if int(fila['stock']) < 5:
                    produtos_baixos.append({
                        'id': fila['id'],
                        'nome': fila['nome'],
                        'stock': fila['stock']
                    })

            if produtos_baixos:
                with open('baixo_stock.csv', 'w', newline='', encoding='utf-8') as saida:
                    campos = ['id', 'nome', 'stock']
                    escritor = csv.DictWriter(saida, fieldnames=campos)
                    escritor.writeheader()
                    escritor.writerows(produtos_baixos)

                print(f"Creouse 'baixo_stock.csv' con {len(produtos_baixos)} produtos.")

                print("\nProdutos con stock baixo:")
                for p in produtos_baixos:
                    print(f"- {p['nome']} (ID: {p['id']}, Stock: {p['stock']})")
            else:
                print("Non hai produtos con stock inferior a 5 unidades.")

    except FileNotFoundError:
        print("Erro: Non se atopou o ficheiro 'produtos.csv'")
    except Exception as e:
        print(f"Erro ao procesar o ficheiro: {e}")


def crear_ficheiro_exemplo():
    """Crea un ficheiro CSV de exemplo para probas."""
    produtos = [
        {'id': '1', 'nome': 'Portátil', 'prezo': '800', 'stock': '10'},
        {'id': '2', 'nome': 'Rato', 'prezo': '25', 'stock': '3'},
        {'id': '3', 'nome': 'Teclado', 'prezo': '45', 'stock': '2'},
        {'id': '4', 'nome': 'Monitor', 'prezo': '250', 'stock': '7'},
        {'id': '5', 'nome': 'Webcam', 'prezo': '60', 'stock': '1'},
    ]

    with open('produtos.csv', 'w', newline='', encoding='utf-8') as ficheiro:
        campos = ['id', 'nome', 'prezo', 'stock']
        escritor = csv.DictWriter(ficheiro, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(produtos)

    print("Ficheiro 'produtos.csv' creado para probas.\n")


def menu():
    """Menú principal do programa."""
    if not os.path.exists('produtos.csv'):
        crear = input("Non se atopa 'produtos.csv'. Queres crear un de exemplo? (s/n): ")
        if crear.lower() == 's':
            crear_ficheiro_exemplo()
        else:
            print("O programa necesita este ficheiro para funcionar.")
            return

    while True:
        print("=== XESTOR DE INVENTARIO CSV ===")
        print("1. Calcular valor total do inventario")
        print("2. Detectar produtos con stock baixo (<5)")
        print("3. Saír")

        opcion = input("Selecciona unha opción (1-3): ")

        if opcion == "1":
            valor_total_inventario()
        elif opcion == "2":
            existencias_baixas()
        elif opcion == "3":
            print("Saíndo...")
            break
        else:
            print("Opción non válida.\n")


if __name__ == "__main__":
    menu()