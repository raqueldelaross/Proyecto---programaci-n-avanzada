import os
from seleccion_pokemon import Seleccion_pokemon
from equipo import Equipo 
from batallas import Batallas
from pokedex import Pokedex
from tienda import Tienda

clear = lambda: os.system('cls')

# Bloque principal:
print('\nBIENVENIDO A POKEMON ROJO. ')
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
        posion = 0
        superposion = 0
        hiperposion = 0
        restaurar = 0
        monedas = 2000
        pokeball = 0
        superpokeball = 0
        ultraball = 0
        masterball = 0
        clear()
        # menu
        print('Bienvenido a la tienda')
        print('1. Objetos curativos')
        print('2. Poké Ball')
        print('3. Ver inventario de objetos curativos y pokeballs')
        opcion = int(input('Ingrese la opción a la que desea acceder: '))
        if opcion == 1:
            clear()
            print('OBBJETOS CURATIVOS')
            print('   Nombre:        Puntos de Salud:     Valor:')
            print('1. Posión                20             300')
            print('2. Super-posión          50             700')
            print('3. Hiper-posión         200            1200')
            print('4. Restaurar      (vida completa)      3000')
            compra1 = int(input('Ingrese el número de opción del objeto que desea comprar: '))
            cantidad = int(input('Ingrese la cantidad de objetos seleccionados que desea adquirir: '))
            if compra1 == 1:
                clear()
                if cantidad * 300 > monedas:
                    print('Cantidad de monedas insuficientes')
                else:
                    posion = posion + cantidad
                    monedas = monedas - (cantidad * 300)
                    print('Los objetos han sido comprados correctamente')
            if compra1 == 2:
                clear()
                if cantidad * 700 > monedas:
                    print('Cantidad de monedas insuficientes')
                else:
                    monedas = monedas -(cantidad * 700)
                    superposion = superposion + cantidad
                    print('Los objetos han sido comprados correctamente')
            if compra1 == 3:
                clear()
                if cantidad * 1200 > monedas:
                    print('Cantidad de monedas insuficientes')
                else:
                    monedas = monedas - (cantidad * 1200)
                    hiperposion = hiperposion + cantidad
                    print('Los objetos han sido comprados correctamente')
            if compra1 == 4:
                clear()
                if cantidad * 3000 > monedas:
                    print('Cantidad de monedas insuficientes')
                else:
                    restaurar = restaurar + cantidad
                    monedas = monedas - (cantidad * 3000)
                    print('Los objetos han sido comprados correctamente')
        elif opcion == 2:
            clear()
            print('POKÉ-BALLS')
            print('   Nombre:     Proporción de captura:     Valor:')
            print('1. Pokéball                 1               200')
            print('2. Super-ball               1.5             600')
            print('3. Ultra-ball               2              1200')
            print('4. Master-ball            255            100000')
            compra1 = int(input('Ingrese el número de opción de la pokéball que desea comprar: '))
            cantidad = int(input('Ingrese la cantidad de objetos seleccionados que desea adquirir: '))
            if compra1 == 1:
                clear()
                if cantidad * 200 > monedas:
                    print('Cantidad de monedas insuficientes')
                else:
                    pokeball = pokeball + cantidad
                    monedas = monedas - (cantidad * 200)
                    print('Los objetos han sido comprados correctamente')
            if compra1 == 2:
                clear()
                if cantidad * 600 > monedas:
                    print('Cantidad de monedas insuficientes')
                else:
                    superpokeball = superpokeball + superpokeball
                    monedas = monedas - (cantidad * 600)
                    print('Los objetos han sido comprados correctamente')
            if compra1 == 3:
                clear()
                if cantidad * 1200 > monedas:
                    print('Cantidad de monedas insuficientes')
                else:
                    ultraball = ultraball + cantidad
                    monedas = monedas - (cantidad * 1200)
                    print('Los objetos han sido comprados correctamente')
            if compra1 == 4:
                clear()
                if cantidad * 100000 > monedas:
                    print('Cantidad de monedas insuficientes')
                else:
                    masterball = masterball + cantidad
                    monedas = monedas - (cantidad * 1200)
                    print('Los objetos han sido comprados correctamente')
                    print(f"Su cantidad de monedas actual es de: {monedas}")
        elif opcion == 3:
            clear()
            print('INVENTARIO DE OBJETOS CURATIVOS Y POKEBALLS')
            print('OBJETOS CURATIVOS:')
            print(f"Posión:       {posion}")
            print(f"Super-posión: {superposion}")
            print(f"Hiper-posión: {hiperposion}")
            print(f"Restauración: {restaurar}")
            print('\nPOKEBALLS:')
            print(f"Pokeball:     {pokeball}")
            print(f"Super-ball:   {superpokeball}")
            print(f"Ultra-ball:   {ultraball}")
            print(f"Master-ball:  {masterball}")
        else:
            print('ERROR')
            print('ingrese una opción válida')
            os.system("pause")       
    elif opcion == 5:
        clear()
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
