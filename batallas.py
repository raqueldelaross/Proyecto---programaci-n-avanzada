from random import choice, randint
from tienda import Tienda
import requests

class Batallas:
    def __init__(self, seleccion):
        self.seleccion = seleccion

    def pokemon_salvaje(self, nivelpokeusuario):
        nivel = randint(nivelpokeusuario - 5, nivelpokeusuario + 5)
        opcion = randint(1, 1118)
        pokemones = requests.get(f"https://pokeapi.co/api/v2/pokemon/{opcion}/")
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
        movimientos = pokemon['moves']
        movimiento1 = choice(movimientos)
        movimiento2 = choice(movimientos)
        movimiento3 = choice(movimientos)
        movimiento4 = choice(movimientos)
        self.pokesalvaje = {'nombre': pokemon['name'], 'nivel': nivel, 'tipo': pokemon['types'], 'Salud': ps, 'Ataque': atq, 'Defensa': defe, 'Ataque especial': atq_especial, 'Defensa especial': def_especial, 'Velociadad': velocidad} 
        #guardar especificaciones a una variable local para consultar durante batalla

    def atacar():
        pass

    def capturar():
        pass

    def curar():
        print('Utilizar un objeto curativo')
        print('OBJETOS CURATIVOS:')
        print(f"1. Posión:       {posion}")
        print(f"2. Super-posión: {superposion}")
        print(f"3. Hiper-posión: {hiperposion}")
        print(f"4. Restauración: {restaurar}")
        objeto = int(input('Ingrese la opción del objeto curativo que desee usar: '))
        if objeto == 1:
            if posion > 0:
                vida = vida  + 20
                print('Se ha sumado 20 puntos de vida a su pokémon')
            else:
                print('Error, no tiene el objeto curativo seleccionado')
                os.system("pause")  
                continue
        elif objeto == 2:
            if superposion > 0:
                vida = vida  + 50
                print('Se ha sumado 50 puntos de vida a su pokémon')
            else:   
                print('Error, no tiene el objeto curativo seleccionado')
                os.system("pause")  
                continue
        elif objeto == 3:
            if hiperposion > 0:
                vida = vida  + 200
                print('Se ha sumado 200 puntos de vida a su pokémon')
            else:   
                print('Error, no tiene el objeto curativo seleccionado')
                os.system("pause")  
                continue
        elif objeto == 4:
            if restaurar > 0:
                vida = 3000
                print('Se ha restaurado la vida de su pokémon a 300 puntos de vida')
            else:       
                print('Error, no tiene el objeto curativo seleccionado')
                os.system("pause")  
                continue
        else:
            print('ERROR')

    def huir():
        pass

    def ganar():
        pass

    def perder():
        pass

    def __str__():
        pass

    def batalla(self, usuario):
        self.pokemon_salvaje() #generar estadisticas del pokemon salvaje
        #pokemon del usuario
        if self.pokemon.speed > usuario.speed: #comparacion de la velocidad para determinar quien va primero
            turno = 'salvaje'
        else:
            turno = 'usuario'
        x = 2
        while x > 0:
            if(turno == 'usuario'):
                pass
            else:
                pass
        pass

