#Función de definición de los mensaje
def ruletadecolores (color):
    if (color == "rojo"):
        mensaje = "Te regalo pasión y energía"
    elif (color == "verde"):
        mensaje = "Te regalo esperanza y crecimiento"
    elif (color == "azul"):
        mensaje = "Te regalo calma y serenidad"
    elif (color == "amarillo"):
        mensaje = "Te regalo felicidad y optimismo"
    elif (color == "morado"):
        mensaje = "Te regalo dabiduría y creatividad"
    return mensaje

#Función pedir color al ususario
def pedir_color ():
    color = input("Elige un color: rojo · verde · azul · amarillo · morado (escríbelo en minúsculas) ")
    return color

#Llama a la ruleta de colores para que nos diga el mensaje
color = pedir_color ()
mensaje = ruletadecolores (color)

#Imprime mensaje
print (mensaje)