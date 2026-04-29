#Función pedir al usuario que introduzca un color
def pedir_colores ():
    color = input ("Introduce un color: ")
    return color


#Bucle solicitar 5 veces
def solicitud_colores ():
    premio = "FELICIDADES ¡has conseguido un premio!"
    no_premio = "¡Prueba otra vez!"

    for i in range (5):
        colores_usuaria = pedir_colores ()

        if colores_usuaria == "azul":
             print (premio)
             break  
        else:
            print (no_premio)

solicitud_colores()