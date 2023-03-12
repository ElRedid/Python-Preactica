# Simula el funcionamiento de una máquina expendedora creando una operación
# que reciba dinero (array de monedas) y un número que indique la selección
# del producto.
# - El programa retornará el nombre del producto y un array con el dinero
#   de vuelta (con el menor número de monedas).
# - Si el dinero es insuficiente o el número de producto no existe,
#   deberá indicarse con un mensaje y retornar todas las monedas.
# - Si no hay dinero de vuelta, el array se retornará vacío.
# - Para que resulte más simple, trabajaremos en céntimos con monedas
#   de 5, 10, 50, 100 y 200.
# - Debemos controlar que las monedas enviadas estén dentro de las soportadas.
monedas_validas = (200, 100, 50, 10, 5)
productos = { 
            1 : ["Agua 200ml", 525],
            2 : ["Agua con gas 200ml", 645],
            3 : ["Agua 500ml", 850],
            4 : ["Agua con gas 500ml", 965],
            5 : ["Coca Cola 200ml", 1225],
            6 : ["Pepsi Cola 200ml", 1225],
            7 : ["Coca Cola 500ml", 1650],
            8 : ["Pepsi Cola 500ml", 1650],
            9 : ["Jugo de Naranja", 995],
            10 : ["Jugo de Manzana", 995],
}
def maquina_expendedora(saldo = 0):
    print("Maquina expendedora, productos disponibles.")
    for i in productos:
        print(f"\t{i}.", (productos[i])[0] + ". Precio:", (productos[i])[1])
        
    print("Saldo disponible de:", saldo) 
def ingresando_monedas(reintento = 0):
    print("Monedas aceptadas: 5, 10, 50, 100 y 200 centavos.\nPara finalizar con la introduccion de monedas ingrese \'continuar\'")
    monto_total = list()
    resultado = 0 + reintento
    
    while True:
        entrada = input()
        if entrada == '5' or entrada == '10' or entrada == '50' or entrada == '100' or entrada == '200':
            monto_total.append(int(entrada))
        elif entrada.lower() == 'c' or entrada.lower() == 'continue' or entrada.lower() == 'continuar':
            break
        else :
            print("Valor no valido, vuelva a intentarlo.")

    for i in monto_total:
        resultado += i
        
    maquina_expendedora(resultado)
        
    return resultado
def validador(numero):
    try:
        return int(numero)
    except:
        return 0
def seleccion_producto():
    print("Seleccione el producto por su numero en la lista.")
    while True:
        seleccion = input()
        indice = validador(seleccion)
        if  indice in productos:
            descripcion = (productos[indice])[0]
            costo_producto = (productos[indice])[1]
            return descripcion, costo_producto
        else:
            print("Producto no disponible, seleccione otro producto.")
def cancelacion_compra(vuelto):
    print(f"Compra cancelada, retire su cambio de la boquilla de cambios, el total de: {vuelto} centavos")
    retorno_moneda(vuelto)
def compra(total, costo, descripcion):
    if total >= costo:
        print(f"Desea confirmar la compra del producto {descripcion} con el valor de {costo} centavos? (Y/n)")
        cerrar_compra = input()
        if cerrar_compra.lower() == 'y' or cerrar_compra.lower() == 'yes' or cerrar_compra.lower() == 's' or cerrar_compra.lower() == 'si':
            if total > costo:
                cambio = total - costo
                print(f"Compra realizada, puede retirar su producto: {descripcion}. Su cambio a recibir es de: {cambio} centavos.")
                retorno_moneda(cambio)
            else :
                print(f"Compra realizada, puede retirar su producto: {descripcion}.")
            
        else:
            print("Desea seleccionar otro producto? (Y/n)")
            cambio_producto = input()
            if cambio_producto.lower() == 'y':
                maquina_expendedora(total)
                nuevo_pedido = seleccion_producto()
                compra(total,nuevo_pedido[1], nuevo_pedido[0])
            elif cambio_producto.lower() =='n':
                cancelacion_compra(total)
                
                
    else :
        print(f"El costo del producto seleccionado: {descripcion} es de: {costo} centavos, usted a ingresado el todal de {total} centavos, es monto es insuficiente, continuar con la compra ingrese \'continuar\' y agrege el valor faltante, ingrese cualquier valor para cancelar la compra.")
        continuar_compra = input()
        if continuar_compra.lower() == 'continuar':
            nuevo_ingreso_monedas = ingresando_monedas(total)
            total = nuevo_ingreso_monedas
            compra(total, costo, descripcion)
        else:    
            cancelacion_compra(total)   
def retorno_moneda(monedas):
    salida_monedas = list()
    for i in monedas_validas:
        total_monedas = 0
        if monedas / i >= 1:
            total_monedas = int(monedas/i)
            monedas = monedas - (i * total_monedas)
            salida_monedas.append(f"Monedas de {i}: {total_monedas}")
    for i in salida_monedas:
        print(i)
    

maquina_expendedora()
total_ingresado = ingresando_monedas()
descri_producto, costo_producto = seleccion_producto()
compra(total_ingresado, costo_producto, descri_producto)


    