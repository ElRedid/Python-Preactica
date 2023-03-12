# Crea un programa que determine si dos vectores son ortogonales.
# Los dos array deben tener la misma longitud.
# Cada vector se podría representar como un array. Ejemplo: [1, -2]

#-------------función ortogonal-----------------#
def arreglo_ortogonal(primer_vector, segundo_vector):
    resultado = 0
    for i in zip(primer_vector,segundo_vector):
        resultado += i[0] * i[1]
    if resultado == 0:
        return True
    else:
        return False

#-------------función creando vectores (x,y)-----------------#    
def creando_vectores():
    vector = list()
    limite = 0
    while limite < 2:
        limite += 1
        vector.append(int(input(f"Ingrese el valor numero {limite} para el vector: ")))
    return vector

#-------------Resolucion del reto-----------------#
print("Crenado primer vector.")
vector_1 = creando_vectores()
print("Crenado segundo vector.")
vector_2 = creando_vectores()
conclucion = arreglo_ortogonal(vector_1, vector_2)

#-------------Impresion del resultado-----------------#
if conclucion:
    print(f"El vector {vector_1} y el vector {vector_2} son ortogonales.")
else:
    print(f"El vector {vector_1} y el vector {vector_2} no son ortogonales.")
