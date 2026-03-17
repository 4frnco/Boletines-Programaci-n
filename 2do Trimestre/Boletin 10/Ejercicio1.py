class DniNonValido(Exception):
    """Excepción personalizada para DNI no válido."""
    pass

class LicenzaNonValida(Exception):
    """Excepción personalizada para licencia no válida."""
    pass

class Persoa:
    def __init__(self, nome, dni):
        self.nome = nome
        self.setDni(dni)

    def getDni(self):
        return self._dni

    def setDni(self, novo_dni):
        if len(novo_dni) != 9:
            raise DniNonValido("O DNI debe ter 9 caracteres (8 números e 1 letra).")
        numeros = novo_dni[:8]
        letra = novo_dni[8]
        if not numeros.isdigit() or not letra.isalpha() or not letra.isupper():
            raise DniNonValido("Formato de DNI incorrecto. Debe ser 8 números e unha letra maiúscula.")
        self._dni = novo_dni

    def getNome(self):
        return self._nome

    def setNome(self, novo_nome):
        self._nome = novo_nome

    nome = property(getNome, setNome)
    dni = property(getDni, setDni)

class Deportista(Persoa):
    def __init__(self, nome, dni, licenza):
        super().__init__(nome, dni)
        self.setLicenza(licenza)

    def getLicenza(self):
        return self._licenza

    def setLicenza(self, nova_licenza):
        if len(nova_licenza) != 13:
            raise LicenzaNonValida("A licenza debe ter 13 caracteres (aaaa ddd nnnnnn).")
        ano = nova_licenza[:4]
        deporte = nova_licenza[4:7]
        numero = nova_licenza[7:]

        if not ano.isdigit():
            raise LicenzaNonValida("Os primeiros 4 caracteres deben ser números (ano).")
        if not deporte.isalpha() or not deporte.islower():
            raise LicenzaNonValida("Os 3 caracteres seguintes deben ser letras minúsculas (abreviatura do deporte).")
        if not numero.isdigit() or len(numero) != 6:
            raise LicenzaNonValida("Os últimos 6 caracteres deben ser números.")

        self._licenza = nova_licenza

    licenza = property(getLicenza, setLicenza)


if __name__ == "__main__":
    try:
        p = Persoa("Ana", "12345678Z")
        print("Persoa creada:", p.nome, p.dni)
    except DniNonValido as e:
        print("Erro ao crear a persoa:", e)

    try:
        d = Deportista("Carlos", "87654321X", "2024fut123456")
        print("Deportista creado:", d.nome, d.dni, d.licenza)
    except (DniNonValido, LicenzaNonValida) as e:
        print("Erro ao crear o deportista:", e)