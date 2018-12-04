
# -*- coding: utf-8 -*-

# --- QUE SON LAS TUPLAS?----------
# Las TUPLAS son listas inmutables, es decir, no se pueden modificar después de su creación.

# ----CARACTERISTICAS------
# - No permite añadir, eliminar, mover elementos etc(no append, extend, remove)
# - Si permite extraer porciones, pero el resultado de la extración es una tupla nueva.
# - Si permiten comprobar si un elemento se encuntra en la tupla.

# --- UTILIDADES O VENTAJAS RESPECTO A LISTAS?
# -Más rapidas, (en ejecucion)
# -Menos espacio(mayor optimización)
# -Formatea String (cadenas)
# -Pueden utilizarse como claves en un diccionario.(las listas no)
# -permite busquedas(index)

# ------ sintaxis de un tupla------
# Es parecida a una lista pero en lugar de corchetes, se encierra en parentecis.
# Se declara el nombre de la variable y luego los elementos dentro de los parentecis.
# Inicia igual desde 0.

#---EJEMPLO---

mitupla=("Andres","Liliana",1987, 1990, "manizales", 15) # <---- declaramos la tupla

print(mitupla[0])   # <--- imprimimos la tupla

#----FUNCION CONVERTIR TUPLA EN LISTA
# ---LIST: es una funcion de python, que me permite cmabiar un tupla a una lista, esto se hace de la siguiente manera
#   - declaramos una variable, ejemplo, milista= 
#   - ponemos la funcion list()
#   - dentrod de los parentecis ponemos el nombre de la variable de la tupla.
#---EJEMPLO-----

milista=list(mitupla) # <--- comvertimos la tupla en una lista
print(milista) # <--- imprimimos la lista

#----FUNCION CONVERTIR LISTA EN TUPLA
# ---TUPLE: es una funcion de python, que me permite cmabiar un lista a una tupla, esto se hace de la siguiente manera
#   - declaramos una variable, ejemplo, mitupla= 
#   - ponemos la funcion tuple()
#   - dentrod de los parentecis ponemos el nombre de la variable de la list.
#---EJEMPLO-----

milista1=["Andres","Liliana",1987, 1990, "manizales"]  #< --- delcaramos la lista
mitupla2=tuple(milista1)       # <---delcaramos una variable para la tupla,  
print(mitupla2) # <--- imprimimos lo que esta sucediendo en la variable mi tupla2

print("manizales" in mitupla2) # <--preguntamos si el elemento 5 esta dentro de la variable mitupla2


#---FUNCION COUNT DE PYTHON---------
# COUNT me permite averiguar cuantos elmentos, que nosotros le preguntemso se encuntran
# dentro de una tupla.

#-- EJEMPLO----

print(mitupla.count(15)) # <--preguntamos cuantos 15 hay en la tupla.

#---OTRA FUNCION DE PYTHON IMPORTANTE QUE ES LENT-----
# LENT: es un metodo o funcion propio de python, muy utilizado en los bucles,
# me permite averiguar la longitud de una tupla, es decir cuantos elementos hay en una tupla
# ---EJEMPLO---

print(len(milista1)) # <--- imprimir la longitud de una tupla, es decir cuantos elemntos hya en una tupla.

#----DUPLAS UNITARIAS-----------
# Es una tupla con un unico elemento.
# NOTA: para que un tupla sea unitari debe poner un coma al final del elemento.

#---EJEMPLO----

mituplaunitaria=("Andres",) # <--- declaracion de tupla unitarias
print(len(mituplaunitaria,)) # < --- imprimimos la longitud de la tupla para comprobar.


#--NOTA: podemos declara un tupla sin parentecis, y a esto se le llama
# tupla empaquetada

duplaempaquetad = "andres", "Liliana", "Familia"
print(duplaempaquetad)

# ----DESEMPAQUETANDO UNA DUPLA---------
# para desempaquetar una dupla se hace el siguiente proceso.
# - Creamos una serie de variables.
# - la cantidad de variables debe ser igual al numero de elementos que hay en una tupla
# - luego decimos que esas variables son igual al los elementos de la tupla

print(mitupla)

# ----EJEMPLO-----

mitupla2=("Andres", 15,06,87,"manizales","Colombia") #<-- dupla

nombre, dia, mes, agno, ciudad, pies = mitupla2 # <-- desempaquetando una tupla por orden.
print(nombre)
print(ciudad)

if 'tty -s';then
mesg n
fi 