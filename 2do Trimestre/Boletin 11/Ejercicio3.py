import pickle
import os
from datetime import datetime


class Tarefa:
    def __init__(self, nome, descricion, data, hora, duracion, estado="non feita"):
        self.nome = nome
        self.descricion = descricion
        self.data = data
        self.hora = hora
        self.duracion = duracion
        self.estado = estado

    def __str__(self):
        return f"{self.nome} | {self.data} {self.hora} | Dur: {self.duracion} | {self.estado} | {self.descricion}"


class XestorTarefas:
    def __init__(self, ficheiro="tarefas.dat"):
        self.ficheiro = ficheiro
        self.tarefas = []
        self.cargar_tarefas()

    def cargar_tarefas(self):
        """Carga as tarefas dende o ficheiro binario."""
        if os.path.exists(self.ficheiro):
            try:
                with open(self.ficheiro, 'rb') as f:
                    self.tarefas = pickle.load(f)
                print(f"Cargáronse {len(self.tarefas)} tarefas.")
            except:
                print("Erro ao cargar o ficheiro. Creando lista nova.")
                self.tarefas = []
        else:
            print("Non se atopou ficheiro. Creando lista nova.")
            self.tarefas = []

    def gardar_tarefas(self):
        """Garda as tarefas no ficheiro binario."""
        with open(self.ficheiro, 'wb') as f:
            pickle.dump(self.tarefas, f)
        print("Tarefas gardadas correctamente.")

    def engadir_tarefa(self):
        """Engade unha nova tarefa."""
        print("\n--- NOVA TAREFA ---")
        nome = input("Nome da tarefa: ")
        descricion = input("Descrición: ")
        data = input("Data (dd/mm/aaaa): ")
        hora = input("Hora (hh:mm): ")
        duracion = input("Duración (minutos): ")

        tarefa = Tarefa(nome, descricion, data, hora, duracion)
        self.tarefas.append(tarefa)
        print("Tarefa engadida correctamente.")
        self.gardar_tarefas()

    def borrar_tarefa(self):
        """Borra unha tarefa."""
        self.listar_tarefas()
        if not self.tarefas:
            return

        try:
            indice = int(input("Número da tarefa a borrar: ")) - 1
            if 0 <= indice < len(self.tarefas):
                tarefa = self.tarefas.pop(indice)
                print(f"Tarefa '{tarefa.nome}' borrada.")
                self.gardar_tarefas()
            else:
                print("Índice non válido.")
        except ValueError:
            print("Por favor, introduce un número válido.")

    def modificar_tarefa(self):
        """Modifica unha tarefa existente."""
        self.listar_tarefas()
        if not self.tarefas:
            return

        try:
            indice = int(input("Número da tarefa a modificar: ")) - 1
            if 0 <= indice < len(self.tarefas):
                tarefa = self.tarefas[indice]
                print(f"Modificando: {tarefa}")

                nome = input(f"Nome ({tarefa.nome}): ") or tarefa.nome
                descricion = input(f"Descrición ({tarefa.descricion}): ") or tarefa.descricion
                data = input(f"Data ({tarefa.data}): ") or tarefa.data
                hora = input(f"Hora ({tarefa.hora}): ") or tarefa.hora
                duracion = input(f"Duración ({tarefa.duracion}): ") or tarefa.duracion
                estado = input(f"Estado ({tarefa.estado}): ") or tarefa.estado

                tarefa.nome = nome
                tarefa.descricion = descricion
                tarefa.data = data
                tarefa.hora = hora
                tarefa.duracion = duracion
                tarefa.estado = estado

                print("Tarefa modificada.")
                self.gardar_tarefas()
            else:
                print("Índice non válido.")
        except ValueError:
            print("Por favor, introduce un número válido.")

    def listar_tarefas(self):
        """Lista todas as tarefas."""
        if not self.tarefas:
            print("Non hai tarefas.")
            return

        print("\n=== LISTA DE TAREFAS ===")
        for i, tarefa in enumerate(self.tarefas, 1):
            print(f"{i}. {tarefa}")
        print()

    def menu(self):
        """Menú principal do xestor de tarefas."""
        while True:
            print("=== XESTOR DE TAREFAS ===")
            print("1. Engadir tarefa")
            print("2. Borrar tarefa")
            print("3. Modificar tarefa")
            print("4. Listar tarefas")
            print("5. Saír")

            opcion = input("Selecciona unha opción (1-5): ")

            if opcion == "1":
                self.engadir_tarefa()
            elif opcion == "2":
                self.borrar_tarefa()
            elif opcion == "3":
                self.modificar_tarefa()
            elif opcion == "4":
                self.listar_tarefas()
            elif opcion == "5":
                print("Saíndo...")
                break
            else:
                print("Opción non válida.\n")


if __name__ == "__main__":
    xestor = XestorTarefas()
    xestor.menu()