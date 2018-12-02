# condicionalesII.py

# En CondicionalesI vimos la Condicion IF. En esta face
# veremos el IF, junto la instrucciones ELSE y ELIF

# Vamos a estudiar esta condicion y la instruciones, mediante
# un ejemplo que es.
# Controlar el acceso, donde nuestro preguntara la edad, si la edad
# ingresada es mayo que tal edad entonces mostrar un mensaje,
# que indique que puede pasar, si no es mayor, entonces
# que imprima un mensaje que no tien acceso.tiene



# NOTA: Cuando encontremos un else, lo podemos traducir por un 
# y si no es verdad.

# IMPORTANTE: Recordemos que si encontramos un if, inmediatamente
# lo traducciomos como un si.

# ------------ESTRUCTURA DE UN ELIF--------------------	

print("Verificacion de acceso")

nota_alumno = int(input("Introduce tu nota, por favor: "))

if nota_alumno<5:
	print("insuficiente")

elif nota_alumno<6:
	print("suficiente")

elif nota_alumno<7:
	print("Bien")

elif nota_alumno<9:
	print("Notable")

else:
	print("Sobresaliente")


#NOTA: Cuando se pone un ELIF es por que estas tomando todo el bloque
# de la condicion, es decir si la primer instruccion, no se cumple, 
# entonces si no si validar la siguiente instruccion, y asi sucesivamente
# hasta llegar al la ultima instruccion si no se cumple, ninguna de las
# anteriores.

