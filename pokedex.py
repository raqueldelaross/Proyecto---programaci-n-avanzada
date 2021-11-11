# Listado de pokemon del jugador
import os


class Pokedex:

    def __init__(self, inicial) -> None:
        self.pokedex = []
        self.indice = 1
        self.inicial(inicial)

    def inicial(self, inicial):
        self.pokedex.append(
            {'numero': self.indice, 'nombre': inicial['nombre'], 'estado': "Pokemon Inicial"})
        self.indice += 1

    def nuevo(self, pokemon, capturado):
        for x in self.pokedex:
            if(pokemon['nombre'] == x['nombre']):
                existe = True
                break
            else:
                existe = False
        if (existe == False):
            if capturado == True:
                self.pokedex.append(
                {'numero': self.indice, 'nombre': pokemon['nombre'], 'estado': "Capturado por Entrenador"})
            elif capturado == False:
                self.pokedex.append(
                    {'numero': self.indice, 'nombre': pokemon['nombre'], 'estado': "No Capturado"})
            else:
                pass
            self.indice += 1
        elif existe == True:
            if capturado == True:
                for x in self.pokedex:
                    if(pokemon['nombre'] == x['nombre']):
                        x['estado'] = "Capturado por Entrenador"

    def mostrar(self):
        os.system("cls")
        print("----POKEDEX----")
        for x in self.pokedex:
            print(f"{x['numero']}. {x['nombre']} ---- {x['estado']}")
        os.system("pause")
