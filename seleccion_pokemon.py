import os
from random import randint #librearia para generar numeros aleatorios
clear = lambda: os.system('cls') #limpiar pantalla

def inicial(poke_incial):
        nivel = 5
        if poke_inicial == 1:
            #DATOS
            EB = 45
            ataque = 49
            defensa = 49
            a_especial = 65 #valor ataque especial
            d_especial = 65 #valor defensa especial
            vel = 45
            #puntos de salud
            vi = randint(1, 45)
            ps = ((vi + 2 * EB)* (nivel/100))+10+nivel
            #puntos de ataque
            vi2 = randint(1, 49)
            atq = ((vi2 + 2 * ataque)*(nivel/100))+5
            #puntos de defensa
            vi3 = randint(1, 49)
            defe = ((vi3 + 2 * defensa)*(nivel/100))+5
            #puntos de ataque especial
            vi4 = randint(1, 65)
            atq_especial = ((vi4 + 2 * ataque)*(nivel/100))+5
            #puntos de defensa especial
            vi5 = randint(1, 65)
            def_especial = ((vi5 + 2 * defensa)*(nivel/100))+5
            #velocidad
            vi6 = randint(1, 45)
            velocidad = ((vi6 + 2 * vel)*(nivel/100))+5
            

            print('Su pokemon es: BULBASAUR')
            apodo = input('Ingrese apodo: ')
            print(f"Nivel-----------: {nivel} ")
            print('Movimientos-----: ')
            print('<< Datos de combate >>')
            print(f"Puntos de salud-: {ps} ")
            print(f"Ataque----------: {atq}")
            print(f"Defensa---------: {defe}")
            print(f"Ataque especial-: {atq_especial}")
            print(f"Defensa especial: {def_especial}")
            print(f"Velocidad-------: {velocidad}")

        if poke_inicial == 2:
            #DATOS
            EB = 39
            ataque = 52
            defensa = 43
            a_especial = 60 #valor ataque especial
            d_especial = 50 #valor defensa especial
            vel = 65
            #puntos de salud
            vi = randint(1, 39)
            ps = ((vi + 2 * EB)* (nivel/100))+10+nivel
            #puntos de ataque
            vi2 = randint(1, 52)
            atq = ((vi2 + 2 * ataque)*(nivel/100))+5
            #puntos de defensa
            vi3 = randint(1, 43)
            defe = ((vi3 + 2 * defensa)*(nivel/100))+5
            #puntos de ataque especial
            vi4 = randint(1, 60)
            atq_especial = ((vi4 + 2 * a_especial)*(nivel/100))+5
            #puntos de defensa especial
            vi5 = randint(1, 50)
            def_especial = ((vi5 + 2 * d_especial)*(nivel/100))+5
            #velocidad
            vi6 = randint(1, 65)
            velocidad = ((vi6 + 2 * vel)*(nivel/100))+5
            

            print('Su pokemon es: CHARMANDER')
            apodo = input('Ingrese apodo: ')
            print(f"Nivel-----------: {nivel} ")
            print('Movimientos-----: ')
            print('<< Datos de combate >>')
            print(f"Puntos de salud-: {ps} ")
            print(f"Ataque----------: {atq}")
            print(f"Defensa---------: {defe}")
            print(f"Ataque especial-: {atq_especial}")
            print(f"Defensa especial: {def_especial}")
            print(f"Velocidad-------: {velocidad}")

        if poke_inicial == 3:
            #DATOS
            EB = 44
            ataque = 48
            defensa = 65
            a_especial = 50 #ataque especial
            d_especial = 64 #defensa especial
            vel = 43
            #puntos de salud
            vi = randint(1, 44) #valor individual aleatorio
            ps = ((vi + 2 * EB)* (nivel/100))+10+nivel
            #puntos de ataque
            vi2 = randint(1, 48)
            atq = ((vi2 + 2 * ataque)*(nivel/100))+5
            #puntos de defensa
            vi3 = randint(1, 65)
            defe = ((vi3 + 2 * defensa)*(nivel/100))+5
            #puntos de ataque especial
            vi4 = randint(1, 50)
            atq_especial = ((vi4 + 2 * a_especial)*(nivel/100))+5
            #puntos de defensa especial
            vi5 = randint(1, 64)
            def_especial = ((vi5 + 2 * d_especial)*(nivel/100))+5
            #velocidad
            vi6 = randint(1, 43)
            velocidad = ((vi6 + 2 * vel)*(nivel/100))+5
            

            print('Su pokemon es: SQUIRTLE')
            apodo = input('Ingrese apodo: ')
            print(f"Nivel-----------: {nivel} ")
            print('Movimientos-----: ')
            print('<< Datos de combate >> ')
            print(f"Puntos de salud-: {ps} ")
            print(f"Ataque----------: {atq}")
            print(f"Defensa---------: {defe}")
            print(f"Ataque especial-: {atq_especial}")
            print(f"Defensa especial: {def_especial}")
            print(f"Velocidad-------: {velocidad}")

#Bloque principal:
print(' BIENVENIDO A POKEMON ROJO. ')
print('INICIO DE JUEGO... ')
print('Pokemon Inicial Disponibles: ')
print('1 - BULBASAUR. \n2 - CHARMANDER. \n3 - SQUIRTLE.')
poke_inicial = int(input('Seleccione un pokemon inicial: '))

clear()
print(inicial(poke_inicial))
