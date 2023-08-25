# -*- coding: utf-8 -*-

# ------------CONDICIONALES 1------------------
# Dentro de las estructuras de control de flujo, hay 2 grandes grupos, los CONDICIONALES Y los BUCLES, y a su ves
# cada unos de estos dos grupos tienen varias estructuras diferentes.

# ----------HOY VEREMOS LAS  CONDICIONALES-------
# La estructura de la condicional mas utilizada en casi todos los lenguajes de progrmacion, es la CONDICIONAL IF.

# -------- CONOCER PRIMERO EL FLUJO DE EJECUCION DE UN PROGRMA--------------
# El flujo de ejecuciond de un programa es el orden con que se ejecutan sus instrucciones.
# un programa esta compuesto por varias instrucciones que se van escribiendo, como se escribe un texto en una carta, es decir  
# una instruccion debajo de la otra. 
# Y el flujo de una ejecucion es el orden que sigue el programa a la hora de leer y ejecutar esas instrucciones. 
# El orden en este flujo de ejcucion normal mente es de arriba a bajo, se dice NORMALMENTE por que este flujo puede ser ALTERADO,
# por diversas causas, una de ellas es presisamente las ESTRUCTURAS DE CONTROL FLUJO, lo que hacen estas estructuras es modificar,
# ese orden natural de arriba hacia abajo, en la ejecucion de las instrucciones de un programa.

#------- COMO FUNCIONA EXACTAMENTE UN CONDICIONAL IF??------------
# Lo que se hace, es que cuando se corre un progrma y se encuntra una condicion if, el progrma se detien y va a verificar si la condicion dada, 
# es verdadera o falsa, si la condicion es verdadera ingresara dentro del flujo de la condicion y leera las lineas de codigo que 
# estan dentro de la condicion.
# Luego de terminar de leer las lineas que estan dentrode  la condicion, continua hacia abajo con las otras lineas que estan,
# fuera de la condicion.
# Lo que hace si la condicion es FALSA. Si la condicion es falsa, lo que hace el progrma es saltar lo que hay dentro de la condicion, e
# ignorar el codigo que hay dentro de la condicion, de modo que no la ejecutaria , y continuaria con el codigo que hay luego de la condicion.

# ------- AHORA VEREMOS LA SINTAXIS DE UNA CONDICIONAL IF----------------
# Para ver como funciona una condicion if, vamos a utilizar conceptos que ya hemos visto y los vamos a mesclar,
# con el bloque de la condicional if.
# Vamos a crear un funcion a la cual vamos a llamar evaluacion; que es lo que va a hacer esta funcion,
# esta funcion va a recivir por parametros una nota, una nota que puede ser de un alumno, y esta funcion se va a encargar
# de decirme si el alumno en funcion de la nota que recive esta aprobado o no esta aprobado, si la nota es superior a 5 o = a 5, entonces
# el alumno esta aprobado, si no es superior a 5 entonces el alumno no esta aprobado. 

# ------------EJEMPLO----------

def evaluacion(nota):
    valoracion="aprobado"
    return valoracion
print(evaluacion(1))
    
# ---------------EXPLIACION---------------
# Declaramos la funcion con el nombre evaluacion, decimos que esa evaluacion va a recivir un parametros,
# Luego declaramos una variable la que decimos que es igula a aprobado, es decir por el momento si imprimimos la funcion, dira que 
# todos los estudiantes sin importar la nota estan aprobados.
# NOTA: Recordar que si la funcion devuelve algo es necesario ponerle un return, de lo que necesite devolver, para este ejemplo,
#       vamos a devolver lo que esta dentro de la varibale valoracion.

# Pero para que el enunciado funciones debemos poner una condicional if de la siuiente manera.
# Luego de tener la funcion declarada, con el parametro que va a recivir, declaramos una variable que imprimira si la nota >= 5,
# (mayor o igal que 5), y luego declaramos la condicional if.
# En la condicional if, lo que se va a hacer es, EVALUAR SI LA NOTA QUE LE HE PASADO POR ARAMETRO A ESTA FUNCION, por ejemplo, es
# < 5,  EN EL CASO DE QUE ESTO SEA VERDAD, DENTRO DE LA CONDICIONAL IF, se pondra la variable antes declara pero cambiando el texto,
# a no aprobado.
# NOTA: Recordar los operadores de comparacion, > (mayor que), <(menor que), ==(Igual que), >=(mayor o igual que), <=(menor o igual que),
#       != (Indiferente que), estos operadores son muy utilizados en las condiciones y bucles.

