# Dado un listado de números, encuentra el SEGUNDO más grande.

def ingreso_datos(datos = set()):
    numeros = datos
    print("Bienvenido al reto 32, donde se tiene que encontrar el segundo valor mas grande.\nIngrese los numeros, para salir ingrese cualquier valor diferente a un numero.")
    while True:
        new_data = input()
        try:
            numeros.add(int(new_data))
        except:
            break
    return numeros

def imprimiendo_el_segundo_mayor(datos):
    try:
        datos.remove(max(datos))
        print(f"El segundo numero mayor ingresado es el {max(datos)}.")
    except:
        print("Se necesita minimo dos numeros ingresados para que el programa funcione.")

input_data = ingreso_datos()
imprimiendo_el_segundo_mayor(input_data)