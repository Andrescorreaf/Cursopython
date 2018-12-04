# -*- coding: utf-8 -*-

# ---QUE SON LOS DICCIONARIOS EN PYTHON?.

# Son una estructura de datos que nos permite almacenar valores de diferente tipo
# (enteros, cadenas de textos, decimales) e incluso listas y otros diccionarios

#-----CARACTERISTICAS----------
# La principal característica de los diccionarios 
# es que los datos se almacenan asociados a una clave 
# de tal forma que se crea una asociación de tipo CLAVE:VALOR para cada elemento almacenado.

# Los elementos almacenados no están ordenados. 
# El orden es indiferente a la hora de almacenar informacón en un diccionario.

#---SINTAXIS DE UN DICCIONARIO-----.
# -Nombre que le quieras dar a un diccionario. Ejemplo, midiccionario
# -y los lementos que van dentro estan encerrado bajo llave, va primero la CLAVE , luego : y el VALOR·

#----FUNCIOANAMIENTO----------
# Se declara la variable del diccionario.
# dentro de las llaves va primero la clave, la clave puede ser de cualquier tipo (texto, numerico, una tupla, listas, diccionario)
# luego va dos puentos el valor que puedes ser de diferente tipo,(texto, numerico, lista, tupla, diccionrio).

#----EJEMPLO------

midiccionario={"Alemania":"Berlin", "Francia":"Paris", "Reio unido":"Londres", "Espania":"Madrid"}

#---- PARA AGREGAR UN ELEMENTO A UN DICCIONARIO----
# ponemos el nombre del diccionario.
# luego  en corchetes va la clave, cerramos corchetes y ponemos = y el valor.

midiccionario["Colombia"] = "manizales"

print(midiccionario)

# --------------CAMBIAR UN VALOR A UNA CLAVE----------------------
# Se hace el mismo proceso anterio, ya que lo que hace python es sobre escribir el valor asignado.

midiccionario["Colombia"]= "Bogota"
print(midiccionario)

# -------- COMO ELIMINAR UN ELEMENTO--------
# Para eliminar un elemento del diccionario utilizamos una funcion propira de python que es DEL.
# del es una funcion propia de pytho y nos sirve para eliminar un elemento del diccionario.
# la sintaxis sería: la funcion del, luego el nombre del dicionario luego dentro de corchetes la clave que se va eliminar
# NOTA: se eliminŕa la pareja completa.

# --------EJEMPLO------------------------------------------------

del midiccionario["Francia"] # <---- declaramos la linea de codigo que me elimiara la pareja del valor ingresaod en corchetes
print(midiccionario)

#----------------EJEMPLO DE UN DICCIONARIO CON VALORES DE TIPO NUMERICO ENTERO Y FLOTANTE-------------
midiccionario2={"Andres":31, "Ciudad":"manizales", "Anio de nacimieno":1987, "Dia":15, "mes":06, "estatura":1.7}
print(midiccionario2)

# -----GREGARLE VALORES A AUN DICCIONARIO MEDIANTE UNA TUPLA.
# la sistaxis seria.
# Se crea la tupl.
# luego se declara el nombre del diccionario, luego ponemos = y dentro de llaves ingresamos el nobre de la tupla, que es la
# qe va a ser la clave para los valores que se van a ingresar al diccioario, luego
# entre corchetes va la posicion de la tupla, luego dos puntos : y ya se pone el valor de la clave del diccionario.

#-------------EJEMPLO--------------------------

mitupla=("Capital de Caldas", "Capital de risaralda","Capital del Quindio")
midiccionario3={mitupla[0]:"Manizales", mitupla[1]:"Pereira", mitupla[2]:"Armenia"}
print(midiccionario3)

# ----------MOSTRAR EL VALOR DE LA CLAVE ASIGANADA AL DICCIONARIO DESDE UNA TUPLA.
# mostrar el valor de la clave asignada desde el u
print(midiccionario3["Capital del Quindio"])     #<--- de esta maera se accede al valor de un diccionario


# ----- COMO ALMACENAR UNA TUPLA EN UN DICCIONARIO JUTO CON OTROS VALORES------------
# La sintaxis es la siguientes.
# Declaramos el nombr del diccionario,
# ingresamos la clave y el valor, luego de ya tener los valores del diccionario.
# Podemos ingresar una clave y si queremso qe esa clave tenga vario valores, se hace lo siguiente; ponemos el valor que va a ser la clave
# luego ponemos dos puntos: luego en corchetes ingresamos lo valores que queremos que asignar a la clave.

# -------------EJEMPLO----------------
midiccionario4={"Liliana":23, "Dia de naimiento":24, "Ciudad y Departamento":("Manizales","Caldas")}
print(midiccionario4) 


# ----- COMO ALMACENAR UN DICCIONARIO DENTRO DE OTRO DICCIONARIO------------
# Para almacenar un diccionario dentrod e otro diccionario se realiza la siguiente declaracion:
# 1--> Declaramos el nombre del primer diccionario, luego entre llaves se ponen las claves y valores normal de las llaves.
# 2--> Despues de tener el diccionario agregamos otro dentro de este de la siguiente manera; Ponemos el el valor que le vamos a dar
#      al diccionario, luego DOS PUNTOS : , luego brimos llaves, y dentro de las llaves ponemos el valor y clave, luego de poner el VALOR:CLAVE, que necesites,
#      cierras el diccionario, y luego continuas con el otro que inciaste.

# ------ EJEMPLO-------------------------------------------


midiccionario5={"Datos usuario 1":{"Liliana":23, "Dia de nacimiento":24}, "Ciudad y Departamento":("Manizales","Caldas"),"Datos":{"Nombres":("Andres Felipe","liliana Ocampo")}}

print(midiccionario5["Datos usuario 1"])

# ---------METODOS INTERESANTES QUE SE PUEDEN UTILIZAR CON UN DICCIONARIO----------------------
# Metodos com el KEYS, VALUEs, LENG.
# El metodo KEYS, nos devuelve las claves de un diccionario.
# El metodo VALUEs, que nos devuleve los valores, diccionario.
# El metodo LENG, que nos devuelve la longitud, de un diccionario.

# -------------EJEMPLO-------------------

midiccionario5={"Datos usuario 1":{"Liliana":23, "Dia de nacimiento":24}, "Ciudad y Departamento":("Manizales","Caldas"),"Datos":{"Nombres":("Andres Felipe","liliana Ocampo")}}

print(midiccionario5.keys())  # <---- Nos devuleve todas la claves del diccionario

print(midiccionario5.values())  # <---- Nos devuleve todos los valores de las claves del diccionario

print(len(midiccionario5))  # <---- Nos devuleve la longitud del diccionario.