# Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra
# que calcule el mínimo común múltiplo (mcm) de dos números enteros.
# - No se pueden utilizar operaciones del lenguaje que 
#   lo resuelvan directamente.

#------------------------Funcion que genera los numeros naturales del valor dado--------------------------------------#
def numeros_naturales(valor_mcm):
    lista_numeros_naturales = list()
    for i in range(1, 101):
        lista_numeros_naturales.append(i * valor_mcm)
    return lista_numeros_naturales
#------------------------Funcion de calculo mcd y mcm--------------------------------------#
def mcd(valor_1, valor_2):
    mayor = int()
    for i in range(1, valor_1 + 1):
        if valor_1 % i == 0 and valor_2 % i == 0:
            mayor = i
    return mayor
def mcm(valor_1, valor_2):
    resultado = list()
    valor_natural_1 = numeros_naturales(valor_1)
    valor_natural_2 = numeros_naturales(valor_2)
    for i in valor_natural_1:
        if i in valor_natural_2:
            resultado.append(i)
    return resultado[0]
#------------------------Datos y llamada de metodos--------------------------------------#
valor_1 = 24
valor_2 = 31
if valor_1 < valor_2:
    contenedor = valor_1
    valor_1 = valor_2
    valor_2 = contenedor
if valor_1 != 0 and valor_2 != 0:
    print(f"El maximo comun divisor de {valor_1} y {valor_2} es:", mcd(valor_1, valor_2))
    print(f"El minimo comun multiplo de {valor_1} y {valor_2} es:", mcm(valor_1, valor_2))
else :
    print("El valor 0 no es contemplado para estos calculos.")