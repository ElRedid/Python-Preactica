# Escribe una función que calcule si un número dado es un número de Armstrong
# (o también llamado narcisista).
# Si no conoces qué es un número de Armstrong, debes buscar información 
# al respecto.

numero = int(input("Es un numero Armstrong?: "))
calculo = 0
for i in str(numero):
    calculo += int(i) ** len(str(numero))
if numero == calculo:
    print(f"El numero {numero} es un numero Armstrong.")
else :
    print(f"El numero {numero} no es un numero Armstrong.")