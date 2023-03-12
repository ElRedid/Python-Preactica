# Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
# ¿De cuántas maneras eres capaz de hacerlo?
# Crea el código para cada una de ellas.
archivo = open("practica_didactica/numeros.txt", "r")
#-------------------------Forma 1-----------------------------------#
for i in range(1, 101):
    print(i, end = " ")
print()
contador = 1
#-------------------------Forma 2-----------------------------------#
while contador <= 100:
    print(contador, end = " ")
    contador += 1
print()
#-------------------------Forma 3-----------------------------------#
print(archivo.read())
archivo.close()
#-------------------------Ya es toda we-----------------------------------#