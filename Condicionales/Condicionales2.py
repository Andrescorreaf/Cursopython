# -*- coding: utf-8 -*-

#  -----CONDICIONALES IF ACOMPAÑADOS DE UN ELSE O UN ELIF.

#----VAMOS A VER LA INSTRUCCION ELSE.
#----Vamos aplicar esta funcion, con un ejercicio practico, que es controlar una acceso a menores de edad.
#----Vamos a decirle al usuariao que introdusca por teclado cual es su edad, y si la edad es menor que 18, entonces 
#----que nuestro progrma imprima un mensaje indicando que no puede pasar por que es menor de edad, y si no es menor de 18, 
#----que imprima un mensaje que puede pasar.
#----NOTA: else quiere decir (y si no es verdad). esto quiere decir que donde ves un else, inmediatamente ya sabes que su traduccion
#---- es:  Y SI NO ES VERDAD.
#---- OCURRE lo mismo si ves la condicion if, IF quiere decir si tal cosa es verdad, y else y si no es verdad.


#----- RECORDAR QUE EL PROGRMA SE VA EJECUTAR DE FORMA DE ARRIBA A BAJO-----

print("Progrma control de ingreso") # STEP 1 <---Imprimimos un mensaje que le mostraremos al usuario como 
edad_usuario = input("ingresar edad de usuario: ") # STEP 2 <--- luego declaramos una variable donde se guardara lo ingresado en el input


def edad1(edad): # <--------------STEP 3: Ejecuta la funcion, pero como no tiene ningun argumento se salta la linea  
    #mensaje="Puede pasar"
    if edad< 18: #<---------------STEP 4: Ingresa a la condicion if   
        mensaje="No puede pasar"
    else:
        mensaje="puede pasar"
    return mensaje

print(edad1(int(edad_usuario)))



