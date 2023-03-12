# Crea una función que reciba dos array, un booleano y retorne un array.
# - Si el booleano es verdadero buscará y retornará los elementos comunes
#   de los dos array.
# - Si el booleano es falso buscará y retornará los elementos no comunes
#   de los dos array.
# - No se pueden utilizar operaciones del lenguaje que
#   lo resuelvan directamente.

#------------------------Opteniendo valores diferentes de los arrays--------------------------------------#
def diferentes(array_1, array_2):
    array_optenido = set()
    for i in array_1:
            unico = True
            for j in array_2:
               if i == j:
                    unico = False
                    break      
            if unico:
                array_optenido.add(i)
    return array_optenido 
#------------------------Generando nuevo array--------------------------------------#
def new_array(array_1, array_2, operador):
    array_optenido = set()
    if operador == True:
        for i in array_1:
            for j in array_2:
                if i == j:
                    array_optenido.add(i)
                    break
    elif operador == False:
        array_optenido = set(list(diferentes(array_1, array_2)) + list(diferentes(array_2, array_1)))
    else:
        array_optenido = "Error en el operador de los datos."
    return array_optenido
#------------------------Inicializando variables operativas--------------------------------------#
array_1_creacion = ["hola", "que tal", 425, True, "alma marsela goso", "Julio", "Mario" ]
array_2_creacion = [421, "que tal", False, True, "hola", "hola", "Romero", "hola", "Mario"]
operador_creacion = False
#------------------------Ordenando arraus segun longitud--------------------------------------#
if len(array_1_creacion) < len(array_2_creacion):
    contenedor = array_1_creacion
    array_1_creacion = array_2_creacion
    array_2_creacion = contenedor
#------------------------Llamando a la funcion e imprimiendo el resultado--------------------------------------#
print(new_array(array_1_creacion, array_2_creacion, operador_creacion))