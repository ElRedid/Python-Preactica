# Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
# - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
# - EXTRA: ¿Eres capaz de dibujar más figuras?



def figuras(figura, tamaño, largo = 0):
    if figura == 1:
    #-------------cuadrado-----------------# 
        for i in range(tamaño):
            for j in range(tamaño):
                if i == 0 or i == tamaño - 1 or j == 0 or j == tamaño - 1:
                    print("*", end= " ")
                else :
                    print(" ", end= " ")
            print()
    elif figura == 2:
    #-------------Trigangulo Isosceles-----------------#        
        for i in range(tamaño):
            for j in range(tamaño):
                if i == tamaño - 1 or j == 0 or j == i:
                    print("*", end= " ")
                else :
                    print(" ", end= " ")
            print()
    elif figura == 3:    
    #-------------Trigangulo equilatero-----------------#
        if tamaño % 2 != 0:
            diagonal_secundaria = tamaño - 1 
            salto = False      
            for i in range(tamaño):
                for j in range(tamaño):
                    if i >= ((tamaño/2)-1):
                        if i == tamaño -1 or j == i or j == diagonal_secundaria :
                            print("*", end= " ")
                        else :
                            print(" ", end= " ")
                        salto = True
                diagonal_secundaria -= 1
                if salto:
                    print()
                    salto = False
        else:
            print("Para el triangulo equilatero se necesita que el tamaño sea impar.\nVuelva a intentarlo.")
    elif figura == 4:
        #-------------Rectangulo-----------------#
        if tamaño != largo:
            for i in range(tamaño):
                for j in range(largo):
                    if i == 0 or i == tamaño - 1 or j == 0 or j == largo - 1:
                        print("*", end= " ")
                    else :
                        print(" ", end= " ")
                print()
        else:
            print("Si el largo y ancho son iguales se estaría opteniendo un cuadrado.\nVuelva a intentarlo.")


print("Bienvenido al sistema de graficos 2D.\n"+\
        "Puede seleccionar unas de las siguientes figuras:\n"+\
        "\t1.) Cuadrado.\n"+\
        "\t2.) Triangulo isosceles.\n"+\
        "\t3.) Triangulo equilatero.\n"+\
        "\t4.) Rectangulo.")
figura_input = int(input("Ingrese el numero correspondiente a la figura: "))
if figura_input == 4:
    print("Para el rectangulo debe de introducir su largo y su ancho:")
    largo = int(input("Largo: "))
    tamaño = int(input("Ancho: "))
    figuras(figura_input, tamaño, largo)
elif figura_input < 4 and figura_input > 0:
    tamaño = int(input("Tamaño: "))
    figuras(figura_input, tamaño)
else :
    print("Figura no contenplada")
