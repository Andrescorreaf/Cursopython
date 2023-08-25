# ----------CondicionalesIII.py-------------------
# En Condicionales II:
# vimos el uso de la estructura de la condicion IF.

# -------CONDICIONALES SWITCH------------------
# para esta tercera parte veremos la condicional Swith. 
# Switch: En otros leguanje esta instruccion es muy comun, pero en python
# no existe esta instruccion ya que como python es un lenguaje demaciado simple,
# decidieron no agregar esta funcion ya que hace exactamente lo mismo que un if.

# El switch se utiliza en otros lenguajes cuando hay que evaluar muchas condiciones
# encadenadas, es decir muchas posibilidades. 

# Una de las alternativas que ofrece python es por ejemplo el uso de diccionarios,
# cuando hay que evaluar muchas condiciones a la vez.

# Y otra alternativa es utilizar la CONCATENACION de operadores ofrecidos por python. 

# CONCATENACION DE OPERADORES DE COMPARACION, a la hora de construir un condicional,
# esto nos va  a permitir evaluar un monton de condiciones encadenadas. 

# OPERADORES LOGICOS AND y OR, que son utlizados en otros lenguajes y se pueden utilizar
# en python que nos permite evaluar varias condiciones.

# OPERADOR IN, que al igual que es utilizado en otros lenguajes, tambien es utilizado en python.
# que permite evaluar varias condiciones.


#----------VEREMOS EL USO DE LA CONCATENACION DE OPERADORES LOGICOS------

edad = 7

if 0<edad<100:# ----> Esta es una concatenacion de operadores de comparacion, esto lo lee de izquierda a derecha.
			  # quiere decir que si esta primer condicion 0<edad es falsa, inmediatamente salta hasta el else, y no coninua lellendo la instruccion,
			  # pero si 0<edad es verdadero entonces continua leyendo la linea y hace la siguiente comparacion edad<100, si es verdadero imprime, o sino (else), imprime.
	print("Edad es correct")
else:
	print("Edad incorrecta")


#-----------OTRO EJEMPLO------------------------
# EL CASO DE USO ES:
# Crear un progrma que evalue el salario de una serie de personas
# que laboran en una empresa. Vamos a evaluar el salario de presidente de la empresa,
# el de un director, el de un jefe de area y el de un administrativo. 
# Lo que se hace es evaluar que cada salario es diferente por su puesto de trabajo.

salario_presidente= int(input("Ingrese el salario del presidente: "))
print("salario_presidente: " + str(salario_presidente))

salario_director= int(input("Ingrese el salario del director: "))
print("salario_director: " + str(salario_director))

salario_jefe_area= int(input("Ingrese el salario del jefe_area "))
print("salario_jefe_area: " + str(salario_jefe_area))

salario_administrativo= int(input("Ingrese el salario del administrativo: "))
print("salario_administrativo: " + str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
	print(" Todo funciona adecuadamente")
else:
	print("hay fallas en los pagos")






