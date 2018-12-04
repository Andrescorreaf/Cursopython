
# -*- coding: utf-8 -*-
# ----------QUE ES UNA FUNCION?
# Una funcion es un conjunto de líneas de código agrupadas (bloque de codigo)
# que funcionan como una unidad realizando una tarea especifica. 

# las funciones en Python pueden O no devolver valores.
# Las funciones en Python pueden tener O no parámetros/argumentos.
# A las funciones tambien se las denomina "metodos" cuando se
# encuentran definidas dentro de una clase.

#----------UTILIDADES-------------
# Principal utilidad de una funcion aunque no unica es 
# poder Reutilizar el código(cuando sea necesasio o si es necesario) pero seria extraño.

#---------LA SINTAXIS DE UNA FUNCION-----------------
# La sintaxis de una funcion es la siguiente.

# def = es una palabra reservada de python. luego. 
# nombre_funcion = igual a como se declara una variable, se coloca la incial con mayuscula. Nombre_funcion(parametros):
# () = parentecis, zona de parametros o zona de argumentos. Luego.
# : = donde termina la primer linea para declarar la funcion. Luego.
# las instrucciones que híran dentro de esa función con una pequeña identacion.
# Nota: la identacion es fundamental ya que le indica a python que esas instrucciones hacen parte de esa funcion. 
# return() = Luego de las instrucciones la funcion puede llevar dentro una return (es opcional).
# el return tiene que ver con la devolucion de valores, si la funcion necesita devolver valores lleva return si no, no lleva return.

#-------------------EJEMPLO---------------------------------------------

# Sintaxis 1:
# def nombre_función(): # parabra reservada def, a continuacion nombre de la funcion y luego los paraentecis.
    # instrucciones de la función # luego la instruccion, dionde se indica que es lo que se quiere hacer con es funcion. 
    # return (opcional)           # el return tiene que ver con la devolucion de valores, es decir si la funcion tien que devolver valores lleva el retorn, si no no se le pode retorn 


# Sintaxis 2: con argumentos. Es decir esta funcion recive parametros, o argumentos. 

# def nombre_función(parámetros):
    # instrucciones
    # return (opcional)


# NOTA: dentro de los parentecis se les llama zona de parametros.

# return: recordemos que una funcion puede devolver valores
        # si la funcion devulve valores lleva return
        # si NO devulve valores pues no lo lleva.

# NOTA: En la segunda funcion vemos que dentro de los parentecis hay argumentos
        # esto quiere decir que esta funcion recive parametros o argumentos.


# ---------------PARA LA EJECUCION FUNCION-----------
# para ejecutar una funcion, 
# unicamente se escribe el nombre de la funcion y los parenteis vacios, por que no recive parametros.
# en el caso que la funcion recive parametros se escribe el nombre de la funcion
# y entre parentecis los parametros necesarios.


#----------EJEMPLO----------------
# Antes de empezar debemos recordar algo importante de la utilidad de uan funcion y es la reutilidad de esa funciones.
# NOTAS: Dentro de una funcion tenemos las funciones predefinidas y las funciones popias.
    # LAS FUNCIONES PREDEFINIDAS: son las que se nos proporcionan con el lenguaje de programacion de turno,
        # en este caso Python, como por ejmeplo; print(). Print es una fucion predefinidia de Python, que podemos 
        # utilizar dentro de nuestra PROPIA funcion.
    # FUNCIONES PROPIAS: esta es creadas por el propio desarrollador y pueden ser utilizadas en el futuro.   

#print("estamos aprendiendo Python") # recordar que cada line es una insturccion.
#print("estamos aprendiendo instrucciones basicas") # segunda linea o instruccion
#print("estamos aprendiendo avanzando") # tercer liena o instruccion

# Nota si queremos que la anterior instruccion o instrucciones se repita varias veces
# Es mejor que meterla en una funcion, puesto que la otra manera es copiar y pegar varias veces el codigo.
# pero si copia y pega varias veces una instruccion podria hacer el codigo mas largo.

# En el siguiente proceso vamos a poner las instrucciones dentro de una funcion

# NOTA: Una funcion, NUNCA va arealizar su tarea hasta que esta funcion no es llamada.

# --------DECLARAMOS LA FUNCION-----------

def mensaje(): # <----- esto es LA DECLARACION DE LA FUNCIÓN----

    print("estamos aprendiendo Python")
    print("estamos aprendiendo instrucciones basicas") # <---las lineas que aparecen identadas serian EL CUERPO DE LA FUNCIÓN
    print("estamos aprendiendo avanzando")

# NOTA:  la anterior funcion NO hace nada hasta que SEA LLAMADA.

# ------- COMO LLAMAR UNA FUCNION?-------------

# Se escribimos el nombdre de la fucnion y los parametros, fuera de la funcion. 

mensaje() # <--esta seria la LLAMADA A LA FUNCIÓN, y traerá todo lo que esta dentro de la funcion, en este caso imprimir()

mensaje() # <------- PUEDES LLAMAR LA FUNCIONA CUANTAS VECES DECEE y agregarle algun mensaje.
print("ejecutando codigo fuera de la funcion")

# Nota: recordar que el flujo de ejecuccion de un progrma siempre va de arriba abajo. 
# ecepto cuando se encuntre con una funciones y bucles.

mensaje()
print("EJECUTANDO CODIGO FUERA DE LA FUNCION") # <--NOTA: dentro de cada llamda a una funcion pued baer otras lineas de codigo.