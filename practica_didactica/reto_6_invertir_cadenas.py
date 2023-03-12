# Crea un programa que invierta el orden de una cadena de texto
# sin usar funciones propias del lenguaje que lo hagan de forma automática.
# - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

cadena = input("Ingrese una cadena de texto para invertirla: ")
iterador = 0
while len(cadena) > iterador * -1:
    iterador -= 1
    print(cadena[iterador], end="")