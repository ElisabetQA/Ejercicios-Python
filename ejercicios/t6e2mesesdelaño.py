#Lista de los meses del año
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

#Función para solicitar un número 
def pedir_numero ():
    return int (input ("Dime un número del 1 al 12 => "))

#Función para mostrar el mes
def mostrar_mes (meses, numero_elegido):
    mes = meses[numero_elegido - 1]

    if numero_elegido == 6:
        print (mes, "¡EL MEJOR MES! 🥳 ")
    else:
       print (mes)


numero_elegido = pedir_numero ()
mostrar_mes (meses, numero_elegido)