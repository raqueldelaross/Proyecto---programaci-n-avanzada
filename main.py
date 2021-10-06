# Programa principal del proyecto
import requests
import os
import random
from pokemon import Pokemon

id = 1

while 0:
    print("Bienvenido a Pokemón! Estas listo para comenzar?")
    print("Selecciona tu primer pokemón")
    print("1. Bulbasaur")
    print("2. Charmander")
    print("3. Squirtle")
    select = int(input())

# Bulbasaur
    if (select == 1):
        pokemons = requests.get(f"https://pokeapi.co/api/v2/pokemon/1/")
        pokemon = pokemons.json()
        nombre = "Bulbasaur"
        altura = pokemon['height']
        peso = pokemon['weight']
        nivel = 5
        tipo = pokemon['types']
        habilidades = pokemon['abilities']
        movimientos = []
        max = pokemon['moves'].len()
        mov  = random.randint(0,max-1)
        movimientos.append(pokemon['moves'][mov])
        mov  = random.randint(0,max-1)
        movimientos.append(pokemon['moves'][mov])
        max = pokemon['stats'][0]['base_stat']
        hp = random.randint(0, max)
        max = pokemon['stats'][1]['base_stat']
        attack = random.randint(0, max)
        #repetir para stats 2 - 5
        max = pokemon['stats'][2]['base_stat']
        attack = random.randint(0, max)
        max = pokemon['stats'][3]['base_stat']
        attack = random.randint(0, max)
        max = pokemon['stats'][4]['base_stat']
        attack = random.randint(0, max)
        max = pokemon['stats'][5]['base_stat']
        attack = random.randint(0, max)
        apodo = input("Que apodo le quiere dar al pokemon? ")
        pokemon = Pokemon(nombre, altura, peso, nivel, tipo, habilidades, movimientos, hp, attack)

# Charmander
if (select == 2):
        pokemons = requests.get(f"https://pokeapi.co/api/v2/pokemon/4/")
        pokemon = pokemons.json()
        nombre = "Charmander"
        altura = pokemon['height']
        peso = pokemon['weight']
        nivel = 5
        tipo = pokemon['types']
        habilidades = pokemon['abilities']
        movimientos = []
        max = pokemon['moves'].len()
        mov  = random.randint(0,max-1)
        movimientos.append(pokemon['moves'][mov])
        mov  = random.randint(0,max-1)
        movimientos.append(pokemon['moves'][mov])
        max = pokemon['stats'][0]['base_stat']
        hp = random.randint(0, max)
        max = pokemon['stats'][1]['base_stat']
        attack = random.randint(0, max)
        #repetir para stats 2 - 5
        max = pokemon['stats'][2]['base_stat']
        attack = random.randint(0, max)
        max = pokemon['stats'][3]['base_stat']
        attack = random.randint(0, max)
        max = pokemon['stats'][4]['base_stat']
        attack = random.randint(0, max)
        max = pokemon['stats'][5]['base_stat']
        attack = random.randint(0, max)
        apodo = input("Que apodo le quiere dar al pokemon? ")
        pokemon = Pokemon(nombre, altura, peso, nivel, tipo, habilidades, movimientos, hp, attack)

# Squirtle
if (select == 3):
        pokemons = requests.get(f"https://pokeapi.co/api/v2/pokemon/7/")
        pokemon = pokemons.json()
        nombre = "Squirtle"
        altura = pokemon['height']
        peso = pokemon['weight']
        nivel = 5
        tipo = pokemon['types']
        habilidades = pokemon['abilities']
        movimientos = []
        max = pokemon['moves'].len()
        mov  = random.randint(0,max-1)
        movimientos.append(pokemon['moves'][mov])
        mov  = random.randint(0,max-1)
        movimientos.append(pokemon['moves'][mov])
        max = pokemon['stats'][0]['base_stat']
        hp = random.randint(0, max)
        max = pokemon['stats'][1]['base_stat']
        attack = random.randint(0, max)
        #repetir para stats 2 - 5
        max = pokemon['stats'][2]['base_stat']
        attack = random.randint(0, max)
        max = pokemon['stats'][3]['base_stat']
        attack = random.randint(0, max)
        max = pokemon['stats'][4]['base_stat']
        attack = random.randint(0, max)
        max = pokemon['stats'][5]['base_stat']
        attack = random.randint(0, max)
        apodo = input("Que apodo le quiere dar al pokemon? ")
        pokemon = Pokemon(nombre, altura, peso, nivel, tipo, habilidades, movimientos, hp, attack)