# Escribe un programa que se encargue de comprobar si un número es o no primo.
# Hecho esto, imprime los números primos entre 1 y 100.

for i in range(2, 101):
    contador = 0
    for j in range(1, i):
        if i % j == 0:
            contador += 1
    if contador < 2 :
        print(f"{i} es primo.")
    
