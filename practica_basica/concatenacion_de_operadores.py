# Evaluacion de condiciones encadenadas
# La condicion del condicional no está limitada en cuanto a cantidad de comparadores. Ej.:
edad = 25
if 0 < edad < 100: # edad está siendo comparada para saber si es mayor que 0 y tambien para saber si es menor que 100
    print("La edad es correcta")
else:
    print("La edad es incorrecta")

# Ej. con un programa basico de comparacion de salarios.

salario_presidente = int(input("Salario para el precidente: "))
salario_administrador = int(input("Salario para el administrador: "))
salario_secretario = int(input("Salario para el secretario: "))
if salario_presidente> salario_administrador > salario_secretario:
    print(f"""\n
          El salario del director fue asignado con el valor de: {salario_presidente}.
          El salario del administrador fue asignado con el valor de: {salario_administrador}.
          El salario del secretario fue asignado con el valor de: {salario_secretario}.\n
          Datos asignados correctamente.
          """)
elif salario_presidente < salario_administrador :
    print("\n El salario del precidente debe ser mayor al de los demas.")
else:
    print("El salario del secretario no puede ser mayor al del presidente o al del administrador")
