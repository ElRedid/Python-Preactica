# Para los diccionarios hay que tener en cuenta de los datos estan representados por una clave y un valor.
# Estructira basica de un diccionario: variable = { "clave unica" : valor }
# Con respecto para el valor este tambien puede almacenar listas, tuplas, o incluso otros diccionarios.
cod, nombre = 1, "Julio"
mi_diccionario = {
    "codigo" : cod,
    "nombre" : nombre    
}

print(mi_diccionario)

# Con la funcion dir() se puede optener todas sus clases o funciones.
print(dir(mi_diccionario))

# ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__',
# '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__',
# '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__',
# '__str__', '__subclasshook__',
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault','update', 'values']

# Para agregar nuevos valores a un diccionario se puede hacer nombrando al diccionando, pasandole el parametro o valor clave entre corchete e igualandolo al dato que quiere
# ser almacenado. Ej.: nombre_diccionario["clave"] = valor_a_almacenar
mi_diccionario["actividad"] = "activo"
print("\nDiccionario en Python:")
print(mi_diccionario)

# Para sobre-esbrivir un dato es tan simple como pasarle la clave que se desea modificar junto al nuevo valor
mi_diccionario["nombre"] = "Analia"
print("\nSobre-escribiendo un dato en el diccionario:")
print(mi_diccionario)

# Para eliminar se utliza la plabra reservada del, se selecciona el diccionario correspondiente, junto a la clave, este será eliminada con el dato asociado a ella.
del mi_diccionario["actividad"]
print("\nEliminando un dato en el diccionario:")
print(mi_diccionario)

# La asignacion de la clave puede ser cualquier dato con tal que sea unico, como por ejemplo los mismos datos de una tupla.
tupla = "Nombre", "edad", 0
diccionario = {tupla[0] : "Julio", tupla[1] : 25, tupla[2] : "Licenciado"}
print("\nDiccionario tomando como clave una tupla:")
print(diccionario)


# Como se habia dicho previamente, en un diccionario tambien se puede almacenar listas, tuplas e incluso otros diccionarios
lista1 = ["Julio", 25, False]
tupla1 = "Analia", 26, True
diccionario2 = {"usuario" : "Roberto", "Alias" : "Chupamimuñaño"}
diccionario1={
    "lista1" : lista1,
    "tupla1" : tupla1,
    "diccionario2" : diccionario2
}
print("\nDiccionario tomando valores a una lista, una tupla y otro diccionario:")
print(diccionario1)

