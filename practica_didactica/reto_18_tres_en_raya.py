# Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
# y retorne lo siguiente:
# - "X" si han ganado las "X"
# - "O" si han ganado los "O"
# - "Empate" si ha habido un empate
# - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
#   O si han ganado los 2.
# Nota: La matriz puede no estar totalmente cubierta.
# Se podría representar con un vacío "", por ejemplo.

from random import choice


# Funcion con todos los resultados posibles para el juego 3 en raya:
def comprobador_de_vicotia(elemento, matriz):
    victoria = False
    if matriz[0][0] == elemento and matriz[0][1] == elemento and matriz[0][2] == elemento:
        victoria = True
    elif  matriz[1][0] == elemento and matriz[1][1] == elemento and matriz[1][2] == elemento:
        victoria = True
    elif  matriz[2][0] == elemento and matriz[2][1] == elemento and matriz[2][2] == elemento:
        victoria = True
    elif  matriz[0][0] == elemento and matriz[1][0] == elemento and matriz[2][0] == elemento:
        victoria = True
    elif  matriz[0][1] == elemento and matriz[1][1] == elemento and matriz[2][1] == elemento:
        victoria = True      
    elif  matriz[0][2] == elemento and matriz[1][2] == elemento and matriz[2][2] == elemento:
        victoria = True
    elif  matriz[0][0] == elemento and matriz[1][1] == elemento and matriz[2][2] == elemento:
        victoria = True  
    elif  matriz[0][2] == elemento and matriz[1][1] == elemento and matriz[2][0] == elemento:
        victoria = True  
    return victoria

# Generador de matiz en formato de tabla de 3 en raya, cargado con valores "validos" aleatorios.
def generador_random_matriz():
    valores_posibles = ["X", "O", " "] # valores validos para el juego
    contador_X = 0
    contador_O = 0
    espacio_blanco = False
    
    matriz = [" ", " ", " "],\
             [" ", " ", " "],\
             [" ", " ", " "] # matiz inizializada con valores vacios/espacio para marcar el formato para la matiz en forma de tabla 3x3
             
             
    for i in enumerate(matriz): 
        for j in enumerate(matriz):
            matriz[i[0]][j[0]] = choice(valores_posibles) # cargando valores validos aleatorios a la tabla
            if matriz[i[0]][j[0]] == "X":
                contador_X += 1
            elif matriz[i[0]][j[0]] == "O":
                contador_O += 1
            else :
                espacio_blanco = True
                
    return matriz, contador_X, contador_O, espacio_blanco
 
tabla_invalida = True # filtro de tablas desiguales.
valor_X = True
valor_Y = True
while tabla_invalida:
    matriz, cantidad_X, cantidad_O, incompleto = generador_random_matriz() # Solicitando una nueva tabla aleatoria.
    valor_X = comprobador_de_vicotia("X", matriz)
    valor_Y = comprobador_de_vicotia("O", matriz)
    if abs(cantidad_X - cantidad_O) < 2:
        if not (valor_X == True and valor_Y == True):
            tabla_invalida = False

# Imprimendo la nueva tabla generada para realizar el seguimiento del juego con el resultado.
for i in enumerate(matriz):
    for j in enumerate(matriz):
        print("[",matriz[i[0]][j[0]],"]", end = "")
    print()

# Comprobando si exite ganadores en la tabla.


# Resultado entregado con la conclusion del juego.


if valor_X == False and valor_Y == False and incompleto == True:
    print("Tabla incompleta, aun no se define un ganador.")
elif valor_X == True and valor_Y == False:
    print("Ganador: Jugador X.")
elif valor_X == False and valor_Y == True:
    print("Ganador: Jugador O.")
elif valor_X == False and valor_Y == False:
    print("No hay ganadores para esta tabla.")