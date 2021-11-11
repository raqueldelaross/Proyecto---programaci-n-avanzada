import os
from seleccion_pokemon import Seleccion_pokemon
from equipo import Equipo 
from batallas import Batallas
from pokedex import Pokedex
from tienda import Tienda


def clear(): return os.system('cls')


tienda = Tienda()

# Bloque principal:
while(1):
    print('\nBIENVENIDO A POKEMON ROJO. '+'\n')
    print("\033[31m"+'       ***************     ')
    print('     *******************     ')
    print('   ***********************   ')
    print(' *************************** ')
    print('*************'+"\033[30m"+"****"+"\033[31m"+'**************')
    print("\033[30m"+'*************'+"\033[37m"+"****"+"\033[30m"+'*************')
    print("\033[30m"+'*************'+"\033[37m"+"****"+"\033[30m"+'*************')
    print("\033[37m"+'*************'+"\033[30m"+"****"+"\033[37m"+'**************')
    print(' *************************** ')
    print('   ***********************   ')
    print('     *******************     ')
    print('       ***************     '+'\n')
    print('INICIO DE JUEGO... ')
    print('Pokemon Inicial Disponibles: ')
    print('1 - BULBASAUR. \n2 - CHARMANDER. \n3 - SQUIRTLE.')
    poke_inicial = 0
    poke_inicial = int(input('Seleccione un pokemon inicial: '))
    if(poke_inicial < 1 or poke_inicial > 3):
        print("Esta no es una opcion valida. Por favor seleccione de nuevo")
        os.system("pause")
        clear()
    else:
        break

clear()

# Asigna dentro de una variable la clase Pokemon_inicial 

seleccion = Seleccion_pokemon(poke_inicial)
primer = seleccion.inicial()
clear()
equipo = Equipo(primer)
pokedex = Pokedex(primer)

while True:
    # Menú de interacción
    clear()
    print('Bienvenido al juego de Pokémon')
    print('------------------------------')
    print('1. Equipo pokémon')
    print('2. Batallas contra pokémon salvajes')
    print('3. Pokédex')
    print('4. Tienda')
    print('5. Salir del videojuego')
    # seleccionar una opción del menú 
    opcion = int(input('Seleccione una opción para continuar: '))
    clear()
    if opcion == 1:
        equipo.progreso()
    elif opcion == 2: 
        # Al igual que la opción uno seleccionara un pokemon de los que tiene para poder pelear
        # Si el usuario selecciona un pokemon existente que envie este dato a la clase batallas: 
        # Batallas(“Link para el pokemon mencionado”)
        pokemon = equipo.pokemon_inicial
        batalla = Batallas(pokemon, tienda)
        nuevo, captura, seleccionado = batalla.batalla()
        pokedex.nuevo(nuevo, captura)
        if(captura == True):
            equipo.nuevo_pokemon(nuevo)
    elif opcion == 3:
        pokedex.mostrar()
    elif opcion == 4:
        clear()
        # menu
        print('Bienvenido a la tienda')
        print('1. Objetos curativos')
        print('2. Poké Ball')
        print('3. Ver inventario de objetos curativos y pokeballs')
        opcion = int(input('Ingrese la opción a la que desea acceder: '))
        if opcion == 1:
            clear()
            print(f"Monedas Disponibles: {tienda.monedas}")
            print('OBJETOS CURATIVOS')
            print('   Nombre:        Puntos de Salud:     Valor:')
            print('1. Posión                20             300')
            print('2. Super-posión          50             700')
            print('3. Hiper-posión         200            1200')
            print('4. Restaurar      (vida completa)      3000')
            compra1 = int(
                input('Ingrese el número de opción del objeto que desea comprar: '))
            cantidad = int(
                input('Ingrese la cantidad de objetos seleccionados que desea adquirir: '))
            tienda.objetos_curativos(compra1, cantidad)
            os.system('pause')

        elif opcion == 2:
            clear()
            print(f"Monedas Disponibles: {tienda.monedas}")
            print('POKÉ-BALLS')
            print('   Nombre:     Proporción de captura:     Valor:')
            print('1. Pokéball                 1               200')
            print('2. Super-ball               1.5             600')
            print('3. Ultra-ball               2              1200')
            print('4. Master-ball            255            100000')
            compra1 = int(
                input('Ingrese el número de opción de la pokéball que desea comprar: '))
            cantidad = int(
                input('Ingrese la cantidad de objetos seleccionados que desea adquirir: '))
            tienda.poke(compra1, cantidad)
            os.system('pause')

        elif opcion == 3:
            clear()
            tienda.__str__()
            os.system('pause')
        else:
            print('ERROR')
            print('ingrese una opción válida')
            os.system("pause")
    elif opcion == 5:
        clear()
        # Mostrar creditos
        print('\033[32m'+'GRACIAS POR JUGAR A POKEMON\nGRUPO DE DESARROLLO:\n')
        print('**************************************************************************')
        print('* LIDER DEL GRUPO DE DESARROLLADORES: HEIDI RAQUEL DE LA ROSA QUINONEZ   *')
        print('* DESARROLLADOR: ANGEL SEBASTIAN PEREIRA FAJARDO                         *')
        print('* DESARROLLADOR: YEFRI RICARDO CHAY HERRERA                              *')
        print('* DESARROLLADOR: FRANCISCO JAVIER SANCHEZ TASEJ                          *')
        print('**************************************************************************')
        input('Presiona cualquier tecla para continuar...')
        print('\033[39m')
        clear()
        break
    else:
        continue
