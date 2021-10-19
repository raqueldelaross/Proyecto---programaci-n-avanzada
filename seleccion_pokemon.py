from random import randint
from random import choice

class Seleccion_pokemon:
    def __init__(self, pokemon):
        self.pokemon = pokemon

    def inicial(self):
        nivel = 5
        if self.pokemon == 1:
            #puntos de salud
            vi = randint(1, 20)
            EB = 45
            ataque = 49
            defensa = 49
            vel = 45
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
            movimientos_bulbasaur = ['Scratch', 'Growl', 'Leech seed', 'Vine whip', 'Posion powder', 'Sleep powder', 'Take down', 'Razor leaf', 'Sweet scent', 'Growth', 'Double-edge', 'Worry seed', 'Synthesis', 'Seed Bomb']
            movimiento1 = choice(movimientos_bulbasaur)
            movimiento2 = choice(movimientos_bulbasaur)

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
            #puntos de salud
            vi = randint(1, 20)
            EB = 39
            ataque = 52
            defensa = 43
            vel = 65
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
            movimientos_charmander = ['Scratch', 'Growl', 'Ember', 'Smokescreen', 'Dragon rage', 'Scary face', 'Fire fang', 'Flame brust', 'Slash', 'Flamethrower', 'Fire spin', 'Inferno']
            movimiento1 = choice(movimientos_charmander)
            movimiento2 = choice(movimientos_charmander)

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
            #puntos de salud
            vi = randint(1, 20)
            EB = 44
            ataque = 48
            defensa = 65
            vel = 43
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
            movimientos_squirtle = ['Trackle', 'Tail whip', 'Water Gun', 'Whitdraw', 'Bubble', 'Bite', 'Rapid spin', 'Protect', 'Water pulse', 'Aqua tail', 'Skull bash', 'Iron defense', 'Rain dance', 'Hydro pump']
            movimiento1 = choice(movimientos_squirtle)
            movimiento2 = choice(movimientos_squirtle)            

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
