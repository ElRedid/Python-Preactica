# Su sintaxis es muy parecida a la de la funcion.

def GenerarNumeros(numeros):
    yield numeros
    
# Por lo general en cuanto a sintaxis la diferencia es que un generador generalmente utiliza la palabra reservada yield.
# Esta estructura se utiliza cuando se quiere devolver los valores optenidos de uno en uno, por cada vez que es llamada la funcion se optiene el siguiente valor.

# Para ver la diferencia claramente, la compararemos con una funcion ya conocida.

def GeneraPares(limite):
    num = 1
    lista = []
    while num < limite:
        lista.append(num * 2)
        num += 1
    return lista

print(GeneraPares(10))

# Su equivalente en generador es:

def GeneraPares2(limite):
    num = 1
    while num < limite:
        yield num * 2
        num += 1
    
pares = GeneraPares2(10)
for i in pares:
    print(i, end = " ")
    
# El objeto generador entra en estado de suspencion hasta que se haya utilizado todos sus valores, por ejemplo el siguiente generador va mostrando los numeros con la funcion next.

def GeneraPares3(limite):
    num = 1
    while num < limite:
        yield num * 2
        num += 1
    
pares = GeneraPares3(10)
print("\nPrimera llamada")
print(next(pares))
print("Segunda llamada")
print(next(pares))
print("Tercera llamada")
print(next(pares))

# Para cuando se necesite trabajar con bubles anidados dentro de la funcion, se puede utilizar el yield from, el cual, permite presindir del buble anidado.

def Devuleve_ciudades(*ciudades):
    for elemento in ciudades:
        yield from elemento

ciudades_devueltas = Devuleve_ciudades("Ciudad del Este", "Asuncion", "Encarnacion", "Minga")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))