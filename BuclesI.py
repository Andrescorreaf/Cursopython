# -*- coding: utf-8 -*-

#-------------------HOY VEREMOS LOS BUCLES---------------

# Los bucles, es repetir una linea de codigo varias veces, o
# hacer que vairas lineas de codigo se repita varias veces.
# El bucles es una estructura de control de flujo.

#--------------TIPOS DE BUCLES-------------------

# Hay varios tipos de bucles, aquellos lenguajes que cuentan
# con bucles como estructura de control de flujo. Tienen 2 tipos de bucles.
# Tienen 2 tipos de bucles.

# BUCLES DETERMINADOS: 
# Se ejecutan un numero determinado de veces.
# Se sabe a priori cuantas veces se va a ejecutar el codigo del interior del bucle.

# BUCLES INDETERMINADOS:
# Se ejecutan un numero indeterminado de veces.
# No sabe a priori cuantas veces se va a ejecutar el codigo
# del interior del bucle.
# El numero de veces que se ejecutará dependerá de las circunstancias 
# durante la ejecucion del progrma.

#------------EJEMPLO BUCLE DETERMINADO--------------
# El BUCLE DETERMINADO se hace con el for.
# se declara de la siguiente manera.

# ---------------SINTAXIS................
# for variable in elemnto a recorrer: 
#     cuerpo del bucle. ----> lineas de codigo a repeetir.


# NOTA: elemento a recorrer puede ser una lista, puede ser una tupla,
#       pude ser una cadena de texto, puede ser un rango.


#-------EJEMPLO BUCLE FOR.--------------------

for i in ["primavera", "verano", "otoño,", "Invierno"]: #---> delcaracion del bucle, en este caso se va areptir 3 veces.
    print(i)


