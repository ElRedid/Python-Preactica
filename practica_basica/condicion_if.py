# Condicional if se utiliza para tomar una decicion o un rumbo de accion teniendo en cuenta si se cumple la sentencia validadora.
a = 2023
b = int(input("Ingrese su año de nacimiento: "))
if a - b >= 18:
    print("Es mayor de edad.")

# Cuando se quiere tomar una accion cuando no se cumple la condicion se utiliza la palabra reservada else.
if a - b < 18 and a - b > 0:
    print("Es menor de edad")
else:
    print("Es mayor de edad")
    
# Cuando se quiere definir mas rumbos de accion dentro del if existen los if anidados, que tambien se puede utilizar la palabra reservada elif
if a - b <= 18 and a - b > 0:
    print("Es menor de edad.")
elif a -b >= 18 and a - b > 0:
    print("Es mayor de edad.")
else:
    print("Error al introducir los datos")
    
# Ejemplo de validacion de correo con instruccion condicional If
correo = input("Ingrese su correo: ")
    
if "@gmail.com" in correo or "@hotmail.com" in correo:
    print("Valido")
else:
    print("No valido")
