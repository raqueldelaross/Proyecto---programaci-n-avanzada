import os


class Equipo:
    def __init__(self, inicial):
        self.listapokemon = []
        self.pokemon_inicial = inicial
        self.nuevo_pokemon(inicial)

    def progreso(self):
        i = 1
        print("Tu equipo de Pokemón ---------")
        for pokemon in self.listapokemon:
            print(f"{i} -- {pokemon['nombre']}")
        seleccion = int(
            input("Eliga el pokemón del que desea ver el progreso.. "))
        os.system("cls")
        visualizar = self.listapokemon[seleccion-1]
        self.mostrar(visualizar)

    def mostrar(self, visualizar):
        os.system("cls")
        print('-------- DATOS DEL POKEMON --------')
        print(
            f"Nombre ---------: {visualizar['nombre']} ** APODO -----: {visualizar['apodo']}")
        print(f"Nivel-----------: {visualizar['nivel']} ")
        print(f"Tipos ----------:", end=" ")
        for x in visualizar['tipo']:
            print(x['name'], end=", ")
        print("")
        print(f"Movimientos-----:", end=" ")
        for x in visualizar['movimientos']:
            print(x, end=", ")
        print("")
        print(f"Experiencia ----: {visualizar['experiencia']}")
        print('-------- DATOS DE COMBATE --------')
        print(f"Puntos de salud-: {visualizar['Salud']} ")
        print(f"Ataque----------: {visualizar['Ataque']}")
        print(f"Defensa---------: {visualizar['Defensa']}")
        print(f"Ataque especial-: {visualizar['Ataque especial']}")
        print(f"Defensa especial: {visualizar['Defensa especial']}")
        print(f"Velocidad-------: {visualizar['Velocidad']}")
        input('Presione cualquier tecla para continuar...')
        os.system("cls")

    def nuevo_pokemon(self, pokemon):
        self.listapokemon.append(pokemon)
        print(self.listapokemon)