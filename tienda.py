class Tienda: 
    def __init__(self, opcion, monedas, compra1, compra2, money):
        self.opcion = opcion
        self.monedas = monedas
        self.compra1 = compra1
        self.compra2 = compra2
        self.money = money
    def t(self, opcion, monedas, compra1, compra2, money):
        self.opcion = opcion
        self.monedas = monedas
        self.compra1 = compra1
        self.compra2 = compra2
        self.money = money
        monedas = 2000
        # menu
        print('Bienvenido a la tienda')
        print(f"Su cantidad de monedas es de: {monedas}")
        print('1. Objetos curativos')
        print('2. Poké Ball')
        opcion = int(input('Ingrese la opción a la que desea acceder'))
        if opcion == 1:
            print('OBBJETOS CURATIVOS')
            print('   Nombre:        Puntos de Salud:     Valor:')
            print('1. Posión                20             300')
            print('2. Super-posión          50             700')
            print('3. Hiper-posión         200            1200')
            print('4. Restaurar      (vida completa)      3000')
            compra1 = int(input('Ingrese el número de opción del objeto que desea comprar: '))
            compra2 = int(input('Ingrese la cantidad de objetos seleccionados que desea adquirir: '))
            if compra1 == 1:
                if compra2 * 300 > monedas:
                    print('Cantidad de monedas insuficientes')
                else:
                    monedas = monedas - (compra2 * 300)
                    print('Los objetos han sido comprados correctamente')
                    print(f"Su cantidad de monedas actual es de: {monedas}")
            if compra1 == 2:
                if compra2 * 700 > monedas:
                    print('Cantidad de monedas insuficientes')
                else:
                    monedas = monedas -(compra2 * 700)
                    print('Los objetos han sido comprados correctamente')
                    print(f"Su cantidad de monedas actual es de: {monedas}")
            if compra1 == 3:
                if compra2 * 1200 > monedas:
                    print('Cantidad de monedas insuficientes')
                else:
                    monedas = monedas - (compra2 * 1200)
                    print('Los objetos han sido comprados correctamente')
                    print(f"Su cantidad de monedas actual es de: {monedas}")
            if compra1 == 4:
                if compra2 * 3000 > monedas:
                    print('Cantidad de monedas insuficientes')
                else:
                    monedas = monedas - (compra2 * 3000)
                    print('Los objetos han sido comprados correctamente')
                    print(f"Su cantidad de monedas actual es de: {monedas}")
        elif opcion == 2:
            print('POKÉ-BALLS')
            print('   Nombre:     Proporción de captura:     Valor:')
            print('1. Pokéball                 1               200')
            print('2. Super-ball               1.5             600')
            print('3. Ultra-ball               2              1200')
            print('4. Master-ball            255            100000')
            compra1 = int(input('Ingrese el número de opción de la pokéball que desea comprar: '))
            compra2 = int(input('Ingrese la cantidad de objetos seleccionados que desea adquirir: '))
            if compra1 == 1:
                if compra2 * 200 > monedas:
                    print('Cantidad de monedas insuficientes')
                else:
                    monedas = monedas - (compra2 * 200)
                    print('Los objetos han sido comprados correctamente')
                    print(f"Su cantidad de monedas actual es de: {monedas}")
            if compra1 == 2:
                if compra2 * 600 > monedas:
                    print('Cantidad de monedas insuficientes')
                else:
                    monedas = monedas - (compra2 * 600)
                    print('Los objetos han sido comprados correctamente')
                    print(f"Su cantidad de monedas actual es de: {monedas}")
            if compra1 == 3:
                if compra2 * 1200 > monedas:
                    print('Cantidad de monedas insuficientes')
                else:
                    monedas = monedas - (compra2 * 1200)
                    print('Los objetos han sido comprados correctamente')
                    print(f"Su cantidad de monedas actual es de: {monedas}")
            if compra1 == 4:
                if compra2 * 100000 > monedas:
                    print('Cantidad de monedas insuficientes')
                else:
                    monedas = monedas - (compra2 * 1200)
                    print('Los objetos han sido comprados correctamente')
                    print(f"Su cantidad de monedas actual es de: {monedas}")
        else:
            print('ERROR')
            print('ingrese una opción válida')
