# Las funciones en Python son declaradas con la palabra reservada "def":

def Nombre(nombre):
    print(f"Bienvenido {nombre} al sistema")
    
def Edad_valida(edad):
    if edad > 20 :
        print("Es mayor de edad")
    elif edad < 20 :
        print("Es menor de edad")
    
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingese su edad: "))
Nombre(nombre)
Edad_valida(edad)