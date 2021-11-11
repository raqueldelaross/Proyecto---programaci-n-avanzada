from random import choice, randint, random
import requests
import os


class Batallas:
    def __init__(self, seleccion, inventario):
        # pokemon se recibe desde el programa main.py
        self.pokemon_seleccionado = seleccion 
        self.vida = self.pokemon_seleccionado['Salud']
        self.inventario = inventario
        self.captura = False
        self.estado = None

    def pokemon_salvaje(self, nivelpokeusuario):
        if(nivelpokeusuario <= 5):
            nivel = randint(1, nivelpokeusuario + 5)
        else:
            nivel = randint(nivelpokeusuario - 5, nivelpokeusuario + 5)
        opcion = randint(1, 800)
        pokemones = requests.get(
            f"https://pokeapi.co/api/v2/pokemon/{opcion}/")
        url = f"https://pokeapi.co/api/v2/pokemon/{opcion}/"
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
        movimiento = requests.get(movimiento1['move']['url'])
        movimiento = movimiento.json()
        movimiento1 = {'nombre': movimiento['name'], 'tipo': movimiento['type']['name'], 'categoria': movimiento['meta']
                       ['category']['name'], 'potencia': movimiento['power'], 'precision': movimiento['accuracy']}
        while(movimiento1['potencia'] == None):
            movimiento1 = choice(movimientos)
            movimiento = requests.get(movimiento1['move']['url'])
            movimiento = movimiento.json()
            movimiento1 = {'nombre': movimiento['name'], 'tipo': movimiento['type']['name'], 'categoria': movimiento['meta']
                           ['category']['name'], 'potencia': movimiento['power'], 'precision': movimiento['accuracy']}
        movimiento2 = choice(movimientos)
        movimiento = requests.get(movimiento2['move']['url'])
        movimiento = movimiento.json()
        movimiento2 = {'nombre': movimiento['name'], 'tipo': movimiento['type']['name'], 'categoria': movimiento['meta']
                       ['category']['name'], 'potencia': movimiento['power'], 'precision': movimiento['accuracy']}
        while(movimiento2['potencia'] == None):
            movimiento2 = choice(movimientos)
            movimiento = requests.get(movimiento2['move']['url'])
            movimiento = movimiento.json()
            movimiento2 = {'nombre': movimiento['name'], 'tipo': movimiento['type']['name'], 'categoria': movimiento['meta']
                           ['category']['name'], 'potencia': movimiento['power'], 'precision': movimiento['accuracy']}
        movimiento3 = choice(movimientos)
        movimiento = requests.get(movimiento3['move']['url'])
        movimiento = movimiento.json()
        movimiento3 = {'nombre': movimiento['name'], 'tipo': movimiento['type']['name'], 'categoria': movimiento['meta']
                       ['category']['name'], 'potencia': movimiento['power'], 'precision': movimiento['accuracy']}
        while(movimiento3['potencia'] == None):
            movimiento3 = choice(movimientos)
            movimiento = requests.get(movimiento3['move']['url'])
            movimiento = movimiento.json()
            movimiento3 = {'nombre': movimiento['name'], 'tipo': movimiento['type']['name'], 'categoria': movimiento['meta']
                           ['category']['name'], 'potencia': movimiento['power'], 'precision': movimiento['accuracy']}
        movimiento4 = choice(movimientos)
        movimiento = requests.get(movimiento4['move']['url'])
        movimiento = movimiento.json()
        movimiento4 = {'nombre': movimiento['name'], 'tipo': movimiento['type']['name'], 'categoria': movimiento['meta']
                       ['category']['name'], 'potencia': movimiento['power'], 'precision': movimiento['accuracy']}
        while(movimiento4['potencia'] == None):
            movimiento4 = choice(movimientos)
            movimiento = requests.get(movimiento4['move']['url'])
            movimiento = movimiento.json()
            movimiento4 = {'nombre': movimiento['name'], 'tipo': movimiento['type']['name'], 'categoria': movimiento['meta']
                           ['category']['name'], 'potencia': movimiento['power'], 'precision': movimiento['accuracy']}
        exp = pokemon['base_experience']
        tipos = []
        for i in pokemon['types']:
            tipos.append(
                {'name': i['type']['name'], 'url': i['type']['url']})
        speciesdata = requests.get(pokemon['species']['url'])
        speciesdata = speciesdata.json()
        self.ratiocaptura = speciesdata['capture_rate']
        print(f"Capture ratio {self.ratiocaptura}")
        self.pokesalvaje = {'nombre': pokemon['name'], 'url': url, 'apodo': "", 'nivel': nivel, 'tipo': tipos, 'Salud': ps, 'Ataque': atq, 'Defensa': defe, 'Ataque especial': atq_especial,
                            'Defensa especial': def_especial, 'Velocidad': velocidad, 'experiencia': exp, 'movimientos': [movimiento1, movimiento2, movimiento3, movimiento4], 'niveles_subidos': 0}
        # guardar especificaciones a una variable local para consultar durante batalla
        return self.pokesalvaje

    def atacar(self, ataque):
        at = ataque
        if(self.turno == 'salvaje'):
            salvajetipos = []
            for x in self.pokesalvaje['tipo']:
                salvajetipos.append(x['name'])
            muy_eficaz = []
            poco_eficaz = []
            sin_efecto = []
            for x in self.pokemon_seleccionado['tipo']:
                lista = requests.get(x['url'])
                lista = lista.json()
                for y in lista['damage_relations']['double_damage_from']:
                    muy_eficaz.append(y['name'])
                for y in lista['damage_relations']['half_damage_from']:
                    poco_eficaz.append(y['name'])
                for y in lista['damage_relations']['no_damage_from']:
                    sin_efecto.append(y['name'])

            for x in salvajetipos:
                if x in muy_eficaz:
                    indice_tipogolpe = 2
                    break
                elif x in poco_eficaz:
                    indice_tipogolpe = 0.5
                    break
                elif x in sin_efecto:
                    indice_tipogolpe = 0
                    break
                else:
                    indice_tipogolpe = 1
            v = randint(85, 100)
            daño = 0.01 * 1.5 * 2 * v * \
                ((((0.2 * self.salvaje['nivel'] + 1) * self.salvaje['Ataque']
                 * at['potencia']) / (25 * self.pokemon_seleccionado['Defensa'])) + 2)
            golpe = randint(0, 100)
            if(at['precision'] != None):
                if(golpe <= at['precision']):
                    critico = randint(0, 100)
                    if(critico <= 6.25):
                        daño = daño + (daño/2)
                        daño = daño * indice_tipogolpe
                        self.vida = self.vida - daño
                        if(self.salvajevida > 0 and self.vida <= 0):
                            self.perder()
                    else:
                        daño = daño * indice_tipogolpe
                        self.vida = self.vida - daño
                        if(self.salvajevida > 0 and self.vida <= 0):
                            self.perder()
                else:
                    print("Ataque del pokemon salvaje fallido")
                    daño = "Ataque fallido"
            self.historial.append(
                {'pokemon': self.pokesalvaje['nombre'], 'ataque': at['nombre'], 'daño': daño})

        elif(self.turno == 'jugador'):
            jugadortipos = []
            for x in self.pokemon_seleccionado['tipo']:
                jugadortipos.append(x['name'])
            muy_eficaz = []
            poco_eficaz = []
            sin_efecto = []
            for x in self.pokesalvaje['tipo']:
                lista = requests.get(x['url'])
                lista = lista.json()
                for y in lista['damage_relations']['double_damage_from']:
                    muy_eficaz.append(y['name'])
                for y in lista['damage_relations']['half_damage_from']:
                    poco_eficaz.append(y['name'])
                for y in lista['damage_relations']['no_damage_from']:
                    sin_efecto.append(y['name'])

            for x in jugadortipos:
                if x in muy_eficaz:
                    indice_tipogolpe = 2
                    break
                elif x in poco_eficaz:
                    indice_tipogolpe = 0.5
                    break
                elif x in sin_efecto:
                    indice_tipogolpe = 0
                    break
                else:
                    indice_tipogolpe = 1
            v = randint(85, 100)
            daño = 0.01 * 1.5 * 2 * v * \
                ((((0.2 * self.pokemon_seleccionado['nivel'] + 1) * self.pokemon_seleccionado['Ataque']
                 * at['potencia']) / (25 * self.salvaje['Defensa'])) + 2)
            golpe = randint(0, 100)
            if(golpe <= at['precision'] and at['precision'] != None):
                critico = randint(0, 100)
                if(critico <= 6.25):
                    daño = daño + (daño/2)
                    daño = daño * indice_tipogolpe
                    self.salvajevida = self.salvajevida - daño
                    if self.salvajevida <= 0 and self.vida > 0:
                        self.ganar()
                else:
                    daño = daño * indice_tipogolpe
                    self.salvajevida = self.salvajevida - daño
                    if self.salvajevida <= 0 and self.vida > 0:
                        self.ganar()
            else:
                print("Tu ataque ha fallido")
                daño = "Ataque fallido"
            self.historial.append(
                {'pokemon': self.pokemon_seleccionado['apodo'], 'ataque': at['nombre'], 'daño': daño})

        if self.turno == 'salvaje':
            self.turno = 'jugador'
        if self.turno == 'jugador':
            self.turno = 'salvaje'

    def capturar(self):
        if(self.salvajevida > 0):
            if(self.inventario.pokeball > 0 or self.inventario.superpokeball > 0 or self.inventario.ultraball > 0 or self.inventario.masterball > 0):
                print('Utilizar una pokebola')
                print('POKEBOLAS:')
                print(f"1. Pokeball:       {self.inventario.pokeball}")
                print(f"2. Superpokeball: {self.inventario.superpokeball}")
                print(f"3. Ultraball: {self.inventario.ultraball}")
                print(f"4. Masterball: {self.inventario.masterball}")
                objeto = int(
                    input('Ingrese la opción de la pokebola que desee usar: '))

                if(objeto == 1):
                    if self.inventario.pokeball > 0:
                        self.inventario.usar_poke(1)
                        captura = (((3*self.pokemon_salvaje['Salud'])-(
                            2*self.salvajevida))*self.ratiocaptura*1)/(3*self.pokemon_salvaje['Salud'])
                        if(captura >= 255):
                            print("Pokemon Capturado!")
                            self.estado = 2
                            self.x = 0
                        else:
                            print(
                                "Fallaste! No se logro capturar el pokemon este turno")
                            self.turno = 'salvaje'
                            os.system("pause")
                    else:
                        print('Error, no tiene el objeto seleccionado')
                        os.system("pause")
                if(objeto == 2):
                    if self.inventario.superpokeball > 0:
                        self.inventario.usar_poke(2)
                        captura = (((3*self.pokemon_salvaje['Salud'])-(
                            2*self.salvajevida))*self.ratiocaptura*1.5)/(3*self.pokemon_salvaje['Salud'])
                        if(captura >= 255):
                            print("Pokemon Capturado!")
                            self.estado = 2
                            self.x = 0
                        else:
                            print(
                                "Fallaste! No se logro capturar el pokemon este turno")
                            self.turno = 'salvaje'
                            os.system("pause")
                    else:
                        print('Error, no tiene el objeto seleccionado')
                        os.system("pause")
                if(objeto == 3):
                    if self.inventario.ultraball > 0:
                        self.inventario.usar_poke(3)
                        captura = (((3*self.pokemon_salvaje['Salud'])-(
                            2*self.salvajevida))*self.ratiocaptura*2)/(3*self.pokemon_salvaje['Salud'])
                        if(captura >= 255):
                            print("Pokemon Capturado!")
                            self.estado = 2
                            self.x = 0
                        else:
                            print(
                                "Fallaste! No se logro capturar el pokemon este turno")
                            self.turno = 'salvaje'
                            os.system("pause")
                    else:
                        print('Error, no tiene el objeto seleccionado')
                        os.system("pause")
                if(objeto == 4):
                    if self.inventario.masterball > 0:
                        self.inventario.usar_poke(4)
                        captura = (((3*self.pokemon_salvaje['Salud'])-(
                            2*self.salvajevida))*self.ratiocaptura*255)/(3*self.pokemon_salvaje['Salud'])
                        if(captura >= 255):
                            print("Pokemon Capturado!")
                            self.estado = 2
                            self.x = 0
                        else:
                            print(
                                "Fallaste! No se logro capturar el pokemon este turno")
                            self.turno = 'salvaje'
                            os.system("pause")
                    else:
                        print('Error, no tiene el objeto seleccionado')
                        os.system("pause")

        # NOTA: CAPTURAR DEBE RETORNAR UN BOOLEANO (TRUE SI LO CAPTURO, FLASE SI NO)
        pass

    def curar(self):
        print('Utilizar un objeto curativo')
        print('OBJETOS CURATIVOS:')
        print(f"1. Posión:       {self.inventario.posion}")
        print(f"2. Super-posión: {self.inventario.superposion}")
        print(f"3. Hiper-posión: {self.inventario.hiperposion}")
        print(f"4. Restauración: {self.inventario.restaurar}")
        objeto = int(
            input('Ingrese la opción del objeto curativo que desee usar: '))
        if objeto == 1:
            if self.inventario.posion > 0:
                self.vida += 20
                self.inventario.posion -= 1
                print('Se ha sumado 20 puntos de vida a su pokémon')
                self.inventario.usar_cura(1)
            else:
                print('Error, no tiene el objeto curativo seleccionado')
                os.system("pause")  
                #continue
        elif objeto == 2:
            if self.inventario.superposion > 0:
                self.vida += 50
                self.inventario.superposion -=1
                print('Se ha sumado 50 puntos de vida a su pokémon')
                self.inventario.usar_cura(2)
            else:   
                print('Error, no tiene el objeto curativo seleccionado')
                os.system("pause")  
                # continue
        elif objeto == 3:
            if self.inventario.hiperposion > 0:
                self.vida += 200
                self.inventario.hiperposio -=1
                print('Se ha sumado 200 puntos de vida a su pokémon')
                self.inventario.usar_cura(3)
            else:   
                print('Error, no tiene el objeto curativo seleccionado')
                os.system("pause")  
                # continue
        elif objeto == 4:
            if self.inventario.restaurar > 0:
                self.vida = 3000
                self.inventario.restaurar -=1
                print('Se ha restaurado la vida de su pokémon')
                self.inventario.usar_cura(4)
            else:       
                print('Error, no tiene el objeto curativo seleccionado')
                os.system("pause")  
                # continue
        else:
            print('ERROR')

    def huir(self):
        num_a = randint(0, 255)
        A = self.pokemon_seleccionado['Velocidad']
        B = self.pokesalvaje['Velocidad']
        F = (((A * 128 / B) + 30) % 256)
        if num_a < F:
            print( f"¡Huida Exitosa! *fin de la batalla* ")
            self.x = 0
            self.estado = 1
        else:
            print( f"No puede huir en este momento!")
    
        os.system('pause')

    def ganar(self):
        print('Ganaste')
        self.x = 0
        self.estado = 1
        # Experiencia
        experiencia = (
            self.pokesalvaje['experiencia'] * self.pokesalvaje['nivel']) / 7
        print(f"Usted a adquirido {experiencia} exp")
        nivelsiguiente = self.pokemon_seleccionado['nivel']+1
        subir = 0.8 * (nivelsiguiente *
                       nivelsiguiente * nivelsiguiente)
        self.pokemon_seleccionado['experiencia'] += experiencia
        if experiencia >= subir:
            if subir == experiencia:
                self.pokemon_seleccionado['experiencia'] = 0
            else:
                self.pokemon_seleccionado['experiencia'] = self.pokemon_seleccionado['experiencia'] - subir
            self.pokemon_seleccionado['nivel'] += 1
            self.pokemon_seleccionado['niveles_subidos'] += 1
            print("Felicidades has subido de nivel!")
            # Movimiento nuevo
            self.aprender_movimiento()

            # Bonificacion monetaria
        if self.pokesalvaje['nivel'] <= 10:
            self.inventario.monedas += 200
        elif self.pokesalvaje['nivel'] > 10 and self.pokesalvaje['nivel'] <= 30:
            self.inventario.monedas += 500
        elif self.pokesalvaje['nivel'] > 30 and self.pokesalvaje['nivel'] <= 60:
            self.inventario.monedas += 1000
        elif self.pokesalvaje['nivel'] > 60 and self.pokesalvaje['nivel'] <= 80:
            self.inventario.monedas += 2000
        elif self.pokesalvaje['nivel'] > 80 and self.pokesalvaje['nivel'] <= 100:
            self.inventario.monedas += 10000

        os.system("pause")

    def perder(self):
        print('Perdiste')
        self.x = 0
        self.estado = 0
        os.system("pause")

    def aprender_movimiento(self):
        if (self.pokemon_seleccionado['niveles_subidos'] == 4):
            print(
                "Felicidades has subido 4 Niveles puedes aprender un movimiento nuevo!")
            os.system("pause")
            if(self.pokemon_seleccionado['movimientos'].len() < 4):
                movimientos = requests.get(
                    self.pokemon_seleccionado['url'])
                movimientos = movimientos.json()
                movimientos = movimientos['moves']
                aprendido = choice(movimientos)
                movimiento = requests.get(aprendido['move']['url'])
                movimiento = movimiento.json()
                nuevo_movimiento = {'nombre': movimiento['name'], 'tipo': movimiento['type']['name'], 'categoria': movimiento['meta']
                                    ['category']['name'], 'potencia': movimiento['power'], 'precision': movimiento['accuracy']}
                while(nuevo_movimiento['potencia'] == None):
                    aprendido = choice(movimientos)
                    movimiento = requests.get(
                        aprendido['move']['url'])
                    movimiento = movimiento.json()
                    nuevo_movimiento = {'nombre': movimiento['name'], 'tipo': movimiento['type']['name'], 'categoria': movimiento['meta']
                                        ['category']['name'], 'potencia': movimiento['power'], 'precision': movimiento['accuracy']}
                    if nuevo_movimiento in self.pokemon_seleccionado['movimientos']:
                        nuevo_movimiento['potencia'] = None
                os.system("cls")
                self.pokemon_seleccionado['movimientos'].append(
                    nuevo_movimiento)
                self.pokemon_seleccionado['niveles_subidos'] = 0
                print("Nuevo movimiento aprendido!")
                print(
                    f"Nombre del Movimiento ---: {nuevo_movimiento['nombre']}")
                print(
                    f"Tipo --------------------: {nuevo_movimiento['tipo']}")
                print(
                    f"Categoría ---------------: {nuevo_movimiento['categoria']}")
                print(
                    f"Potencia ---------------: {nuevo_movimiento['potencia']}")
                print(
                    f"Precision ---------------: {nuevo_movimiento['precision']}")
                os.system("pause")
            else:
                movimientos = requests.get(
                    self.pokemon_seleccionado['url'])
                movimientos = movimientos.json()
                movimientos = movimientos['moves']
                aprendido = choice(movimientos)
                movimiento = requests.get(aprendido['move']['url'])
                movimiento = movimiento.json()
                nuevo_movimiento = {'nombre': movimiento['name'], 'tipo': movimiento['type']['name'], 'categoria': movimiento['meta']
                                    ['category']['name'], 'potencia': movimiento['power'], 'precision': movimiento['accuracy']}
                while(nuevo_movimiento['potencia'] == None):
                    aprendido = choice(movimientos)
                    movimiento = requests.get(
                        aprendido['move']['url'])
                    movimiento = movimiento.json()
                    nuevo_movimiento = {'nombre': movimiento['name'], 'tipo': movimiento['type']['name'], 'categoria': movimiento['meta']
                                        ['category']['name'], 'potencia': movimiento['power'], 'precision': movimiento['accuracy']}
                    if nuevo_movimiento in self.pokemon_seleccionado['movimientos']:
                        nuevo_movimiento['potencia'] = None
                print(
                    f"Su pokemon ya tiene 4 Movimientos Aprendidos, para aprender el movimiento {nuevo_movimiento['nombre']} Tiene que cambiar un movimiento previamente aprendido por su pokemon")
                os.system("pause")
                os.system("cls")
                print("Datos del nuevo Movimiento")
                print(
                    f"Nombre del Movimiento ---: {nuevo_movimiento['nombre']}")
                print(
                    f"Tipo --------------------: {nuevo_movimiento['tipo']}")
                print(
                    f"Categoría ---------------: {nuevo_movimiento['categoria']}")
                print(
                    f"Potencia ---------------: {nuevo_movimiento['potencia']}")
                print(
                    f"Precision ---------------: {nuevo_movimiento['precision']}")
                cambio = input(
                    '\nDesea cambiar un movimiento ya existente por este nuevo movimiento? (1. Si/ 2. No) ')
                os.system("cls")
                if cambio == 1:
                    print('Ok, que movimiento deseas reemplazar?')
                    num = 1
                    for x in self.pokemon_seleccionado['movimientos']:
                        print(
                            f"{num} {x['nombre']} -- Tipo: {x['tipo']} -- Categoria: {x['categoria']} -- Potencia: {x['potencia']} -- Precision: {x['precision']}")
                        num += 1
                    print(
                        f"5) Creo que mejor me quedo con mis movimientos actuales")
                    reemplazar = int(input(""))
                    if reemplazar == 1:
                        self.pokemon_seleccionado['movimientos'][0] = nuevo_movimiento
                        self.pokemon_seleccionado['niveles_subidos'] = 0
                        print("Movimiento reemplazado!")
                    if reemplazar == 2:
                        self.pokemon_seleccionado['movimientos'][1] = nuevo_movimiento
                        self.pokemon_seleccionado['niveles_subidos'] = 0
                        print("Movimiento reemplazado!")
                    if reemplazar == 3:
                        self.pokemon_seleccionado['movimientos'][2] = nuevo_movimiento
                        self.pokemon_seleccionado['niveles_subidos'] = 0
                        print("Movimiento reemplazado!")
                    if reemplazar == 4:
                        self.pokemon_seleccionado['movimientos'][3] = nuevo_movimiento
                        self.pokemon_seleccionado['niveles_subidos'] = 0
                        print("Movimiento reemplazado!")
                    if reemplazar == 5:
                        print(
                            'Muy bien, Los movimientos de tu pokemon no se han modificado')
                        self.pokemon_seleccionado['niveles_subidos'] = 0
                    os.system("pause")
                elif cambio == 2:
                    print(
                        'Muy bien, Los movimientos de tu pokemon no se han modificado')
                    self.pokemon_seleccionado['niveles_subidos'] = 0
                    os.system("pause")
                else:
                    print('Ingrese una opcion valida')

    def __str__():
        pass

    def batalla(self):
        # generar estadisticas del pokemon salvaje

        self.salvaje = self.pokemon_salvaje(self.pokemon_seleccionado['nivel']) 
        self.salvajevida = self.salvaje['Salud']
        # comparacion de la velocidad para determinar quien va primero
        if self.salvaje['Velocidad'] > self.pokemon_seleccionado['Velocidad']:
            self.turno = 'salvaje'
        elif self.pokemon_seleccionado['Velocidad'] > self.salvaje['Velocidad']:
            self.turno = 'jugador'
        else:
            rand = randint(1, 10)
            if(rand <= 5):
                self.turno = 'salvaje'
            elif rand > 5:
                self.turno = 'jugador'
        self.x = 2
        self.historial = []
        while self.x > 0:
            os.system("cls")
            print(
                f"Pokemon Rival ------ {self.pokesalvaje['nombre']} --- Nivel: {self.pokesalvaje['nivel']} --- Salud: {self.salvajevida}")
            print(
                f"Tú Pokemon --------- {self.pokemon_seleccionado['apodo']} --- Nivel: {self.pokemon_seleccionado['nivel']} --- Salud: {self.vida}")
            if(self.turno == 'jugador'):
                print("Es tu turno!")
                print(
                    "Acciones Disponibles: \n 1. Atacar \n 2. Capturar Pokemon \n 3. Usar Objeto Curativo \n 4. Huir")
                accion = int(input("Que accion desea realizar? "))
                if accion == 1:
                    num = 1
                    for x in self.pokemon_seleccionado['movimientos']:
                        print(
                            f"{num} {x['nombre']} -- Tipo: {x['tipo']} -- Categoria: {x['categoria']} -- Potencia: {x['potencia']} -- Precision: {x['precision']}")
                        num += 1
                    num = int(
                        input("Que movimiento desea utilizar para el ataque? "))
                    ataque = self.pokemon_seleccionado['movimientos'][num-1]
                    self.atacar(ataque)
                elif accion == 2:
                    self.capturar()
                elif accion == 3:
                    self.curar()
                elif accion == 4:
                    self.huir()
                else:
                    print("Escoja una opcion válida")
            elif(self.turno == 'salvaje'):
                print("Es turno del pokemon rival!")
                ataque = choice(self.pokesalvaje['movimientos'])
                self.atacar(ataque)
            else:
                pass
            print("---- Historial de Ataques ----")
            if self.historial != None:
                for x in self.historial:
                    print(f"{x['pokemon']} --- {x['ataque']} --- {x['daño']}")
            else:
                print("No se han realizado ataques aún")
            os.system("pause")

        if self.estado == 0:  # perder batalla
            return(self.pokesalvaje, False, self.pokemon_seleccionado)
        elif self.estado == 1:  # ganar batalla o huir
            # el false indica que no hay captura del pokemon
            return(self.pokesalvaje, False, self.pokemon_seleccionado)
        elif self.estado == 2:
            # el true indica que si hay captura del pokemon
            return(self.pokesalvaje, True, self.pokemon_seleccionado)
            