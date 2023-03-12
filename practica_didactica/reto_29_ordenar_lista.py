# Crea una función que ordene y retorne una matriz de números.
# - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
#   adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
#   o de mayor a menor.
# - No se pueden utilizar funciones propias del lenguaje que lo resuelvan
#   automáticamente.
#------------Vector de prueba ------------------#
lista = [2, 5, 3, 100, 1, 8 ,4, 500, 87, 83, 62]
#------------------ Solucion con metodos directos del sistema-----------------#
def orden_vector_con_funcion_de_sistema(seleccion,vector: list):
    
    if seleccion == '1' or seleccion.lower() == "ascendente" or seleccion.lower == "asc":
        vector.sort()
        print_vector(vector)
    elif seleccion == '2' or seleccion.lower() == "descendente" or seleccion.lower == "desc":
        vector.sort(reverse= True)
        print_vector(vector)
    else:
        print("Valor no valido, vuelva a intentarlo.")
#------------------ Solucion sin metodos directos del sistema-----------------#
def orden_vector_sin_funcion_de_sistema(seleccion, lista: list):
    lista_ordenada = list()   
    if seleccion == '1' or seleccion.lower() == "ascendente" or seleccion.lower == "asc":
        for i in lista:
            lista_ordenada.append(i)
            iterador = 0
        while iterador < len(lista_ordenada):
            if lista_ordenada[iterador] < lista_ordenada[iterador - 1]:
                aux = lista_ordenada[iterador - 1]
                lista_ordenada[iterador - 1] = lista_ordenada[iterador]
                lista_ordenada[iterador] = aux
                iterador = 0
            iterador += 1
        print_vector(lista_ordenada)
    elif seleccion == '2' or seleccion.lower() == "descendente" or seleccion.lower == "desc":
        for i in lista:
            lista_ordenada.append(i)
            iterador = 0
            while iterador < len(lista_ordenada):
                if lista_ordenada[iterador] > lista_ordenada[iterador - 1]:
                    aux = lista_ordenada[iterador - 1]
                    lista_ordenada[iterador - 1] = lista_ordenada[iterador]
                    lista_ordenada[iterador] = aux
                    iterador = 0
                iterador += 1
        print_vector(lista_ordenada)
    else:
        print("Valor no valido, vuelva a intentarlo.")
#------------------Imprimiendo resultado-----------------#
def print_vector(vector_ordenado: list):
    for i in vector_ordenado:
        print(i, end=" ")
    

#------------------Insercion de datos-----------------#
# Se puede extender el ejercicio insertando un vector propio            
print("Ordenar vector de forma ascendente o descendente:\n\t1.) Ascendente o Asc\n\t2.) Descendente o Desc.")
input_dato = input("Seleccione una de las opciones: ")
#orden_vector_con_funcion_de_sistema(input_dato, lista)
orden_vector_sin_funcion_de_sistema(input_dato, lista)