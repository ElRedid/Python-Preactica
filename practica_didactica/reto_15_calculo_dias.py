# Crea una función que calcule y retorne cuántos días hay entre dos cadenas
# de texto que representen fechas.
# - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
# - La función recibirá dos String y retornará un Int.
# - La diferencia en días será absoluta (no importa el orden de las fechas).
# - Si una de las dos cadenas de texto no representa una fecha correcta se
#   lanzará una excepción.


# Funcion que calcula cuantos días quedan en el mes teniendo en cuenta cuantos días trascurriendo utilizando el diccionario
# mediante una suma consecutiva hasta llegar al indice del mes seleccionado, posteriormente se le suma los días que ya pasaron segun la 
# fecha ingresada.
def calculo_dias(mes, dia):
    total_dias = 0
    for i in range(1, mes + 1):
        total_dias += dias_en_meses[i-1]
    return total_dias + dia

# Funcion utilizada para separar los datos en las correspondientes variables de trabajo.
def desempaquedado_fecha(fecha):
    dato = str()
    devolver = list()
    for i in fecha + "/":
        if i != "/":
            dato += i
        else :
            devolver.append(int(dato))
            dato = ""
    return devolver # Valor devuelto: una lista con elemetos int

# Validando la fecha + desempaquetado de datos
def validador_fecha(descripcion):
    validor = True
    while validor:
        dato = input(f"Ingrese la {descripcion} fecha: ")
        dia, mes, anho = desempaquedado_fecha(dato)
        if dia < 1 or dia > 31:
            print("El día no puede ser menor a 1 o mayor a 31. Vuelva a intentarlo.")
        elif mes < 1 or mes > 12:
            print("El mes no puede ser menor a 1 o mayor a 12. Vuelva a intentarlo.")
        elif anho < 1680 or anho > 2500:
            print("El año no puede ser menor a 1680 o mayor a 2500. Vuelva a intentarlo.")
        else:
            validor = False
    return dia, mes, anho        
        

dias_en_meses = {
    0 : 0,
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,              #Diccionario utilziado para tener en cuenta cuantos días trascurrieron desde la fecha ingresada
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
 
}

print("Calculo de días existentes entre dos fechas.\nLas fechas deben de estar en formato dd/mm/aaaa")

dia_1, mes_1, anho_1 = validador_fecha("primera")
dia_2, mes_2, anho_2 = validador_fecha("segunda")

dias_1 = calculo_dias(mes_1, dia_1)
dias_2 = calculo_dias(mes_2, dia_2)
total_anho =  abs(anho_1 - anho_2)
total_dias = abs(dias_1 - dias_2)
total_anho_dias = 365 * total_anho
resultado =  total_dias + total_anho_dias
print(f"Faltan en total: {total_anho} años y {total_dias} días para llegar de la fecha 1 a la fechas 2.")
print(f"En total hay: {resultado} días de distancia entre ambas fechas.")
