# Crea una función que sume 2 números y retorne su resultado pasados
# unos segundos.
# - Recibirá por parámetros los 2 números a sumar y los segundos que
#   debe tardar en finalizar su ejecución.
# - Si el lenguaje lo soporta, deberá retornar el resultado de forma
#   asíncrona, es decir, sin detener la ejecución del programa principal.
#   Se podría ejecutar varias veces al mismo tiempo.
from threading import Thread
from time import sleep
def suma(valor_1, valor_2, orden):
    sleep(5)
    print(f"\nOperacion numero:{orden}:", valor_1 + valor_2)

inicio = True
orden = 0
while inicio:
    orden += 1
    primer_valor = int(input("Primer valor: "))
    segundo_valor = int(input("Segundo valor: "))
    th_read = Thread(target= suma, args=(primer_valor, segundo_valor, orden))
    th_read.start()
    continuar =input("Desdea continuar con el programa?\nno para salir del programa: ")
    if continuar.lower() == "no":
        print("Cerrando programa....")
        sleep(2)
        inicio = False
    else :
        print("Continuando con la ejecucion del programa....")

    


