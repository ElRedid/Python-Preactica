# Crea una función que reciba un String de cualquier tipo y se encargue de
# poner en mayúscula la primera letra de cada palabra.
# - No se pueden utilizar operaciones del lenguaje que
#   lo resuelvan directamente.

def mayusculas(palabra):
    mayusculas = True
    resultado = str()
    for i in palabra:
        if mayusculas:
            resultado += i.upper()
        else:
            resultado += i
        if i == " ":
            mayusculas = True
        else:
            mayusculas = False
    return resultado

palabra = input("Ingrese una palabra en la cual cada letra inicial será convertida en mayusculas:\n")
print(mayusculas(palabra))