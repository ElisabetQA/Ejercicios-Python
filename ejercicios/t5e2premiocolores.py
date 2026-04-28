#Pedimos a la usuario 5 veces que introduzca un color
def pedir_colores ():
    color = input ("Introduce un color: ")
    return color


#Bucle solicitar 
def solicitud_colores ():

    premio = "FELICIDADES ¡has conseguido un premio!"
    no_premio = "¡Prueba otra vez!"

    for colores_usuaria in range (5):
        colores_usuaria = pedir_colores ()


        if colores_usuaria == "azul":
             break
        print (premio)
        
        print (no_premio)

        colores_usuaria +=1


solicitud_colores()