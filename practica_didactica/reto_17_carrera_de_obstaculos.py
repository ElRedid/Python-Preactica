# Crea una función que evalúe si un/a atleta ha superado correctamente una
# carrera de obstáculos.
# - La función recibirá dos parámetros:
#      - Un array que sólo puede contener String con las palabras
#        "run" o "jump"
#      - Un String que represente la pista y sólo puede contener "_" (suelo)
#        o "|" (valla)
# - La función imprimirá cómo ha finalizado la carrera:
#      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
#        será correcto y no variará el símbolo de esa parte de la pista.
#      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
#      - Si hace "run" en "|" (valla), se variará la pista por "/".
# - La función retornará un Boolean que indique si ha superado la carrera.
# Para ello tiene que realizar la opción correcta en cada tramo de la pista.

from random import choices

def carrera(competidor, circuito):
    atleta = competidor
    pista = circuito
    tramo = list()
    for i in enumerate(atleta):
        if atleta[i[0]] == "run" and pista[i[0]] == "_" or atleta[i[0]] == "jump" and pista[i[0]] == "|":
            tramo.append(pista[i[0]])
        elif atleta[i[0]] == "run" and pista[i[0]] != "_":
            tramo.append("/")
        elif atleta[i[0]] == "jump" and pista[i[0]] != "|":
            tramo.append("x")
    return tramo

 
#atleta = ["run", "jump", "run", "run", "run", "jump","jump","jump","run"]
#pista = ["_", "|", "_", "_", "_", "|", "|", "|", "_" ]
#atleta = ["run", "jump", "run", "run", "run", "jump","jump","jump","run"]
#pista = ["_", "|", "|", "|", "|", "_", "_", "_", "_" ]

base_atleta = ["run", "jump"]
base_pista = ["_", "|"]
largo = int(input("Ingrese el largo de la pista en metros: "))
atleta = choices(base_atleta, k= largo)
pista = choices(base_pista, k= largo)

resultado = carrera(atleta, pista)

print(f"Atleta: {atleta}")
print(f"Pista: {pista}")
print(f"Resultado: {resultado}")

if resultado == pista:
    print("*" * 5 + f"Carrera de {largo} metros finalizada con éxito: Felicidades" + "*" * 5)
else:
    print("*" * 5 + f"Carrera de {largo} metros finalizada con errores: Vuelva a intentarlo"+ "*" * 5)
