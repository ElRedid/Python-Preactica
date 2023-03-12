# Crea una única función (importante que sólo sea una) que sea capaz
# de calcular y retornar el área de un polígono.
# - La función recibirá por parámetro sólo UN polígono a la vez.
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# - Imprime el cálculo del área de un polígono de cada tipo.

def calcular_area(poligono: dict):
    if poligono["tipo"] == "triangulo" or poligono["tipo"] == 1:
        area = (poligono["base"] * poligono["altura"])/ 2
    elif poligono["tipo"] == "cuadrado" or poligono["tipo"] == 2:
        area = poligono["base"] ** 2
    elif poligono["tipo"] == "rectangulo" or poligono["tipo"] == 3:
        area = poligono["base"] * poligono["altura"]
    return area

validador = True
base = str
altura = str
while validador:
    print("Calculando el area de un poligono, seleccione el tipo:\n1.) Triangulo.\n2.) Cuadrado.\n3.) Rectangulo.")
    poligono = input("Seleccionar:")
    if poligono.lower() == "triangulo" or poligono == "1":
        base = int(input("Ingrese la base del triangulo: "))
        altura = int(input("La altura del triangulo: "))
        validador = False
    elif poligono.lower() == "cuadrado" or poligono == "2":
        base = int(input("Ingrese un lado del cuadrado para calcular su area: "))
        validador = False
    elif poligono.lower() == "rectangulo" or poligono == "3":
        base =  int(input("Ingrese el lago del rectangulo: "))
        altura = int(input("Ingrese el alto del rectangulo: "))
        validador = False
    else:
        print("Operacion no valida.")


dato_poligono = { "tipo" : poligono.lower(), "base" : base, "altura" : altura}
print("El area resultante es igual a",calcular_area(dato_poligono),"metros cuadrados.")
    
