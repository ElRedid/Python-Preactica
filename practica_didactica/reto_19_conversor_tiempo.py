# Crea una función que reciba días, horas, minutos y segundos (como enteros)
# y retorne su resultado en milisegundos.
 
 
 
dias = int(input("Ingrese los dias para realizar el calculo: "))
horas = int(input("Ingrese las horas para realizar el calculo: "))
minutos = int(input("Ingrese los minutos para realizar el calculo: ")) 
segundos = int(input("Ingrese los segundos para realizar el calculo: "))
dias = ((((dias * 24) * 60 )) * 60) * 1000
horas = (((horas * 60 )) * 60) * 1000
minutos = (minutos * 60) * 1000
segundos = segundos * 1000

print(f"Da un total de: {dias + horas + minutos + segundos} milisegundos.")