# Autor: Brayan Sierra

# Clase que almacena e inicializa la estructura de datos de un equipo.

class equipo:

    def __init__(self,nombre):
        self.nombre = nombre
        self.victorias = 0
        self.empates = 0
        self.derrotas = 0
        self.golesAnotados = 0
        self.golesRecibidos = 0