# Las clases son un conjunto ordenado y relacionado de caracteristicas y funciones de un objeto.

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def persona(self):
        print(f"El usuario {self.nombre} {self.apellido} está registrado")
        
print("Registro de Usuario:\nIngrese el nombre:")
nombre = input()
apellido = input("Ingrese el apellido:")
persona = Persona(nombre,apellido)
persona.persona()        