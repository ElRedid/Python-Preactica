# Crea un programa se encargue de transformar un número
# decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
entrada = int(input("Ingrese numero que desea convertir de decimal a binario: "))
resultado = str()
while entrada >= 1:
    resto = entrada % 2
    entrada = int(entrada / 2)
    resultado = resultado + str(resto)
binario = str()
for i in range(1, len(resultado)+1):
    binario += resultado[i * -1] 
print(binario)
