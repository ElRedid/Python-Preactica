# Escribe una función que reciba dos palabras (String) y retorne
# verdadero o falso (Bool) según sean o no anagramas.
# Un Anagrama consiste en formar una palabra reordenando TODAS
# las letras de otra palabra inicial.
# NO hace falta comprobar que ambas palabras existan.
# Dos palabras exactamente iguales no son anagrama.

def palabras(palabra_1: str, palabra_2: str):
    anagrama = True
    if palabra_1.lower() == palabra_2.lower():
        anagrama = False 
    elif len(palabra_1) == len(palabra_2) and sorted(palabra_1.lower()) == sorted(palabra_2.lower()):
        anagrama = True
    else:
        anagrama = False
    return anagrama

print("Ejercicio Anagrama.")
palabra_1 = input("Ingrese primera palabra: ")
palabra_2 = input("Ingrese segunda palabra: ")
anagrama = palabras(palabra_1, palabra_2)
if anagrama:
    print("Es un anagrama.")
else:
    print("No es un anagrama.")