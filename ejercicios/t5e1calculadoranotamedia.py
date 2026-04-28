#Solicitar cúantas notas quiere introducir
def cantidad_notas ():
    numero_de_notas = int (input ("¿Cuántas notas desea introducir? "))
    return numero_de_notas


#Solicitar cada nota
def notas_por_alumno ():
    notas = float (input ("Introduce la nota: "))
    return notas

   
#llamar a las funciones
numero_de_notas = cantidad_notas ()


def media ():   
    notas_introducidas = 1
    suma = 0

    while notas_introducidas <= numero_de_notas:
        nota = notas_por_alumno ()
        suma = suma + nota
        notas_introducidas +=1

    media = suma/numero_de_notas
    print ("La media es: ", media)

media ()