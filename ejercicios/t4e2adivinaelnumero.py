#Función para mesajes
def adivina (numero):
    if numero == 4:
        mensaje = "FELICIDADES ¡¡Has acertado!!"
    else :
        mensaje = "Fallaste, vuelve a intentarlo ;D"
    return mensaje

#Función pedir el número
def pedir_numero ():
    numero = int (input("Dime un número del 1 al 10: "))
    return numero

#Llamar a la función
numero = pedir_numero ()
mensaje = adivina (numero)

#imprimir el mensaje
print (mensaje)