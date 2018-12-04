# -*- coding: utf-8 -*-

# -----------QUE SON LAS LISTAS----------
# Son una estructura de datos que nos permite almacenar
# gran cantidad de valores(equivalentes a los array en otros lenguajes de progrmación)

# En Python las listas pueden guardar diferentes tipo de valores(en otros lenguajes no ocurre esto con los array)


# Se pueden expandir dinámicamente añadiendo nuevos elementos 
# (otra novedad respecto a los arrays entro lenguajes)

# --------SINTAXIS DE LAS LISTAS----------------
# nombre que le quiere asiganr a la lista
# y a continuacion los elemntos que forman parte de esa lista
# separados por coma y entre corchetes.
# nombreLista=[elem1,elem2,elem3....]

# Como una lista en definitiva lo que nos permite es almacenar una serie de valores
# Esos valores de una lista deben estar indentificados y localizables.
# para que esto sea posible recurrimos a lo que se llama un INDICE.
# -----INDICE---
# Es la posicion del elemento dentro de la lista, RECORDAR, que 
# una particularidad de las listas es que siempre se comienza a nuemerar
# el primer elemento de la lista con el indice o posiscion 0.
# ES DECIR: en la lista del ejemplo elem1, esta en la posicion 0.

# ------EJERCICIOS--------------------
# EJERCICIO 1: Declarando una lista.
            # imprimir la lista completa.

milista=["Maria", 5, True, 78.35] # La poscion comienza siempre en 0, y el indice en 1. 

#print(milista[:])  # <--- imprimir la lista completa.


#print(milista[2])  # <--- imprimir el elemento que esta en el indice 2, en esta caso imprime el el elemento True, por que esta en la posicion 3

#print(milista[-0]) # <--- cuando escribimos un indice negativo, lo que hace python, es contar en la lista desde el final, con la eceptcion que el primer el elemnto es -0, y el ultimo es -1,

#print(milista[0:3]) # <--PORCION: cuando tengamos listas muy largas, pues es muy probable que necesitemos acceder a una porcion de es lista, por lo que necesitamso decire a que porcion acceder de la lsita , como muestra el ejemplo. 
                    # aqui estamos indicando que por favor acceda a la primer porcion de la lista.
                    # lo que hace es imprimir indice 0, es decir el primer elemento lo incluye, despues seria el segundo indice 2, y luego el indice 3, que seria exlucive.print(milista[0:3])

#print(milista[1:3]) # <--- en este caso indicamos imprime indice 1 que es 5, y exlcuya el indice 2 que es Marta, respuest seria Pepe.

#print(milista[:3]) # <--- lo que ara este caso si no ponemos el primer indice python cuenta desde cero, quiere decir que en este ejemplo, el indice es 0, y el elemneto 3, devera devolver "Maria", "Pepe", "Marta",

print(milista[2:]) # <--- si solo ponemso el primer indice para buscar una porcion en la lista, este buscara desde el indice indicado hasta el ulimo, ejemplo si ponemos 2,mostrara dese el elementos 2 hasta el ultimo.

print(milista[2:3]) # < ---1 es el indice(No posicion)donde inicia el conteo incluyendo ese valor y 2 donde termina escluyendo ese valor.  


#------PARA AGREGAR UN ELEMENTO A ALA LISTA------

# para agregar un elemento a una lista se hace los siguiente.
# - Ponemos el nombre de la lista, ejemplo, milista
# - Agregamos .append()
# - Dentro de los parentecis ponemos el elemento que queremos agregar, ejemplo, ("Andres")
# - NOTA: .append() agrega el elemento al final.

milista.append("Andres") # <---- agregamos el lemento

print(milista[:]) # <---- imprimimos toda la lista

