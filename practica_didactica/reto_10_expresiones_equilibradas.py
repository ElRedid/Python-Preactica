
#  Crea un programa que comprueba si los paréntesis, llaves y corchetes
#  de una expresión están equilibrados.
#  - Equilibrado significa que estos delimitadores se abren y cieran
#    en orden y de forma correcta.
#  - Paréntesis, llaves y corchetes son igual de prioritarios.
#    No hay uno más importante que otro.
#  - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
#  - Expresión no balanceada: { a * ( c + d ) ] - 5 }

parentesis_apertura, parentesis_cierre = 0, 0
llaves_apertura, llaves_cierre = 0, 0
corchetes_apertura, corchetes_cierre = 0, 0
entrada = input("Ingrese una exprecion matematica: ")

for dato in entrada:
    if dato == "(":
        if parentesis_apertura == 0:
            parentesis_apertura +=1
        else:
            parentesis_apertura = 0
    elif dato == ")":
        if parentesis_cierre == 0:
                parentesis_cierre +=1
        else:
                parentesis_cierre = 0
    elif dato == "{":
        if llaves_apertura == 0:
                llaves_apertura +=1
        else:
                llaves_apertura = 0
    elif dato == "}":
        if llaves_cierre == 0:
                llaves_cierre +=1
        else:
                llaves_cierre = 0
    elif dato == "[":
        if corchetes_apertura == 0:
                corchetes_apertura +=1
        else:
                corchetes_apertura = 0
    elif dato == "]":
        if corchetes_cierre == 0:
                corchetes_cierre +=1
        else:
                corchetes_cierre = 0
if parentesis_apertura == parentesis_cierre and llaves_apertura == llaves_cierre and corchetes_apertura == corchetes_cierre:
    print("Exprecion equilibrada.")
else:
    print("Exprecion no equilibrada.")
    if parentesis_apertura > parentesis_cierre:
        print("Existe un parentecis de apertura sin cerrar.")
    elif parentesis_apertura < parentesis_cierre:
        print("Existe un parentecis de cierre demas.")
    if llaves_apertura > llaves_cierre:
        print("Existe una llave de apertura sin cerrar.")
    elif llaves_apertura < llaves_cierre :
        print("Existe una llave de cierre demas.")
    if corchetes_apertura > corchetes_cierre:
        print("Existe un corchete de apertura sin cerrar.")
    elif corchetes_apertura < corchetes_cierre:
        print("Existe un corchete de cierre demas.")