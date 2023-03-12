# Enunciado: ¡La Tierra Media está en guerra! En ella lucharán razas leales
# a Sauron contra otras bondadosas que no quieren que el mal reine
# sobre sus tierras.
# Cada raza tiene asociado un "valor" entre 1 y 5:
# - Razas bondadosas: Pelosos (1), Sureños buenos (2), Enanos (3),
#   Númenóreanos (4), Elfos (5)
# - Razas malvadas: Sureños malos (2), Orcos (2), Goblins (2),
#   Huargos (3), Trolls (5)
# Crea un programa que calcule el resultado de la batalla entre
# los 2 tipos de ejércitos:
# - El resultado puede ser que gane el bien, el mal, o exista un empate.
#   Dependiendo de la suma del valor del ejército y el número de integrantes.
# - Cada ejército puede estar compuesto por un número de integrantes variable
#   de cada raza.
# - Tienes total libertad para modelar los datos del ejercicio.
# Ej: 1 Peloso pierde contra 1 Orco
#     2 Pelosos empatan contra 1 Orco
#     3 Pelosos ganan a 1 Orco
from random import randint 
class Luchadores:
    def __int__(self):
        self.razadada = None
        self.bando = None
        self.poder = 0  
    razas_combatientes = {1 : ("Pelosos", 1),
                        2 : ("Sureños buenos", 2),
                        3 : ("Enanos", 3),
                        4 : ("Númenóreanos", 4),
                        5 : ("Elfos", 5),
                        6 : ("Sureños malos", 2),
                        7 : ("Orcos", 2),
                        8 : ("Goblins", 2),
                        9 : ("Hungaros", 3),
                        10 : ("Trolls", 4)}
    bando = ("Justicia", "Caos")
def generador_ejercito(bando):
    ejercito = list()
    tamaño_ejercito = randint(1,100)
    for i in range(tamaño_ejercito):
        raza = grupos(bando)
        personaje = Luchadores()
        personaje.razadada = personaje.razas_combatientes[raza][0]
        personaje.poder = personaje.razas_combatientes[raza][1]
        personaje.bando = personaje.bando[bando]
        ejercito.append(personaje)
    return ejercito
def grupos(valor):
    if valor == 0:
        grupos = randint(1,5)
    elif valor == 1:
        grupos = randint(6,10)  
    return grupos
def total_ataque(ejercito):
    ataque = 0
    for i in ejercito:
        ataque += i.poder  
    return ataque
def resultado(ejercito_1, ejercito_2):
    if total_ataque(ejercito_1) > total_ataque(ejercito_2):
        print("Gana el ejercito del bien.")
    elif total_ataque(ejercito_1) < total_ataque(ejercito_2):
        print("Gana el ejercito del mal.")
    else:
        print("La batalla termina en empate.")
def detalle_ejercito(ejercitos):
    ejercito = ejercitos.copy()
    print("Total de tropas:", len(ejercito),"\n")
    print("Dicha tropa está compuesta por:")
    detalle = list()
    while len(ejercito) != 0:
        raza = ejercito.pop(0)
        contador = 1
        iterador = 0
        while iterador < len(ejercito):
            i = ejercito[iterador]
            if raza.razadada == i.razadada:
                ejercito.pop(iterador)        # Al sacarle un componente a la lista hay que restarle uno al iterador, ya que la lista se acomoda 
                contador += 1                 # y al reajustarse si el iterador no se descuenta salta un elemento de la lista.
                iterador -= 1
            iterador += 1
        detalle.append((raza.razadada,contador))
    for i in detalle:
        print(f"\tRaza: {i[0]}. Cantidad: {i[1]}")
    print(f"Total de ataque: {total_ataque(ejercitos)}")

ejercito_del_bien = generador_ejercito(0)
ejercito_del_mal = generador_ejercito(1)
print("*"*6,"Tropas del ejercito del bien","*"*6)
detalle_ejercito(ejercito_del_bien)
print("\n"+"*"*6,"Tropas del ejercito del mal","*"*6)
detalle_ejercito(ejercito_del_mal)
print()
resultado(ejercito_del_bien, ejercito_del_mal)