# ----AGREGAR ELEMENTOS EN OTRA POSICION DE LA LISTA---------
# Si queremos agregar el elemento en otra posicion, 
# tendriamos que utilizar otra funcion de python que es .insert, funciona de la siguiente manera.
# - ponemos el nombre de la lista, ejemplo, milista.
# - agregamos la funcion a utilizar que es .insert()
# - dentro de los parentecis la funcion insert nos pide 2 argumentos, que son.
#           - primero poner la posicion o indice donde queremos que quede el elemento a agregar
#           - y luego el elemento que queremos agregar.

#----EJEMPLO---

milista.insert(1,"Juan") # <-----insertamos un elemnto a una lista
print(milista[0:2])      # <---- imprimimos la lista que deceamos obtener 

#-----AGREGAR MAS DE UN ELEMENTO EN UNA LISTA-----
# Para agregar mas de un elemento a una lista utilizamos una funcion propia de python que es EXTEND.
# extend funciona de la siguiente manera.
#  - nombre de la lista, ejemplo, milista
#  - funcion de python .extend([])
#  - y dentro de los parentecis ponemos los lementos que quermos agregar dentro un corchete, como si fuera una lista.
# ----EJEMPLO.----

milista.extend(["Blanca", "Liliana", "Hernan"]) # <----- Agregamos mas de un elemento a la lista

print(milista[:]) # <---- imprimimos la lista que deceamos obtener 


#---OTRA FUNCIONALIDAD UTIL ES EL INDEX-----
# INDEX es otra funcion propia de ýthon que me devuelve el indice o posicion donde se encuntra algun elemento.
# FUNCIONA DE LA SIGUIENTE MANERA:
#   - seleccionamos la funcion de python de imprimir, print()
#   - dentro de los parentecis ponemos el nombre de la lista y la funcion index, y entre parentecis el elementos a buscar.

# EJEMPLO.

print(milista.index("Blanca"))


#---OTRA FUNCION IMPORTATE EN PYTHON ES IN-----
# IN es una funcion propia de python, que me ayud aa buscar un elemento dentro de una lista
# y devolvera un verdadero o falso si no esta.
# EJEPLO:

print("Juan" in milista) # <-- imprima  V o F si Juan esta dentro de la lista milista.

#---OTRA FUNCION IMPORTANTE PROPIA DE PYTHON ES REMOVE---
# REMOVE me ayuda a eliminar un elementode una lista, funciona de la siguiente manera.
# - primero, poner el nombre de la lista,
# - segundo, poner la funcion de python .remove()
# - y tercero, poner dentro de los parentecis el elemento a eliminar.
#----EJEMPLO:

milista.remove(True) # <---- declaramos la funcion para eliminar un elemento.
print(milista[:])    # < ---- imprimimos lo que esta sucediendo en milista

#---OTRA FUNCION PROPIA DE PYTHON PARA ELIMINAR EL ULTIMO ELEMTNO DE UNA LISTA---
# POP es una funcion de python que nos ayuda a eliminar el ultimo elemento de una lista, funciona de la siguiente manera.
# - colocamos el nombre de la lista
# - agregamos la funcion .pop()

milista.pop()   # < ---- funcion para eliminar el ultimo elemento de una lista
print(milista)  # <---- imprimimos lo que sucede en mlista


#----UTILIZANDO EL OPERADOR + DE PYTHON EN UNA LISTA--
#--- + es un operador de python que me ayuda a UNIR 2 listas.

milista2=["Colombia", 12, 1987, "Manizales", "Caldas"] # <--- declarando una segunda lista

milista3= milista + milista2  # <---- uniendo las dos lista

print(milista3[:]) # <---- imprimiendo las 2 listas


#---UTILIZANDO EL OPERADO * DE PYTHON EN UNA LISTA
# EL OPERADOR * EN UNA LISTA funciona como repetidor. Es decir,
# si colocamos luego de una lista el signo asterisco * y luego un numero 3,
# estamos indicando que me repida es lista 3 veces, ejemplo.

milista=["Maria", 5, True, 78.35] *3 # <-- declaramso las veces qeu queremso repetir una lista

print(milista[:])  # < --- imprimimos lo que esta sucediendo en milista.


