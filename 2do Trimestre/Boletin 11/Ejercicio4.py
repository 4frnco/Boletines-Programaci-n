import pickle
import os


class Cliente:
    def __init__(self, id_cliente, nome, telefono):
        self.id = id_cliente
        self.nome = nome
        self.telefono = telefono

    def __str__(self):
        return f"ID: {self.id} | {self.nome} | Tel: {self.telefono}"


class XestorClientes:
    def __init__(self, ficheiro="clientes.dat"):
        self.ficheiro = ficheiro
        self.clientes = []
        self.cargar_clientes()

    def cargar_clientes(self):
        """Carga os clientes dende o ficheiro binario."""
        if os.path.exists(self.ficheiro):
            try:
                with open(self.ficheiro, 'rb') as f:
                    self.clientes = pickle.load(f)
                print(f"Cargáronse {len(self.clientes)} clientes.")
            except:
                print("Erro ao cargar o ficheiro. Creando lista nova.")
                self.clientes = []

    def gardar_clientes(self):
        """Garda os clientes no ficheiro binario."""
        with open(self.ficheiro, 'wb') as f:
            pickle.dump(self.clientes, f)
        print("Clientes gardados correctamente.")

    def engadir_cliente(self):
        """Engade un novo cliente."""
        print("\n--- NOVO CLIENTE ---")
        id_cliente = input("ID do cliente: ")

        # Comprobar se o ID xa existe
        for cliente in self.clientes:
            if cliente.id == id_cliente:
                print("Erro: Xa existe un cliente con ese ID.")
                return

        nome = input("Nome: ")
        telefono = input("Teléfono: ")

        cliente = Cliente(id_cliente, nome, telefono)
        self.clientes.append(cliente)
        print("Cliente engadido correctamente.")

    def modificar_cliente(self):
        """Modifica os datos dun cliente."""
        id_cliente = input("ID do cliente a modificar: ")

        for cliente in self.clientes:
            if cliente.id == id_cliente:
                print(f"Datos actuais: {cliente}")
                nome = input(f"Novo nome (deixar baleiro para manter '{cliente.nome}'): ")
                telefono = input(f"Novo teléfono (deixar baleiro para manter '{cliente.telefono}'): ")

                if nome:
                    cliente.nome = nome
                if telefono:
                    cliente.telefono = telefono

                print("Cliente modificado correctamente.")
                return

        print("Non se atopou un cliente con ese ID.")

    def baixa_cliente(self):
        """Dá de baixa un cliente."""
        id_cliente = input("ID do cliente a dar de baixa: ")

        for i, cliente in enumerate(self.clientes):
            if cliente.id == id_cliente:
                confirmacion = input(f"Seguro que queres eliminar a {cliente.nome}? (s/n): ")
                if confirmacion.lower() == 's':
                    self.clientes.pop(i)
                    print("Cliente eliminado.")
                return

        print("Non se atopou un cliente con ese ID.")

    def listar_clientes(self):
        """Lista todos os clientes."""
        if not self.clientes:
            print("Non hai clientes.")
            return

        print("\n=== LISTA DE CLIENTES ===")
        for cliente in self.clientes:
            print(cliente)
        print()

    def menu(self):
        """Menú principal do xestor de clientes."""
        try:
            while True:
                print("=== XESTOR DE CLIENTES ===")
                print("1. Engadir novo cliente")
                print("2. Modificar datos")
                print("3. Dar de baixa cliente")
                print("4. Listar clientes")
                print("5. Saír")

                opcion = input("Selecciona unha opción (1-5): ")

                if opcion == "1":
                    self.engadir_cliente()
                elif opcion == "2":
                    self.modificar_cliente()
                elif opcion == "3":
                    self.baixa_cliente()
                elif opcion == "4":
                    self.listar_clientes()
                elif opcion == "5":
                    print("Gardando e saíndo...")
                    self.gardar_clientes()
                    break
                else:
                    print("Opción non válida.\n")
        finally:
            # Gardar ao saír por calquera motivo
            self.gardar_clientes()


if __name__ == "__main__":
    xestor = XestorClientes()
    xestor.menu()