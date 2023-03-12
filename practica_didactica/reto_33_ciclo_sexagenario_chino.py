# Enunciado: Crea una función, que dado un año, indique el elemento 
# y animal correspondiente en el ciclo sexagenario del zodíaco chino.
# - Info: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
# - El ciclo sexagenario se corresponde con la combinación de los elementos
#   madera, fuego, tierra, metal, agua y los animales rata, buey, tigre,
#   conejo, dragón, serpiente, caballo, oveja, mono, gallo, perro, cerdo
#   (en este orden).
# - Cada elemento se repite dos años seguidos.
# - El último ciclo sexagenario comenzó en 1984 (Madera Rata).

class datos:
    def __init__(self):
        self.zodiaco = ("Rata", "Buey", "Tigre", "Conejo", "Dragón", "Serpiente", "Caballo", "Oveja", "Mono", "Gallo", "Perro", "Cerdo")
        self.wu_xing = ("Madera", "Fuego", "Tierra", "Metal", "Agua")
        self.inicio = 1924
        
def calendario_chino(dato):
    print("Bienvenido, ingrese el año que desea conocer el elemento y animal zodiacal:")
    entrada = int(input())
    entrada = validador(entrada)
    anho_salida = entrada - dato.inicio
    cont_zodiaco = 0
    for i in range(anho_salida):
        if cont_zodiaco < 11:
            cont_zodiaco +=1
        else:
            cont_zodiaco = 0
    while True:
        if anho_salida - 10 >=0:
            anho_salida -= 10
        else:
            break
    resultado = int(anho_salida/2)
    print(f"Para el año {entrada}.","\nEl elemento es:",dato.wu_xing[resultado], "\nEl animal es:", dato.zodiaco[cont_zodiaco])  

def validador(parametro):
    while parametro < 1924:
        parametro = int(input("El año no puede ser menor a 1924, vuelva a intentarlo: "))
    return parametro      
dato = datos()
calendario_chino(dato)


