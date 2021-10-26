import os
clear = lambda: os.system('cls')
class Tienda: 
    def __init__(self):
        self.posion = 0
        self.superposion = 0
        self.hiperposion = 0
        self.restaurar = 0
        self.monedas = 2000
        self.pokeball = 0
        self.superpokeball = 0
        self.ultraball = 0
        self.masterball = 0
        

    def objetos_curativos(self, compra1, cantidad):
        if compra1 == 1:
            if cantidad * 300 > self.monedas:
                print('Cantidad de monedas insuficientes')
            else:
                self.posion = self.posion + cantidad
                self.monedas = self.monedas - (cantidad * 300)
                print('Los objetos han sido comprados correctamente')
        if compra1 == 2:
            clear()
            if cantidad * 700 > self.monedas:
                print('Cantidad de monedas insuficientes')
            else:
                self.monedas = self.monedas -(cantidad * 700)
                self.superposion = self.superposion + cantidad
                print('Los objetos han sido comprados correctamente')
        if compra1 == 3:
            clear()
            if cantidad * 1200 > self.monedas:
                print('Cantidad de monedas insuficientes')
            else:
                self.monedas = self.monedas - (cantidad * 1200)
                self.hiperposion = self.hiperposion + cantidad
                print('Los objetos han sido comprados correctamente')
        if compra1 == 4:
            clear()
            if cantidad * 3000 > self.monedas:
                print('Cantidad de monedas insuficientes')
            else:
                self.restaurar = self.restaurar + cantidad
                self.monedas = self.monedas - (cantidad * 3000)
                print('Los objetos han sido comprados correctamente')

    def poke(self, compra1, cantidad):
        if compra1 == 1:
            clear()
            if cantidad * 200 > self.monedas:
                print('Cantidad de monedas insuficientes')
            else:
                self.pokeball = self.pokeball + cantidad
                self.monedas = self.monedas - (cantidad * 200)
                print('Los objetos han sido comprados correctamente')
        if compra1 == 2:
            clear()
            if cantidad * 600 > self.monedas:
                print('Cantidad de monedas insuficientes')
            else:
                    self.superpokeball = self.superpokeball + cantidad
                    self.monedas = self.monedas - (cantidad * 600)
                    print('Los objetos han sido comprados correctamente')
            if compra1 == 3:
                clear()
                if cantidad * 1200 > self.monedas:
                    print('Cantidad de monedas insuficientes')
                else:
                    self.ultraball = self.ultraball + cantidad
                    self.monedas = self.monedas - (cantidad * 1200)
                    print('Los objetos han sido comprados correctamente')
            if compra1 == 4:
                clear()
                if cantidad * 100000 > self.monedas:
                    print('Cantidad de monedas insuficientes')
                else:
                    self.masterball = self.masterball + cantidad
                    monedas = self.monedas - (cantidad * 1200)
                    print('Los objetos han sido comprados correctamente')
                    print(f"Su cantidad de monedas actual es de: {monedas}")

    def __str__(self):
        print('INVENTARIO DE OBJETOS CURATIVOS Y POKEBALLS')
        print('OBJETOS CURATIVOS:')
        print(f"Posión:       {self.posion}")
        print(f"Super-posión: {self.superposion}")
        print(f"Hiper-posión: {self.hiperposion}")
        print(f"Restauración: {self.restaurar}")
        print('\nPOKEBALLS:')
        print(f"Pokeball:     {self.pokeball}")
        print(f"Super-ball:   {self.superpokeball}")
        print(f"Ultra-ball:   {self.ultraball}")
        print(f"Master-ball:  {self.masterball}")