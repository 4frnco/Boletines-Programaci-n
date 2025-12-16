# Boletín de ejercicios POO Python
# Todos los ejercicios (Libro, Consumo, Coche, Conta) con explicaciones detalladas de cada línea
# Y ahora CON CÓDIGO DE TESTING COMPLETO

# =========================
# EJERCICIO 2 – Clase Consumo
# =========================

class Consumo:
    def __init__(self, km=0, litros=0, vMed=0, pGas=0):
        self.km = km
        self.litros = litros
        self.vMed = vMed
        self.pGas = pGas

    def getTempo(self):
        if self.vMed == 0:
            return 0
        return self.km / self.vMed

    def consumoMedio(self):
        if self.km == 0:
            return 0
        return (self.litros / self.km) * 100

    def consumoEuros(self):
        return self.consumoMedio() * self.pGas

    def setKms(self, km):
        self.km = km

    def setLitros(self, litros):
        self.litros = litros

    def setvMed(self, vMed):
        self.vMed = vMed

    def setPGas(self, pGas):
        self.pGas = pGas
