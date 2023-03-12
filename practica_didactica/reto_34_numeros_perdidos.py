# Enunciado: Dado un array de enteros ordenado y sin repetidos, 
# crea una función que calcule y retorne todos los que faltan entre
# el mayor y el menor.
# - Lanza un error si el array de entrada no es correcto.
def validador_array(array):
    array_ordenado = array.copy(); array_ordenado.sort()
    if array != array_ordenado:
        return False
    for i in range(len(array_ordenado)):
        character_analizado = array_ordenado.pop()
        if character_analizado in array_ordenado:
            return False
    return True

def numeros_entre_minimo_y_maximo(array):
    datos_faltantes = list()
    for i in range(min(array), max(array)):
        if i not in array:
            datos_faltantes.append(i)
    if len(datos_faltantes) == 0:
        print("Secuencia numerica completa, no faltan numeros entre el menor y el mayor.")
    else:
        for i in datos_faltantes:
            print(i, end=" ")
    print("\nFin del programa.")
    
def carga_datos():
    datos = list()
    while True:
        try:
            print("Ingresando datos para el array, para continuar ingrese cualquier caracter diferente a un numero.")
            caracter = int(input())
            datos.append(caracter)
        except:
            break
    if len(datos) < 2:
        print("Se necesita mas de un numero para el correcto funcionamiento del programa, vuelva a intentarlo.")
        carga_datos()
    return datos
print("Ingrese un array de enteros ordenado y sin repetidos:")
carrer = carga_datos()
if validador_array(carrer):
    print("Numeros faltantes:")
    numeros_entre_minimo_y_maximo(carrer)
else:
    print("El array introducido no cumple con los parametros.")

