# Crea una función que imprima los 30 próximos años bisiestos
# siguientes a uno dado.
# - Utiliza el menor número de líneas para resolver el ejercicio
from calendar import isleap
def anhos_bisiestos(anho):
    count = 0
    print(f"30 Años bisiestos despues del {anho} ")
    anho += 1
    while count < 30:
        if isleap(anho):
            print(anho, end=" ")
            count+=1
        anho+=1
print("Años bisiestos en un rango de 30 años, ingrese la fecha")
anho = int(input())
anhos_bisiestos(anho)