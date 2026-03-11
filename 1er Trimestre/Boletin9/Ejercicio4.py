# Boletín de ejercicios POO Python
# Todos los ejercicios (Libro, Consumo, Coche, Conta) con explicaciones detalladas de cada línea
# Y ahora CON CÓDIGO DE TESTING COMPLETO


# =========================
# EJERCICIO 4 – Clase Conta (banco)
# =========================

class Conta:
    def __init__(self, nome, numero, tipo, saldo=0):
        self.__nome = nome
        self.__numero = numero
        self.__tipo = tipo
        self.__saldo = saldo

    def get_nome(self):
        return self.__nome

    def get_numero(self):
        return self.__numero

    def get_tipo(self):
        return self.__tipo

    def get_saldo(self):
        return self.__saldo

    def set_nome(self, nome):
        self.__nome = nome

    def set_numero(self, numero):
        self.__numero = numero

    def set_tipo(self, tipo):
        self.__tipo = tipo

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def ingreso(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad

    def reintegro(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad

    def transferencia(self, contaDestino, importe):
        if 0 < importe <= self.__saldo:
            self.__saldo -= importe
            contaDestino.ingreso(importe)

