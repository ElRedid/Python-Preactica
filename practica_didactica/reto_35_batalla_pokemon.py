# Enunciado: Crea un programa que calcule el daño de un ataque durante
# una batalla Pokémon.
# - La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
# - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
# - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico 
#   (buscar su efectividad)
# - El programa recibe los siguientes parámetros:
#  - Tipo del Pokémon atacante.
#  - Tipo del Pokémon defensor.
#  - Ataque: Entre 1 y 100.
#  - Defensa: Entre 1 y 100.

class Pokemon:
    def __init__(self):
        self.nombre = None
        self.ataque = 10
        self.defensa = 10
        self.elemento = None
        
    def tipo(self, numero):
        elementos =("Agua", "Fuego", "Planta", "Eléctico")
        return elementos[numero]

def efectividad(atacante, defensor):
    if atacante == "Agua":
        if defensor == "Agua":
            return 0.5
        elif defensor == "Fuego":
            return 2
        elif defensor == "Planta":
            return 0.5
        elif defensor == "Eléctico":
            return 1
    elif atacante == "Fuego":
        if defensor == "Agua":
            return 0.5
        elif defensor == "Fuego":
            return 0.5
        elif defensor == "Planta":
            return 2
        elif defensor == "Eléctico":
            return 1
    elif atacante == "Planta":
        if defensor == "Agua":
            return 2
        elif defensor == "Fuego":
            return 0.5
        elif defensor == "Planta":
            return 0.5
        elif defensor == "Eléctico":
            return 1
    elif atacante == "Eléctico":
        if defensor == "Agua":
            return 2
        elif defensor == "Fuego":
            return 1
        elif defensor == "Planta":
            return 0.5
        elif defensor == "Eléctico":
            return 0.5
def ataque(atacante, defensor):
    daño = 50 * (atacante.ataque / defensor.defensa) * efectividad(atacante.elemento, defensor.elemento)
    return daño

def elemento():
    while True:
        try:
            print("Elementos disponibles:\n1.) Agua.\n2.) Fuego.\n3.) Planta\n4.) Eléctrico.")
            elemento = int(input())
            if elemento < 0 or elemento > 4: print("Valor no valido, vuelva a intentarlo")
            else: return elemento
        except : print("Valor no valido, vuelva a intentarlo")           

def estadistica():
     while True:
        try:
            atributo = int(input())
            if atributo < 1 or atributo > 100: print("Valor no valido, vuelva a intentarlo, rando 1 a 100.")
            else: return atributo
        except : print("Valor no valido, vuelva a intentarlo, rando 1 a 100.")  
        
def creando_pokemon():
    nuevo_pokemon = Pokemon()
    print("Ingrese el nombre para el Pokemon:")
    nombre = input()
    nuevo_pokemon.nombre = nombre
    print("Seleccione el elemento del pokemon:")
    elemento_seleccionado = nuevo_pokemon.tipo(elemento() - 1)
    nuevo_pokemon.elemento = elemento_seleccionado
    print("Su ataque:")
    nuevo_pokemon.ataque = estadistica()
    print("Su defensa:")
    nuevo_pokemon.defensa = estadistica()
    return nuevo_pokemon

atacante = creando_pokemon()
defensor = creando_pokemon()
print(f"{atacante.nombre} atacó a {defensor.nombre}.\nEl daño realizado fue de: {int(ataque(atacante, defensor))} puntos.")
#print(atacante.nombre, atacante.ataque, atacante.defensa, atacante.elemento)
