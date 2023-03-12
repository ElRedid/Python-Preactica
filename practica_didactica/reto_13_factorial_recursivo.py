# Escribe una función que calcule y retorne el factorial de un número dado
# de forma recursiva.
def volvear(numero):
    base = numero
    volteado = str()
    retornar = str()
    contador = 0
    for i in range(1, len(base)+1):
        if contador < 3:
            contador += 1
            volteado += base[i * -1]
        else :
            contador = 1
            volteado += f".{base[i * -1]}"  
            
                 
    for i in range(1, len(volteado)+1):
        retornar += volteado[i * -1] 
    print(retornar)
        
    
    
numero = int(input("Calcular factorial del numero: "))
resultado = 1
for i in range(1, numero + 1):
    resultado = i * resultado

#print(resultado)
volvear(str(resultado))