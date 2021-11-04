# Listado de pokemon del jugador

class Pokedex:

    def __init__(self) -> None:
        self.pokedex = []
        self.indice = 1

    def inicial(self, inicial):
        self.pokedex.append(
            {'numero': self.indice, 'nombre': inicial['nombre'], 'estado': "Pokemon Inicial"})
        self.indice += 1

    def nuevo(self, pokemon, capturado):
        if capturado == True:
            self.pokedex.append(
                {'numero': self.indice, 'nombre': pokemon['nombre'], 'estado': "Capturado por Entrenador"})
        elif capturado == False:
            self.pokedex.append(
                {'numero': self.indice, 'nombre': pokemon['nombre'], 'estado': "No Capturado"})
        else:
            pass
        self.indice += 1
