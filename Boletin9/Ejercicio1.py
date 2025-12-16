# Boletín de ejercicios POO Python
# Todos los ejercicios (Libro, Consumo, Coche, Conta) con explicaciones detalladas de cada línea
# Y ahora CON CÓDIGO DE TESTING COMPLETO

# =========================
# EJERCICIO 1 – Clase Libro
# =========================

class Libro:
    def __init__(self, titulo, autor, ano, numPaginas, valoracion):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
        self.__numPaginas = numPaginas
        self.__valoracion = valoracion

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_ano(self):
        return self.__ano

    def get_numPaginas(self):
        return self.__numPaginas

    def get_valoracion(self):
        return self.__valoracion

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_autor(self, autor):
        self.__autor = autor

    def set_ano(self, ano):
        self.__ano = ano

    def set_numPaginas(self, numPaginas):
        self.__numPaginas = numPaginas

    def set_valoracion(self, valoracion):
        self.__valoracion = valoracion

    titulo = property(get_titulo, set_titulo)
    autor = property(get_autor, set_autor)
    ano = property(get_ano, set_ano)
    numPaginas = property(get_numPaginas, set_numPaginas)
    valoracion = property(get_valoracion, set_valoracion)

    def amosarLibro(self):
        return f"Título: {self.__titulo}, Autor: {self.__autor}, Año: {self.__ano}, Páginas: {self.__numPaginas}, Valoración: {self.__valoracion}"


