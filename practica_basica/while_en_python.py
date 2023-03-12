# Los bucles while son conocidos por ser indeterminados, por lo cual, es facil general un bucle infinito si no se los maneja adecuadamente.
i = 0
while i <10:
    i += 1
    print(i, end = " ")
    
def Valor_par(num):
    if num%2 == 0:
        return "valor par"
    else:
        return "valor impar"

def Valor_primo(num):
    interador = 1
    contador = 0
    while interador < num:
        if num%interador == 0:
            contador += 1
        interador += 1
    if contador > 1 or interador == 1:
        return "no es primo"
    else:
        return "ES PRIMO"

print("Validador de numeros: ")
numero = int(input("Ingrese un numero para realizar el conteo: "))
contador = 1
while contador <= numero:
    print(f"El numero {contador} es un {Valor_par(contador)} y {Valor_primo(contador)}")
    contador += 1