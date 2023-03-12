
# Crea un programa que cuente cuantas veces se repite cada palabra
# y que muestre el recuento final de todas ellas.
# - Los signos de puntuación no forman parte de la palabra.
# - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
# - No se pueden utilizar funciones propias del lenguaje que
#   lo resuelvan automáticamente.

crudo = input("Ingrese palabra:\n")
crudo = crudo.lower() + " "
palabras = list()
resultado = set()
palabra = ""
for i in crudo:
    if i != " " and i != "." and i !="?" and i != "," and i != "-" and i != "_" and i !="(" and i != ")" and i != "\'" and i != "\"" \
        and i != "{" and i != "}" and i != "[" and i != "]" and i != "\\" and i != ":" and i != ";":
        palabra = palabra + i
    else:
        palabras.append(palabra)
        palabra = ""

for i in palabras:
    contador = 0
    if i != "":
        for j in palabras:
            if j == i:
                contador += 1
        if contador == 1:
            resultado.add(f"Se encontro {contador} repeticion de la palabra \"{i}\".")  
        else :
            resultado.add(f"Se encontraron {contador} repeticiones de la palabra \"{i}\".")  

final = sorted(list(resultado))

for  i in final:
       print(i)

    
    
    
    
    
#for j in palabra:
#    if i == j:
#        contador += 1
#resultado.add(f"La palabra {i} se repite {contador} vez/veces.")
#print(resultado)