def evaluacion2(nota):
    valoracion="aprobado" #<-- esta linea se va a ejecutar siempre que se llame esta funcion. 
    if nota <= 5: # <----------- Esta es la forma como inicia una condicion en python, no hay parentecis, no hay llaves.
        valoracion="no aprobado" # <--- Aquie dentro de la condicion lo que hace es cambiar la varible de la valoracion en no aprobado.
                                 # Esta linea de codigo se va a ejecutar, solo si la condicion es verdadera, de lo contrario, el programa no entra hasta aqui y continua con las otras lineas.

    return valoracion # <--Luego le decimos a la funcion que nos devuelva lo que hay almacenado en la variable valoracion. 
                      # <--Esta linea tambien se va ejecutar siempre que se llame la funcion, y nos va imprimir lo almacenado en la variable,
                      # ya sea lo que esta fuera d ela condicional, o lo que esta dentro de la condicion.

print(evaluacion2(3)) # <--- Luego llamamos la funcion saliendonos de ella, y psando los parametros que nos pide, 
                      # NOTA: en este caso la estamos inicializando mediante el la funcio print, puede inciar mediante otros o funciones.
                      # RECORDAR: que si no ponemos los parametros arrojara un error, ya que la funcion esta esperando parametros.

# --------AHOR VAMOS A COMPLICAR MAS EL CODIGO CON OTRA FUNCION DE PYTHON-----
# vamos a utilizar la funcion INPUT(). La Funcion input cuando el flujo de ejecucion llegue  ella, el progrma se detendra, a la espera
# de que introduscamos un valor por teclado. Hasta que no introduscamos un valor por teclado y demos enter, el flujo de ejecucion, no
# continuara hacia abajo.

#------- COMO FUCIONA-----------------------
# declaramos el nombre que le vamos a dar al input, 


print("Programa de evaluacion de notas") # <-- mostramos un mensaje al usuario

nota_alumno=input("introduce una nota de un alumno: ") # <-- declaramos una variable al input(), Hasta que este input no tenga un valor por teclado no continuara las otras lineas.
                   # NOTA: Alg muy importante, y es que cuando ingresamos cualquier valor que ingresemos atraves de un input, es conciderado
                   # un texto, s decir si yo ingreso en un input un 7, para python es un texto, 
                   # LA SOLUCION SERIA, que todo lo que introduscamos en un input, se de valor numerico, y eso se hace con una funcion.
                   # definida de python que es int(); la funcion int, transformara cualquier cosa que se introduccida en los parametros en numero 
                   #IMPORTANTE: Dentro de los parametros de un input(), se puede introducir un mensaje, ejemplo, input("Introduce nota")

def evaluacion3(nota2):
    valoracion2 ="aprobado" 
    if nota2<5:                   
        valoracion2="No aprobado" 
        calificacion=7
    return valoracion2

# EJEMPLO DE CONVERTIR UN TEXTO EN UN NUMERO-----------
print(evaluacion3(int(nota_alumno))) # <-- aqui le estamos indicando que lo ingresado en el input() nota_alumno, sea convertido en un numero,
                                     # de esta maner lo ingresado en nota_alumno viaja y queda guardado e el argumento nota.

# IMPORTANTE:<---AMBITO: Tener en cuenta el termino ambito  cuando trabajamos con funciones y con condiciones.
# es tener en cuenta el ambito de las variables, esto quiere decir que una variable solamente es accesible dentro de un ambito.
# EJEMPLO: la variable valoracion, se ha declarado dentro de una funcion y hay que tener claro donde comienza y donde termina es funcion,
#          para el anterior ejemplo la funcion inicia con su declaracion y termina con la instruccion return, ESTO NOS ACLARA, que 
#          FUERA de este ambito la variable valoracion2, no se puede manipular, ni leer, solamente se puede leer y manipular,
#          dentro del ambito de la funcion.
#          Ocurre lo mismo si nosostros por ejemplo, dentro de la condicion if declaramos otra variable, no podemos acceder a ella,
#          fuera de la condicion if, ejemplo dentro de la funcion, o fuera de la funcion, de ninguna manera puede acceder a ella, sino 
#          solo dentro de la condicion.

