# Las tuplas son, en resumen, listas inmutables, es una lista la cual no puede ser modificada.
tupla = ("elemento1", 2, True)

# Y por eso, al ejecutar la función dir retorna pocos metodos:

print(dir(tupla))

# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', 
# '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
# 'count', 'index']

# Con la tupla solo se puede utilizar los metodos count e index que ya vimos como funcionan en una lista.
# Con el metodo count se puede saber cuantos datos de coincidencia hay con respecto al parametro dado. tupla.count(elemento_buscado)
print("\nCantidad de elementos que coinciden con el elemento \"Julio\" dentro de esta tupla:")
print(tupla.count("Julio"))

# Con el metodo index se puede saber el índice del dato respecto al parametro dado. tupla.index(True)
print("\nÍndice del elemento True dentro de esta tupla:")
print(tupla.index(True))