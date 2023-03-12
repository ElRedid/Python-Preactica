# El bucle for es un metodo de repeticion determinado, su estructura es la siguiente: for variable in elemento_a_recorrer:
lista = [1, 2, 3]
for i in lista:
    print("\nEl índice es: " + str(i), end=" ")

# El valor i no representa un numero autoincrementado para el recorrido del elemento, como lo parece en el primer ejemplo, 
# lo que hace i es almacenar cada valor del elemento en cada vuelta del bucle. 
lista1 = ["Invierno", "Verano", "Otoño", "Privabera"]
recorrido = 0
for i in lista1:
    recorrido += 1
    print(f"El valor de i en el recorrido {recorrido} es: {i}")
    
# El tipo de dato range permite utilizar el bucle for con conteos numericos, teniendo en cuenta su estructua range(inicio, fin, pasos)
# Al pasarle solo un parametro el programa entiende que rango por defecto es de 0 y debe de recorrer hasta el rango asignado.
print("\nEjemplo con rango simple:")
for i in range(10):
    print(i, end= " ")

# Al pasarle dos parametros se entiende que el primero es desde donde debe iniciar y el segundo es hasta donde deve ir.
print("\nEjemplo con 2 parametros de rango:")
for i in range(2,7):
    print(i, end=" ")

# Al pasarle 3 parametros se entiende que a parte de designar de donde y hasta donde va el bucle, tambien especifica cuantos pasos debe de dar hasta volver a realizar el conteo.
print("\nEjemplo con 3 parametros de rango:")
for i in range(2, 10, 3):
    print(i, end = " ")
    
# Para reccorrer un string con el for es tan simple como poner la cadena que se desea recorrer
cont = 0
for i in "astraromantico":
    cont += 1
print(f"\nLa cadena ingresada cuenta con {cont} caracteres")

# Es muy util para comparar cadenas o detectar parametros validos para cierta cadena.
gmail = False
for i in "correo@gmail.com":
    if i == "@":
        gmail = True
        
if gmail == True:
    print("correo valido")
else:
    print("correo no valido")
    
