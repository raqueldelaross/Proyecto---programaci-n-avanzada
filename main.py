import os
from seleccion_pokemon import Seleccion_pokemon
from equipo import Equipo 
from batallas import Batallas
from pokedex import Pokedex
from tienda import Tienda

clear = lambda: os.system('cls')


# Bloque principal:
print(' BIENVENIDO A POKEMON ROJO. ')
print('INICIO DE JUEGO... ')
print('Pokemon Inicial Disponibles: ')
print('1 - BULBASAUR. \n2 - CHARMANDER. \n3 - SQUIRTLE.')

poke_inicial = int(input('Seleccione un pokemon inicial: '))
clear()

# Asigna dentro de una variable la clase Pokemon_inicial 
seleccion = Seleccion_pokemon(poke_inicial) # <- Se envia la opcion seleccionada

print(seleccion.inicial())
clear()

while True:
    # Menú de interacción
    print('Bienvenido al juego de Pokémon')
    print('------------------------------')
    print('1. Equipo pokémon')
    print('2. Batallas contra pokémon salvajes')
    print('3. Pokédex')
    print('4. Tienda')
    print('5. Salir del videojuego')
    # seleccionar una opción del menú 
    opcion = int(input('Seleccione una opción para continuar: '))

    if opcion == 1:
        # Temporal (por modificar)
        # Mostrar un menú con todos los pokemon existentes en el juego:
        # “Pokemon existentes:”
        # “Se menciona en una lista los pokemon”
        # Ver = “Seleccione pokemon que desea ver: “
        # Si el pokemon seleccionado fue el pokemon inicial 
        # o fue capturado durante el juego entonces que envie este dato a equipo: 
        # ‘Equipo (“Link para el pokemon mencionado”)'
        # De lo contrario que muestre un mensaje: “Pokémon no desbloqueado”
        Equipo('link')
        
    elif opcion == 2: 
        # Al igual que la opción uno seleccionara un pokemon de los que tiene para poder pelear
        # Si el usuario selecciona un pokemon existente que envie este dato a la clase batallas: 
        # Batallas(“Link para el pokemon mencionado”)
        Batallas('link')

    elif opcion == 3:
        # En la clase Pokedex los atributos serán los links respectivos de cada pokemon  
        # En el método se verificará si los pokemon ya fueron enfrentados 
        # Si ya fueron enfrentados entonces los mostrara en pantalla 
        # De lo contrario no los mostrara
        Pokedex('link1, link2...... link5')

    elif opcion == 4:
        # Mostrar menú para saber si quiere comprar objetos curativos o Poké Ball 
        # Este dato dirigir a la clase Tienda: ‘Tienda(opción)’
        Tienda('opcion')

    elif opcion == 5:
        # Mostrar creditos
        print('\033[32m'+'GRACIAS POR JUGAR A POKEMON\nGRUPO DE DESARROLLO:\n')
        print('************************************************************************')
        print('* LIDER DEL GRUPO DE DESARROLLADORES: HEIDI RAQUEL DE LA ROSA QUINONEZ *')
        print('* DESARROLLADOR: YEFRI RICARDO CHAY HERRERA                              *')
        print('* DESARROLLADOR: ANGEL SEBASTIAN PEREIRA FAJARDO                         *')
        print('* DESARROLLADOR: FRANCISCO JAVIER SANCHEZ TASEJ                          *')
        print('************************************************************************')
        input('Presiona cualquier tecla para continuar...')
        print('\033[39m')
        break

    else:
        continue
