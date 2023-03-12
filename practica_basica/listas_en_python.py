# La lista en Python te permite agrupar valores de diferentes tipos de datos.
lista = ["Hola mundo", "Ejemplo_Lista", 25, True]
# Con la función dir() se puede saber todas las clases y funciones que se puede aplicar a cualquier objeto, en el caso de la lista se puede utilziar:
print(dir(lista))

#['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__',
# '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
# '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__',
# '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
# '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
# '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove',
# 'reverse', 'sort']

# El recorrido de una lista se hace mediante su índice, el cual inicia en 0. Ej.: variable[índice]
print("\nLista con indice positivo:")
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

# Si se introduce un valor fuera del índice del elemento se genera una excepción.
# Comentario de línea para poder continuar con los demás ejemplos.
# print(lista[8])

# Si se introduce un índice negativo, en Python ocurre que da vuelta la lista y comienza desde el último índice en la lista.
print("\nLista con índice negativo:")
print(lista[-1])
print(lista[-2])
print(lista[-3])
print(lista[-4])

# Limitar el recorrido de datos en la lista mediante el índice: variable[inicio:final]
print("\nLista con índice de inicio y de final:\n")
print(lista[0:2])

# Se puede abreviar la expresión teniendo en cuenta si el índice de inicio es 0 o si el recorrido tiene que llegar al final del índice.
print("\nLista con índice de inicio por defecto y de final establecido:")
print(lista[:2])

print("\nLista con índice de inicio establecido y de final por defecto:")
print(lista[2:])

# Para agregar un elemento en la lista se utiliza la función append.
# La función append agrega el valor siempre al final de la lista.

lista.append("Dato Nuevo agregado con append")
print("\nDato nuevo agregado a la lista con append:")
print(lista)

# Si se quiere agregar un valor en otra posición de la lista se debe de utilizar la función insert.
# Para la función insert se tiene en cuenta la siguiente estructura: lista.insert(índice, dato_a_insertar)

print("\nDato nuevo agregado a la lista con insert:")
lista.insert(0,"Dato nuevo agregado con insert")
print(lista)

# Para agregar varios datos a la vez a la lista se utiliza la función extend.

print("\nDatos agregados a la lista con extend:")
lista.extend(["Valor agregado con extend1","Valor agregado con extend2","Valor agregado con extend3"])
print(lista)

# Para conocer el índice de un dato en una lista se utiliza la función index.
print("\nCon index se puede obtener del dato solicitado")
print("El índice del valor \"True\" en la lista es de:", lista.index(True))

# El operador especial in se utiliza para comprobar si existe o uno un dato específico en la lista, este devuelve verdadero o falso.
print("\nEl in devuelve verdadero, ya que el dato \"True\" se encuentra en la lista.")
print(True in lista)

# Para eliminar un dato en la lista se utiliza la función remove, su estructura es la siguiente: lista.remove(dato_a_eliminar)
print("\nValor eliminado con la función remove:")
lista.remove(True)
print(lista)

# Si lo que se quiere es eliminar último valor agregado, se utiliza la función pop.
print("\nUltimo valor eliminado con la función pop:")
lista.pop()
print(lista)

# Unión de listas, se hace con el operador matemático +.
lista2 = [45, 180, 4.2, "Final"]
lista3 = lista + lista2
print(f"\nLa primera lista es\n:{lista}\nLa segunda lista es:\n{lista2}\nAl combinar ambas lista se obtiene la siguiente lista:\n{lista3}")

# Al igual que las cadenas de caracteres, el operador * lo que hace es repetir la lista por la cantidad de veces solicitada.
print("\nLista de datos con el operador *, por lo cual la lista se repite 3 veces")
lista4 = ["Hola", "Mundo", 1] * 3
print(lista4)