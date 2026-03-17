class FormatoDataError(Exception):
    """Excepción personalizada para formato de data incorrecto."""
    pass

class Data:
    def __init__(self, dia, mes, ano):
        self.setDia(dia)
        self.setMes(mes)
        self.setAno(ano)

    def getDia(self):
        return self._dia

    def setDia(self, dia):
        if hasattr(self, '_mes') and hasattr(self, '_ano'):
            self._validarData(dia, self._mes, self._ano)
        self._dia = dia

    def getMes(self):
        return self._mes

    def setMes(self, mes):
        if hasattr(self, '_dia') and hasattr(self, '_ano'):
            self._validarData(self._dia, mes, self._ano)
        self._mes = mes

    def getAno(self):
        return self._ano

    def setAno(self, ano):
        if hasattr(self, '_dia') and hasattr(self, '_mes'):
            self._validarData(self._dia, self._mes, ano)
        self._ano = ano

    def _eBisiesto(self, ano):
        """Comprueba si un año es bisiesto."""
        return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

    def _diasNoMes(self, mes, ano):
        """Devuelve el número de días de un mes dado."""
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif mes in [4, 6, 9, 11]:
            return 30
        elif mes == 2:
            return 29 if self._eBisiesto(ano) else 28
        else:
            return 0  # Mes no válido

    def _validarData(self, dia, mes, ano):
        """Valida que la combinación día/mes/año sea correcta."""
        if ano < 1970 or ano > 2999:
            raise FormatoDataError(f"Ano {ano} fóra do rango (1970-2999).")
        if mes < 1 or mes > 12:
            raise FormatoDataError(f"Mes {mes} non válido (debe ser 1-12).")
        dias_max = self._diasNoMes(mes, ano)
        if dia < 1 or dia > dias_max:
            raise FormatoDataError(f"Día {dia} non válido para o mes {mes} do ano {ano} (máx {dias_max}).")

    def incrementarDia(self):
        """Incrementa la fecha en un día."""
        dias_max = self._diasNoMes(self._mes, self._ano)
        if self._dia < dias_max:
            self._dia += 1
        else:
            self._dia = 1
            self.incrementarMes()

    def incrementarMes(self):
        """Incrementa la fecha en un mes."""
        if self._mes < 12:
            self._mes += 1
        else:
            self._mes = 1
            self.incrementarAno()
        dias_max = self._diasNoMes(self._mes, self._ano)
        if self._dia > dias_max:
            self._dia = dias_max

    def incrementarAno(self):
        """Incrementa la fecha en un año."""
        if self._ano < 2999:
            self._ano += 1
        else:
            raise FormatoDataError("Non se pode incrementar máis aló do ano 2999.")
        if self._mes == 2 and self._dia == 29 and not self._eBisiesto(self._ano):
            self._dia = 28

    def dataIgual(self, outraData):
        """Compara dos fechas."""
        return (self._dia == outraData._dia and
                self._mes == outraData._mes and
                self._ano == outraData._ano)

    def mostrarData(self):
        """Muestra la fecha en formato dd/mm/aaaa."""
        print(f"{self._dia:02d}/{self._mes:02d}/{self._ano}")


    dia = property(getDia, setDia)
    mes = property(getMes, setMes)
    ano = property(getAno, setAno)


if __name__ == "__main__":
    try:
        d = Data(29, 2, 2024)  # Válida (bisiesto)
        d.mostrarData()
        d.incrementarDia()
        d.mostrarData()  # 01/03/2024
    except FormatoDataError as e:
        print("Erro de data:", e)

    try:
        d2 = Data(31, 4, 2023)  # Inválida (abril tiene 30 días)
    except FormatoDataError as e:
        print("Erro de data:", e)