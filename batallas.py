from random import randint
from random import choice

class Batallas:
    def __init__(self, seleccion):
        self.seleccion = seleccion

    def pokemon_salvaje(self, nivelpokeusuario):
        nivel = randint(nivelpokeusuario - 5, nivelpokeusuario + 5)
        # pokemones = consultar API para eleccion del pokemon
        pokemon = choice(pokemones)
        vi = randint(1, 20)
            #EB = sacar de informacion de la api
            #ataque = sacar de informacion de la api
            #defensa = sacar de informacion de la api
            #vel = sacar de informacion de la api
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
            movimientos = #sacar de la api
            movimiento1 = choice(movimientos)
            movimiento2 = choice(movimientos)
            movimiento3 = choice(movimientos)
            movimiento4 = choice(movimientos)
        self.pokesalvaje = ['nombre': pokemon.nombre; 'nivel': nivel;] #guardar especificaciones a una variable local para consultar durante batalla

    def atacar():
        pass

    def capturar():
        pass

    def curar():
        pass

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

