#import sys
#----------CONTINUAMOS BUCLE FOR CON OTRAS FUNCIONES--------------------
#VEREMOS:
#		#Recorriendo strings
#		#Tipo de range
#		#Notaciones especiales con print

#NOTA: Cuando utilizamos la funcion print, dentro de un for, siempre hace un salto de linea.
#	   # si queremos que nos imprima todo en una sola linea, agregamos el argumento END.argumento

# ARGUMENTO END: el argumento end lo que va a determinar es como queremos que termine la impresion del elemento que esta 
#				 imprimiendo a cada vuelta del bucle, cuando ponemos end="" lo que estamos indicando es que termine la impresion con un
#				 espacio que no existe. En ultimas palabras es como decirtle que no haga salto de lineas.

# EJEPLO DE VALIDACION DE UNCORREO

# lo que hace es crear un varibale email boleana y la iniciacmo en falso,
# luego creamos for con la variable i que recorrera la cadena de texto dado.
# lugo creamos un if indicadon que si i es == al caracter dado es decir @ entonces cambie el valor del email en True.
# Luego hacemos otra condicional done indicamos que si email == al verdadero, entonces imprima email es correcto.


#email = False #----> con esto hemos inicado una variable buleana iniciada en falso

# CONTADOR  es un concepto muy utilizado a la hora de manejar bucles, tambien esta el concepto de acumulador.
# CUMULADOR  es otro concepto muy manjado en python.

"""
contador = 0 #--- hemos iniciamos la variable en 0 
miEmail = raw_input("ingrese su correo: ")

for i in miEmail:
	
	if (i=="@" or i=="."):

		contador=contador + 1 # Lo que decimos es que siempre a cada vuelta de BUCLE siempre que se cumpla una condicion, o la otra
							  # incremente la variable contador en 1, eso quiere decir que si el if no se cumple, no ingreso a la linea de 
							  # contador por lo tanto contador sigue siendo 0, luego pasa als siguiente if, como decimos que si contador
							  # es == a 2 imprima algo, pero como no se cumple por que contador no paso a 2, imprime un else.

if contador==2:
	print("Email es correcto")
else:
	print("Email No es correcto")"""


# -------------TIPO RANGE----------------
# el tipo range nos va a permitir utilizar un bucle con contadores, EL TIPO RANGE nos va a devolver algo parecido a un ARAY.
# A UN ARRAY.

for i in range(5):  # ---> lo que hace este range es crearme un array de 0,1,2,3,4, por lo tanto imprimira hola 5 veces.
	print("hola")
