
# -*- coding: utf-8 -*-
# ----FUNCIONES, PASO DE PARAMTROS---
# A continuacion veremos el paso de parametros o argumentos a FUNCIONES.

# Se trata de como hacer  para que una funcion sume diferentes numeros en cada llamada.

# RESPUESTA: Para conseguir esto (que en cada llamada sume valores diferentes),
#           utilizamos lo que se llama parametros o argumentos, que consiste en lo siguiente.
#           En la declaracion de la variable, dentro de los parentecis, lo que se hace es 
#           es declara 2 parametros o 2 argumentos, y se declaran como una variable comun y corriente.
#           Es decir aqui podriamos decir, num1, num2.
#           Al poner num1, num2, estamos indicando que: creamos una funcion la cual va arecivir 2 parametros,
# NOTA: Si declaramos 2 parametros dentro de la zona de parametros, ya no tiene sentido que los declaremos dentro de la funcion. 
# OJO:  Si tines una función que esta preparada para recibir 1 o 2 aparametros, en la llamada obligatoriamente le tienes que pasar esos 2 parametros.
#       Es decir en la primer llamada, devemos pasar 2 valores numerico si lo que queremos es que sume los 2 valores numericos.

#----EXPLICACION-----
# Lo que se esta indicando es que cuando se realiza la primer llamada, y ingreso 1 valor, 
# lo que se hace es almacenar en num1, un valor dado en parentecis en la llamada. 


#def suma(num1, num2): # <--- declaracion de la funcion
   
    #print(num1+num2)

#suma(5,7)

#suma(2,3)

#suma(35,358)


# NOTA: Los argumentos o parametros de una funcion pueden ser de diferente tipos.
# puedes utilizar variso parametros combinados. Ejemplo, 5 parametros, uno de ellos sea entero, otro un boleano, otro un float.

# ------FUNCION CON UN RETURN----
# Una funcion que devuleve un valor funciona de la siguiente manera.
# - Declaramos una variable y decimos que es variable es igual algun resultado que se espera,
# - llamamaos la funcion imprimiendo lo retornado. 

def suma(num1, num2): # <--- declaracion de la funcion
   
    resultado=num1+num2 # <--- declaracion la variable de funcion

    return resultado # <---- indicamos que nos retorne o entregue el resultado de la variable.

print(suma(5,7))   # <---- llamamos la funcion indicando que imprima el resultado. 

almacena_resultado = suma(15,16) # <--- declaramos una variable y le asignamos lo que tiene una funcion.
print(almacena_resultado)        # <--- le indicamos que imprima lo que hay en al variable antes declarada
casa = almacena_resultado + 15
print(casa)
casas2 = casa - 10
print(casas2)




#------IMPORTANCIA DE LA ANTERIOR FUNCIÓN-------
# Es que tu puedes almacenar en una variable lo que te devuleve la funcion.

# ------Ejmplo----
# almacena_resultado = suma(5,8)

# ---- EXPLICACION--------
# Lo que se hace es que dentro de la variable almacena_resultado guardamos lo que devuelve la funcion suma
# ingresando dentro del parentesis 2 parametros

# ---- UTILIDAD------------------
# Lo que acabamos de hacer, en programas complejos, nos permitiría ír utilizando a lo largo de las
# miles de lineas de codigo, que puede tener un programa complejo, pues lo que la función suma haya devuelto
# con los dos valores que le hemos pasado en algun momento, es dceir, todo lo que tengamso empaquetado o almacenado
# en una variable, y eso pues nos permite utlizarlo mas adelante en el codigo de una plaicaion compleja, las veces que queramos
# esto tiene mucha pontencialidad. 

