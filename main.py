import os
from pokeinicial import pokeinicial

clear = lambda: os.system('cls')
# mostrar menú

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
    clear()
elif opcion == 2: 
    clear()
elif opcion == 3:
    clear()
elif opcion == 4:
    clear()
elif opcion == 5:
    clear()
else:
    clear()
