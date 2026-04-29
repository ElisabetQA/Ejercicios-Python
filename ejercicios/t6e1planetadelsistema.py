#Lista de planetas, se añade en la lista el cero para pedir al usuario del 1 al 8
planetas = ["Cero", "Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]

#Función pedir al usuario un número del 1 al 8
def elige_numero ():
    numero = int (input ("Elige un número del 1 al 8 => "))
    return numero
numero = elige_numero ()

#Función mostrar número de la lista
def mostrar_planeta (planetas,numero):
    if numero <= 8:
        print (planetas [numero])
    else: 
        print ("El número introducido no está dentro de rango (1 al 8), vuelve a intentarlo. ")

mostrar_planeta (planetas, numero)