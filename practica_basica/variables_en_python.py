#El tipo de variable es definido automáticamente, el contenido establece el tipo de variable del contenedor. Ej.:
a = int(input("Ingrese primer valor:\n"))
b = int(input("Ingrese segundo valor:\n"))
c = "Hola mundo"
print(type(a))
print(type(b))
print(type(c))
#En Python todo es considerado un objeto, por lo cual al imprimir el tipo de dato, muestra que pertenece a una clase correspondiente al tipo de dato.
#<class 'int'>
#<class 'float'>
#<class 'str'>

#Comparando un valor:

if a != b :
    print("El valor es diferente")
elif a == b :
    print("El valor es igual")
else :
    print("No se puede realizar a acción, error en los datos")

