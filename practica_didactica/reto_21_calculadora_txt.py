# Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su
# resultado e imprímelo.
# - El .txt se corresponde con las entradas de una calculadora.
# - Cada línea tendrá un número o una operación representada por un
#   símbolo (alternando ambos).
# - Soporta números enteros y decimales.
# - Soporta las operaciones suma "+", resta "-", multiplicación "*"
#   y división "/".
# - El resultado se muestra al finalizar la lectura de la última
#   línea (si el .txt es correcto).
# - Si el formato del .txt no es correcto, se indicará que no se han
#   podido resolver las operaciones.

from sys import exit
#-------------------Funciones--------------------# 
def operaciones(operacion, dato, valor_anterior):
    if operacion == "+":
        resultado =  valor_anterior + dato
    elif operacion == "-":
        resultado = valor_anterior - dato
    elif operacion == "*":
        resultado = valor_anterior * dato 
    elif operacion == "/":
        try:
            resultado  =  valor_anterior / dato
        except ZeroDivisionError:
            resultado = valor_anterior    
    return resultado
#-------------------Apertura de fichero--------------------# 
try:        
    fichero = open("practica_didactica/calcular.txt", "r")
except :
    print("Fichero no encontrado, asegurese de que tenga en nombre calcular.txt")
    exit()
#-------------------Instancia, filtro de datos y cierre del fichero--------------------# 
datos_del_fichero = fichero.readlines()
fichero.close()
datos_limpios = list()
for i in datos_del_fichero:
    numero = str()
    for j in i:
        if j == "\n":
            break
        else:
            numero += j
    datos_limpios.append(numero)
#-------------------Resolucion del cuestionamiento--------------------# 
operacion = "+"
reserva = 0
for i in datos_limpios:
    if i != "+" and i != "-" and i != "*" and i != "/":
        resultado = operaciones(operacion, float(i), reserva)
    else:
        operacion = i
        reserva = resultado
print("{0:.2f}".format(resultado))