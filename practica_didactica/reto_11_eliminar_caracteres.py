# Crea una función que reciba dos cadenas como parámetro (str1, str2)
# e imprima otras dos cadenas como salida (out1, out2).
# - out1 contendrá todos los caracteres presentes en la str1 pero NO
#   estén presentes en str2.
# - out2 contendrá todos los caracteres presentes en la str2 pero NO
#   estén presentes en str1.

def eliminar_carapteres(cadena_1, cadena_2):
    salida_1 = str()
    salida_2 = str()
    for i in cadena_1:
        if i not in cadena_2:
            salida_1 += i
    for i in cadena_2:
        if i not in cadena_1:
            salida_2 += i
    return salida_1, salida_2   
entrada_1 = input("Ingrese primera cadena para la comparacion:\n")
entrada_2 = input("Ingrese segunda cadena para la comparacion:\n")
resultado_1, resultado_2 = eliminar_carapteres(entrada_1, entrada_2)
print(f"Resultado de la primera cadena de texto: \" {resultado_1} \"")
print(f"Resultado de la segunda cadena de texto: \" {resultado_2} \"")