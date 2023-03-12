# Una excepcion es un error en tiempo de ejecuccion del programa.
# Los motivos pueden ser muy variados, pero este capturados y tratados.

def suma(num1, num2):
    return num1 * num2
while True:
    try:
        valor_1 = int(input("Ingrese primer valor: "))
        valor_2 = int(input("Ingrese segundo valor: "))
        break
    except ValueError:
        print("Los valores ingresados deben de ser numeros")
    
print("Valor de la suma:", suma(valor_1,valor_2))

# Para la captura de las excepciones se pueden utilizar las funciones de capturas.

# la capsula finally se utiliza con el metodo try, esta se ejecutara independiente de si se encuentra una excepcion o no.

def Division(num1, num2):
    return num2 / num1

try:
    valor_1 = int(input("Ingrese primer valor: "))
    valor_2 = int(input("Ingrese segundo valor: "))
except ValueError:
    print("Los valores ingresados deben de ser numeros")

try:
    resultado = Division(valor_1,valor_2)
    print("El resultado de la divicion es: ", int(resultado))
except ZeroDivisionError:
    print("No se puede dividir por 0")
finally:
    print("Fin de la division")