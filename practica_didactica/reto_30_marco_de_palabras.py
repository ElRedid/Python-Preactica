# Crea una función que reciba un texto y muestre cada palabra en una línea,
# formando un marco rectangular de asteriscos.
# - ¿Qué te parece el reto? Se vería así:
#   **********
#   * ¿Qué   *
#   * te     *
#   * parece *
#   * el     *
#   * reto?  *
#   **********

#------------Funcion de enmarcado---------------------------#
def frase_enmarcada(a):
    lista = a.split(sep=" ")
    maximo = 0
    for i in lista:
        if len(i) > maximo:
            maximo = len(i)
    print("**"+"*" * maximo+"**")
    for i in lista:
        print("*",i.center(maximo),"*")
    print("**"+"*" * maximo+"**")
#------------Input de datos---------------------------#    
palabra = input("Ingrese una frase para enmarcar: ")
frase_enmarcada(palabra)