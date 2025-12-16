# Boletín de ejercicios POO Python
# Todos los ejercicios (Libro, Consumo, Coche, Conta) con explicaciones detalladas de cada línea
# Y ahora CON CÓDIGO DE TESTING COMPLETO

# =========================
# EJERCICIO 3 – Clase Coche
# =========================

class Coche:
    def __init__(self):
        self.velocidade = 0

    def getVelocidade(self):
        return self.velocidade

    def acelerar(self, valor):
        self.velocidade += valor

    def frenar(self, menos):
        self.velocidade -= menos
        if self.velocidade < 0:
            self.velocidade = 0

