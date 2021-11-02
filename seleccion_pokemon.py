from random import randint
from random import choice
import requests


class Seleccion_pokemon:
    def __init__(self, pokemon):
        self.pokemon = pokemon
        self.pokeinicial = {}
    


    def inicial(self):
        nivel = 5
        if self.pokemon == 1:
            nombre = "Bulbasaur"
            #puntos de salud
            vi = randint(1, 20)
            pokemones = requests.get(f"https://pokeapi.co/api/v2/pokemon/1/")
            pokemon = pokemones.json()
            vi = randint(1, 20)
            EB = pokemon['stats'][0]['base_stat']
            ataque = pokemon['stats'][1]['base_stat']
            defensa = pokemon['stats'][2]['base_stat']
            vel = pokemon['stats'][5]['base_stat']
            ps = ((vi + 2 * EB)* (nivel/100))+10+nivel
            #puntos de ataque
            vi2 = randint(1, 20)
            atq = ((vi2 + 2 * ataque)*(nivel/100))+5
            #puntos de defensa
            vi3 = randint(1, 20)
            defe = ((vi3 + 2 * defensa)*(nivel/100))+5
            #puntos de ataque especial
            vi4 = randint(1, 20)
            atq_especial = ((vi4 + 2 * ataque)*(nivel/100))+5
            #puntos de defensa especial
            vi5 = randint(1, 20)
            def_especial = ((vi5 + 2 * defensa)*(nivel/100))+5
            #velocidad
            vi6 = randint(1, 20)
            velocidad = ((vi6 + 2 * vel)*(nivel/100))+5
            # movimientos de BULBASAUR
            movimientos_bulbasaur = pokemon['moves']
            movimiento1 = choice(movimientos_bulbasaur)
            movimiento1 = movimiento1['move']['name']
            movimiento2 = choice(movimientos_bulbasaur)
            movimiento2 = movimiento2['move']['name']
            tipos = pokemon['types']  

            print('Su pokemon es: BULBASAUR')
            apodo = input('Ingrese apodo: ')
            print(f"Nivel-----------: {nivel} ")
            print(f"Movimientos-----: {movimiento1}, {movimiento2}")
            print('Datos de combate. ')
            print(f"Puntos de salud-: {ps} ")
            print(f"Ataque----------: {atq}")
            print(f"Defensa---------: {defe}")
            print(f"Ataque especial-: {atq_especial}")
            print(f"Defensa especial: {def_especial}")
            print(f"Velocidad-------: {velocidad}")
            input('Presione cualquier tecla para continuar...')

        elif self.pokemon == 2:
            nombre = "Charmander"
            #puntos de salud
            vi = randint(1, 20)
            pokemones = requests.get(f"https://pokeapi.co/api/v2/pokemon/4/")
            pokemon = pokemones.json()
            vi = randint(1, 20)
            EB = pokemon['stats'][0]['base_stat']
            ataque = pokemon['stats'][1]['base_stat']
            defensa = pokemon['stats'][2]['base_stat']
            vel = pokemon['stats'][5]['base_stat']
            ps = ((vi + 2 * EB)* (nivel/100))+10+nivel
            #puntos de ataque
            vi2 = randint(1, 20)
            atq = ((vi2 + 2 * ataque)*(nivel/100))+5
            #puntos de defensa
            vi3 = randint(1, 20)
            defe = ((vi3 + 2 * defensa)*(nivel/100))+5
            #puntos de ataque especial
            vi4 = randint(1, 20)
            atq_especial = ((vi4 + 2 * ataque)*(nivel/100))+5
            #puntos de defensa especial
            vi5 = randint(1, 20)
            def_especial = ((vi5 + 2 * defensa)*(nivel/100))+5
            #velocidad
            vi6 = randint(1, 20)
            velocidad = ((vi6 + 2 * vel)*(nivel/100))+5
            # movimientos de CHARMANDER
            movimientos_charmander = pokemon['moves']
            movimiento1 = choice(movimientos_charmander)
            movimiento1 = movimiento1['move']['name']
            movimiento2 = choice(movimientos_charmander)
            movimiento2 = movimiento2['move']['name']
            tipos = pokemon['types']  

            print('Su pokemon es: CHARMANDER')
            apodo = input('Ingrese apodo: ')
            print(f"Nivel-----------: {nivel} ")
            print(f"Movimientos-----: {movimiento1}, {movimiento2}")
            print('Datos de combate. ')
            print(f"Puntos de salud-: {ps} ")
            print(f"Ataque----------: {atq}")
            print(f"Defensa---------: {defe}")
            print(f"Ataque especial-: {atq_especial}")
            print(f"Defensa especial: {def_especial}")
            print(f"Velocidad-------: {velocidad}")
            input('Presione cualquier tecla para continuar...')

        elif self.pokemon == 3:
            nombre = "Squirtle"
            #puntos de salud
            vi = randint(1, 20)
            pokemones = requests.get(f"https://pokeapi.co/api/v2/pokemon/7/")
            pokemon = pokemones.json()
            vi = randint(1, 20)
            EB = pokemon['stats'][0]['base_stat']
            ataque = pokemon['stats'][1]['base_stat']
            defensa = pokemon['stats'][2]['base_stat']
            vel = pokemon['stats'][5]['base_stat']
            ps = ((vi + 2 * EB)* (nivel/100))+10+nivel
            #puntos de ataque
            vi2 = randint(1, 20)
            atq = ((vi2 + 2 * ataque)*(nivel/100))+5
            #puntos de defensa
            vi3 = randint(1, 20)
            defe = ((vi3 + 2 * defensa)*(nivel/100))+5
            #puntos de ataque especial
            vi4 = randint(1, 20)
            atq_especial = ((vi4 + 2 * ataque)*(nivel/100))+5
            #puntos de defensa especial
            vi5 = randint(1, 20)
            def_especial = ((vi5 + 2 * defensa)*(nivel/100))+5
            #velocidad
            vi6 = randint(1, 20)
            velocidad = ((vi6 + 2 * vel)*(nivel/100))+5
            # movimientos de SQUIRTLE
            movimientos_squirtle = pokemon['moves']
            movimiento1 = choice(movimientos_squirtle)
            movimiento1 = movimiento1['move']['name']
            movimiento2 = choice(movimientos_squirtle)
            movimiento2 = movimiento2['move']['name']  
            tipos = pokemon['types']          

            print('Su pokemon es: SQUIRTLE')
            apodo = input('Ingrese apodo: ')
            print(f"Nivel-----------: {nivel} ")
            print(f"Movimientos-----: {movimiento1}, {movimiento2}")
            print('Datos de combate. ')
            print(f"Puntos de salud-: {ps} ")
            print(f"Ataque----------: {atq}")
            print(f"Defensa---------: {defe}")
            print(f"Ataque especial-: {atq_especial}")
            print(f"Defensa especial: {def_especial}")
            print(f"Velocidad-------: {velocidad}")
            input('Presione cualquier tecla para continuar...')
        
        else:
            print('Esta opcion no esta disponible')

        self.pokeinicial = {'nombre': nombre, 'nivel': nivel, 'tipo': tipos, 'Salud': ps, 'Ataque': atq, 'Defensa': defe, 'Ataque especial': atq_especial, 'Defensa especial': def_especial, 'Velociadad': velocidad, 'experiencia': pokemon['base_experience'], 'movimientos': [movimiento1, movimiento2]} 
    
    def datosinicial(self):
        return self.pokeinicial
