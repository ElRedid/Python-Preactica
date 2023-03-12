import numpy as np

class Video_juego:

    def __init__(self):
        self.__serie = 0
        self.__nombre = "Zelda: " 
        self.__anho = 0

    def __validador_anho(self):
        while True:
            try:
                dato = int(input("Ingrese el año: "))
                if dato >= 1900 and dato <= 2100:
                    return dato
                else: print("Dato no valido, asegurese que el año esté comprendido entre 1900 a 2100. Vuelva a intentarlo.")
            except :
                print("Para la fecha los datos deben de ser de tipo numerico. Vuelva a intentarlo.")


    def __validador_serial(self):
        while True:
            serial = input("Ingrese el serial: ")
            if len(serial) >= 5 and len(serial) <= 10 and serial[0].lower() == 'z' and serial[1].lower() == 'l':
                return serial
            else: print("El serial debe de iniciar con las letas zl seguidas de caracteres alfanumericos. Con un minimo de 3 hasta un maximo de 8 caracteres adicionales.")

    def __validador_nombre(self):
        while True:
            nombre = input("Ingrese el nombre: ")
            if len(nombre) >= 5 and len(nombre) <= 20:
                return nombre
            else : print("Nombre no valido, la extencion del nombre debe de contener caracteres alfanumericos con una extencion minima de 5 y maxima de 20. Vuelva a intentarlo.")
            

    def set_dato(self):
        self.__nombre = self.__validador_nombre()
        self.__serie = self.__validador_serial()
        self.__anho = self.__validador_anho()

    def get_info(self):
        print(f"serial: {self.__serie}")
        print(f"nombre: {self.__nombre}")
        print(f"año: {self.__anho}")

zelda = Video_juego()
#zelda.set_dato()
zelda.get_info()