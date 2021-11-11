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
            movimiento = requests.get(movimiento1['move']['url'])
            movimiento = movimiento.json()
            movimiento1 = {'nombre': movimiento['name'], 'tipo': movimiento['type']['name'], 'categoria': movimiento['meta']
                           ['category']['name'], 'potencia': movimiento['power'], 'precision': movimiento['accuracy']}
            while(movimiento1['potencia'] == None):
                movimiento1 = choice(movimientos_bulbasaur)
                movimiento = requests.get(movimiento1['move']['url'])
                movimiento = movimiento.json()
                movimiento1 = {'nombre': movimiento['name'], 'tipo': movimiento['type']['name'], 'categoria': movimiento['meta']
                               ['category']['name'], 'potencia': movimiento['power'], 'precision': movimiento['accuracy']}
            movimiento2 = choice(movimientos_bulbasaur)
            movimiento = requests.get(movimiento2['move']['url'])
            movimiento = movimiento.json()
            movimiento2 = {'nombre': movimiento['name'], 'tipo': movimiento['type']['name'], 'categoria': movimiento['meta']
                           ['category']['name'], 'potencia': movimiento['power'], 'precision': movimiento['accuracy']}
            while(movimiento2['potencia'] == None):
                movimiento2 = choice(movimientos_bulbasaur)
                movimiento = requests.get(movimiento2['move']['url'])
                movimiento = movimiento.json()
                movimiento2 = {'nombre': movimiento['name'], 'tipo': movimiento['type']['name'], 'categoria': movimiento['meta']
                               ['category']['name'], 'potencia': movimiento['power'], 'precision': movimiento['accuracy']}
            tipos = []
            for i in pokemon['types']:
                tipos.append(
                    {'name': i['type']['name'], 'url': i['type']['url']})

            print('Su pokemon es: BULBASAUR')
            apodo = input('Ingrese apodo: ')
            print(f"Nivel-----------: {nivel} ")
            print(f"Tipos ----------:", end=" ")
            for x in tipos:
                print(x['name'], end=", ")
            print("\n")
            print(
                f"Movimientos-----: {movimiento1['nombre']}, {movimiento2['nombre']}")
            print('Datos de combate. ')
            print(f"Puntos de salud-: {ps} ")
            print(f"Ataque----------: {atq}")
            print(f"Defensa---------: {defe}")
            print(f"Ataque especial-: {atq_especial}")
            print(f"Defensa especial: {def_especial}")
            print(f"Velocidad-------: {velocidad}")
            input('Presione cualquier tecla para continuar...')
            self.pokeinicial = {'nombre': nombre, 'url': "https://pokeapi.co/api/v2/pokemon/1/", 'apodo': apodo, 'nivel': nivel, 'tipo': tipos, 'Salud': ps, 'Ataque': atq, 'Defensa': defe, 'Ataque especial': atq_especial,
                                'Defensa especial': def_especial, 'Velocidad': velocidad, 'experiencia': pokemon['base_experience'], 'movimientos': [movimiento1, movimiento2], 'niveles_subidos': 0}

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
            movimiento = requests.get(movimiento1['move']['url'])
            movimiento = movimiento.json()
            movimiento1 = {'nombre': movimiento['name'], 'tipo': movimiento['type']['name'], 'categoria': movimiento['meta']
                           ['category']['name'], 'potencia': movimiento['power'], 'precision': movimiento['accuracy']}
            while(movimiento1['potencia'] == None):
                movimiento1 = choice(movimientos_charmander)
                movimiento = requests.get(movimiento1['move']['url'])
                movimiento = movimiento.json()
                movimiento1 = {'nombre': movimiento['name'], 'tipo': movimiento['type']['name'], 'categoria': movimiento['meta']
                               ['category']['name'], 'potencia': movimiento['power'], 'precision': movimiento['accuracy']}
            movimiento2 = choice(movimientos_charmander)
            movimiento = requests.get(movimiento2['move']['url'])
            movimiento = movimiento.json()
            movimiento2 = {'nombre': movimiento['name'], 'tipo': movimiento['type']['name'], 'categoria': movimiento['meta']
                           ['category']['name'], 'potencia': movimiento['power'], 'precision': movimiento['accuracy']}
            while(movimiento2['potencia'] == None):
                movimiento2 = choice(movimientos_charmander)
                movimiento = requests.get(movimiento2['move']['url'])
                movimiento = movimiento.json()
                movimiento2 = {'nombre': movimiento['name'], 'tipo': movimiento['type']['name'], 'categoria': movimiento['meta']
                               ['category']['name'], 'potencia': movimiento['power'], 'precision': movimiento['accuracy']}
            tipos = []
            for i in pokemon['types']:
                tipos.append(
                    {'name': i['type']['name'], 'url': i['type']['url']})

            print('Su pokemon es: CHARMANDER')
            apodo = input('Ingrese apodo: ')
            print(f"Nivel-----------: {nivel} ")
            print(f"Tipos ----------:", end=" ")
            for x in tipos:
                print(x['name'], end=", ")
            print("\n")
            print(
                f"Movimientos-----: {movimiento1['nombre']}, {movimiento2['nombre']}")
            print('Datos de combate. ')
            print(f"Puntos de salud-: {ps} ")
            print(f"Ataque----------: {atq}")
            print(f"Defensa---------: {defe}")
            print(f"Ataque especial-: {atq_especial}")
            print(f"Defensa especial: {def_especial}")
            print(f"Velocidad-------: {velocidad}")
            input('Presione cualquier tecla para continuar...')
            self.pokeinicial = {'nombre': nombre, 'url': "https://pokeapi.co/api/v2/pokemon/4/", 'apodo': apodo, 'nivel': nivel, 'tipo': tipos, 'Salud': ps, 'Ataque': atq, 'Defensa': defe, 'Ataque especial': atq_especial,
                                'Defensa especial': def_especial, 'Velocidad': velocidad, 'experiencia': pokemon['base_experience'], 'movimientos': [movimiento1, movimiento2], 'niveles_subidos': 0}

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
            movimiento = requests.get(movimiento1['move']['url'])
            movimiento = movimiento.json()
            movimiento1 = {'nombre': movimiento['name'], 'tipo': movimiento['type']['name'], 'categoria': movimiento['meta']
                           ['category']['name'], 'potencia': movimiento['power'], 'precision': movimiento['accuracy']}
            while(movimiento1['potencia'] == None):
                movimiento1 = choice(movimientos_squirtle)
                movimiento = requests.get(movimiento1['move']['url'])
                movimiento = movimiento.json()
                movimiento1 = {'nombre': movimiento['name'], 'tipo': movimiento['type']['name'], 'categoria': movimiento['meta']
                               ['category']['name'], 'potencia': movimiento['power'], 'precision': movimiento['accuracy']}
            movimiento2 = choice(movimientos_squirtle)
            movimiento = requests.get(movimiento2['move']['url'])
            movimiento = movimiento.json()
            movimiento2 = {'nombre': movimiento['name'], 'tipo': movimiento['type']['name'], 'categoria': movimiento['meta']
                           ['category']['name'], 'potencia': movimiento['power'], 'precision': movimiento['accuracy']}
            while(movimiento2['potencia'] == None):
                movimiento2 = choice(movimientos_squirtle)
                movimiento = requests.get(movimiento2['move']['url'])
                movimiento = movimiento.json()
                movimiento2 = {'nombre': movimiento['name'], 'tipo': movimiento['type']['name'], 'categoria': movimiento['meta']
                               ['category']['name'], 'potencia': movimiento['power'], 'precision': movimiento['accuracy']}  
            tipos = []
            for i in pokemon['types']:
                tipos.append(
                    {'name': i['type']['name'], 'url': i['type']['url']})

            print('Su pokemon es: SQUIRTLE')
            apodo = input('Ingrese apodo: ')
            print(f"Nivel-----------: {nivel} ")
            print(f"Tipos ----------:", end=" ")
            for x in tipos:
                print(x['name'], end=", ")
            print("\n")
            print(
                f"Movimientos-----: {movimiento1['nombre']}, {movimiento2['nombre']}")
            print('Datos de combate. ')
            print(f"Puntos de salud-: {ps} ")
            print(f"Ataque----------: {atq}")
            print(f"Defensa---------: {defe}")
            print(f"Ataque especial-: {atq_especial}")
            print(f"Defensa especial: {def_especial}")
            print(f"Velocidad-------: {velocidad}")
            input('Presione cualquier tecla para continuar...')
            self.pokeinicial = {'nombre': nombre, 'url': "https://pokeapi.co/api/v2/pokemon/7/", 'apodo': apodo, 'nivel': nivel, 'tipo': tipos, 'Salud': ps, 'Ataque': atq, 'Defensa': defe, 'Ataque especial': atq_especial,
                                'Defensa especial': def_especial, 'Velocidad': velocidad, 'experiencia': pokemon['base_experience'], 'movimientos': [movimiento1, movimiento2], 'niveles_subidos': 0}

        return self.pokeinicial
    