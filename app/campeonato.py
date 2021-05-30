# Autor: Brayan Sierra

# Clase que representá la lógica de la aplicación.
 
# Se importan las clases que contienen la estructura de equipos y encuentros
from equipo import *
from encuentro import *

# Paquete para generar los encuentros entre equipos
import itertools

class campeonato:
    # Arreglos
    def __init__(self):
        self.equipos = []
        self.emparejamientos = []
        self.resEncuentros = []

    # Método para registrar equipos
    def registrarEquipo(self, nombre):
        self.equipos.append(equipo(nombre))

    # Método para generar los emparejamientos (en total 6)
    def crearEncuentros(self):
        self.emparejamientos = list(itertools.combinations(self.equipos,2))

    # Método para registrar encuentro entre 2 equipos, actualizando valores
    def registrarEncuentro(self, pares, goles1,goles2):
        pares[0].golesAnotados += goles1
        pares[0].golesRecibidos += goles2
        pares[1].golesAnotados += goles2
        pares[1].golesRecibidos += goles1
        if goles1==goles2:
            pares[0].empates +=1
            pares[1].empates +=1
        elif goles1 > goles2:
            pares[0].victorias +=1
            pares[1].derrotas +=1
        else:
            pares[1].victorias +=1
            pares[0].derrotas +=1

        # Se almacena el resultado en el arreglo resEncuentros
        encuentroloc = encuentro(pares[0],pares[1],goles1,goles2) 
        self.resEncuentros.append(encuentroloc)


