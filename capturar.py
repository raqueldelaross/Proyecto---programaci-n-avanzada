from random import randint
def capturar():
 # ps = puntos de salud del pokemon
 # poke_ball = no recuerdo quien trabajo esta variable

    if ps > 0 and poke_ball > 0:
        
        #DATOS DE PRUEBA - incorporar las variables requeridas
        PSmax = randint(0, 255) #puntos de salud totales del pokemon
        PSactual = randint(0, 255) #puntos de salud que tiene en ese momento el Pokémon
        Rc = randint(0, 255) #proporción de captura del Pokémon
        Rb = randint(0, 255) #proporción de captura de la Poké Ball que seleccionó el jugador

        a = (((3 * PSmax - 2 * PSactual) * Rc *Rb) / 3 * PSmax)

        if a >= 255:
            return True
        else:
            return False
            #llamamos a la funcion atacar y el pokemon salvaje ataca
    else:
        print("No es posible realizar la captura\n siga jugando!")

#bloque principal
resultado = (capturar())
print(resultado)