# -*- coding: utf-8 -*-

# En Condicionales 3 vimos el elif con la CONCATENACION
# de operadores de comparacion.

#----------TUTORILA 12, CONDICIONALES 4--------------

# USO DE LOS OPERADORES LOGICOS AND Y OR

# AND: Cuando nos encontramos en el codigo un operdor logico and, lo 
#      podemos interpretar como, Y SI ADEMAS.

# OR: Si encontramos un operador logico OR, lo podemos traducir como O SI NO.

#---------------------EJEMPLO-------------------------------

# CASO DE USO: crear un programa que evalue si un alumno que va a entrar en un
#              colegio tien derecho a beca o no tine derecho a beca.

# NOTA: El programa va a evaluar la distancia a la que vive el alumno del colegio
#       de tal manera que si vive a una distan mayor a 41km entonce aplica para beca
#       de igula manera evalua si este alumnos tien mas hermanos en la institucion,
#       es decri ejemplo mas de 2 hermanos.
#       Tambien se evalua el salario familiar. 
# SE LE DARAÁ BECA A ALUMNO QUE CUMPLA LAS 3 CARACTERISTICAS.

"""print("progrma de becas Año 2018")

distancia_escuela=int(input("introduce la distancia a la escuela en km: "))
print(distancia_escuela)

numero_hermanos=int(input("introduce el numero de hermanos en la institucion: "))
print(numero_hermanos)

salario_familiar=int(input("introduce salario anual bruto: "))
print(salario_familiar)

if distancia_escuela>40 and numero_hermanos>2 and salario_familiar<=20000:
    print("tienes derecho a beca")
else:
    print("No tienes derecho a beca")


#-------------EJEMPLO CON EL OPERADOR OR--------------------------------
print("-------------------------------")
print("progrma de becas 2 Año 2018")

distancia_escuela_2=int(input("introduce la distancia a la escuela en km: "))
print(distancia_escuela_2)

numero_hermanos_2=int(input("introduce el numero de hermanos en la institucion: "))
print(numero_hermanos_2)

salario_familiar_2=int(input("introduce salario anual bruto: "))
print(salario_familiar_2)

if distancia_escuela_2>40 and numero_hermanos_2>2 or salario_familiar_2<=20000:
    print("tienes derecho a beca")
else:
    print("No tienes derecho a beca")
    """



# NOTA: en este ejemplo con OR, loq ue se esta indicando es que si nada de lo anterior al and se cumple
#       verificar si la ultima preposicion es verdadera, si es verdadera entonces se le puede dar beca.


#---------UTILIZANDO EL OPERADOR IN-----------------------------------
# CASO: Elaborar un progrma en el cual un alumno que esta cursadon una carrera,
#       tiene que escoger entre una lista de asignaturas, si el alumno escoge una asignatura
#       de la lsita se le imprime la asigunatua seleccionada.
#       si el alumno escoge una asignatura que no esta en el listado, se le imprime que esa asignatura no esta disponible.
print("------------------------------")

print("Asignaturas optativas Año 2018")
print("Asignaturas optativas: Informatica grafica - Pruebas de software - Usabilidad y accesibilada")

options=raw_input("Escriba la asignatura escogida: ")
asignatura=options.lower() # -----> con esta funcion lower, convierte el texto dado en input a minusculas.
                           # -----> upper()  hace lo contrario transforma el texto en mayuscula.
if asignatura in ("informatica grafica", "pruebas de software", "sabilidad y accesibilada"):

    print("Asignatura elegida: " + asignatura )

else:

    print("La asignatura escogida no esta contemplada")