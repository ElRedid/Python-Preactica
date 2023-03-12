# Cuando hablamos de converciones por lo general se hace referencia a convertir un tipo de dato a otro tipo.
# En el siguiente ejemplo se puede ver como se convierte una entrada de teclado, dado que, un input siempre retorna un dato de tipo str.
# Para convertir un tipo de dato se tiene en cuenta la siguiente estructura: tipo_de_dato_deseado(tipo_de_dato_a_convertir) Ej.: int(input())
a = input("Ingrese cualquier dato, este será considerado un string\n")
b = int(input("Ingrese otro dato, este, este debe de ser de tipo numerico o arrojara una exepcion\n"))
print(type(a))
print(type(b))

# Convertir un tipo de dato sacrifica muchos recursos, por lo cual se recomienda evitarlos en la medida de lo posible
# Tambien se puede utilizar para convertir los tipos de datos complejos, como lo son las listas y las tuplas Ej.:
lista1 = ["Hola que tal", 25, False]
print(type(lista1))

# Con la funcion type para conocer el tipo de dato de la lista en efecto retorna que es de la <class 'list'>
# Pero aplicando la formula anterior para convertira la otro tipo de dato complejo se optiene que es <class 'tuple'>:
tupla1 = tuple(lista1)
print(type(tupla1))

# Para convertir una tupla a una lista es lo mismo, solo hay que tener en cuenta la formula anterior: tipo_de_dato_deseado(tipo_de_dato_a_convertir)
tupla = "Julio", 30, True
print(type(tupla))

# Desenpaquetado de datos se refuere a desempaquetar los datos guardados dentro de un tipo de dato complejo (lista, tupla, etc)
# Para ello, asignamos variables suficientes para cada dato almacenado en la tupla mediante el operador matemático "="
nombre, edad, fuma = lista1
print(f"El ususario {nombre} con edad {edad} es un fumador. {fuma}")

# Lo mismo para una tupla
nombre, edad, fuma = tupla
print(f"El ususario {nombre} con edad {edad} es un fumador. {fuma}")