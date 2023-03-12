# Crea un programa que calcule quien gana más partidas al piedra,
# papel, tijera.
# - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
# - La función recibe un listado que contiene pares, representando cada jugada.
# - El par puede contener combinaciones de "R" (piedra), "P" (papel)
#   o "S" (tijera).
# - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
def comparador_de_jugadas(dato_1, dato_2):
    if dato_1 == "R" and dato_2 == "S" or dato_1 == "S" and dato_2 == "P" or dato_1 == "P" and dato_2 == "R":
        conclusion = "Player 1 win."
    else :
        conclusion = "Player 2 win."
    return conclusion
    

def ganador(jugada_1, jugada_2):
    if jugada_1 == jugada_2:
        resultado = "Tie"
    else :
        resultado = comparador_de_jugadas(jugada_1, jugada_2)
    return resultado

entrada = [("R","S"), ("P","S"), ("P","S")]
player_1 = 0
player_2 = 0
for i in entrada:
    resultados = (ganador(i[0], i[1]))
    if resultados == "Player 1 win.":
        player_1 += 1
    elif resultados == "Player 2 win.":
        player_2 += 1

if player_1 > player_2:
    print(f"El ganador es el Player 1 con {player_1} victoria/s y {player_2} derrota/s.")
elif player_1 < player_2:
    print(f"El ganador es el Player 2 con {player_2} victoria/s y {player_1} derrota/s.")
else:
    print(f"Se registra un empate de ambos jugadores con {player_1} victoria/s.")