#HUIR DE LA BATALLA
from random import randint #librearia para generar numeros aleatorios

def huir():
    num_a = randint(0, 255) #generar numero aleatorio

    #datos generados en def pokemon inicial
    # Pokemon Inicial: 
    # vi6 = randint(1, 20)
    # velocidad = ((vi6 + 2 * vel)*(nivel/100))+5
    # A = velocidad del pokemon que quiere huir 

    #datos generados en def pokemon rival
    #Pokemon Rival: 
    # vi6 = randint(1, 20)
    # velocidad = ((vi6 + 2 * vel)*(nivel/100))+5
    # B = velocidad  del pokemon rival

    #(45 y 65) son datos asignados temporalmente para prueba
    A = 45
    B = 65

    F = (((A * 128 / B) + 30) % 256)

    if num_a < F:
        return f"¡Huida Exitosa! *fin de la batalla* "
    else:
        return f"No puede huir en este momento :( \n ¡intente mas tarde!"
    
    os.system('pause')

#bloque principal
resultado = (huir())
print(resultado)