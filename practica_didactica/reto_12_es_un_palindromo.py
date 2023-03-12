# Escribe una función que reciba un texto y retorne verdadero o
# falso (Boolean) según sean o no palíndromos.
# Un Palíndromo es una palabra o expresión que es igual si se lee
# de izquierda a derecha que de derecha a izquierda.
# NO se tienen en cuenta los espacios, signos de puntuación y tildes.
# Ejemplo: Ana lleva al oso la avellana.
def palindromo(cadena):
    cadena_pulida = cadena
    cadena_resultante = str()
    for i in range(1, len(cadena_pulida)+1):
        cadena_resultante += cadena_pulida[i * -1]
    # print(cadena_pulida,"\n",cadena_resultante)
    return cadena_pulida == cadena_resultante
    

entrada = input("Comprobador de palindromos: ")
cadena = str()
for i in entrada:
    if i != " " and i != "," and i != "." and i != "\'" and i != ":":
        if i == "á":
            cadena += "a"
        elif i == "é":
            cadena += "e"
        elif i == "í":
            cadena += "i"
        elif i == "ó":
            cadena += "o"
        elif i == "ú":
            cadena += "u"
        else:
            cadena += i
print(palindromo(cadena.lower()))