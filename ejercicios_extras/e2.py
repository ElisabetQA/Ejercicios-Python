#Escribir un programa que pregunte al usuario por el número de horas trabajadas 
    # y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

#Función preguntar las horas
def preguntar_horas ():
    return float (input ("¿Cuántas horas trabaja a la semana? "))

#Función preguntas el coste de horas
def preguntar_coste ():
    return float (input ("¿Cuánto te pagan por hora? "))

#Función operación
def operaciones (horas, coste):
    salario = (horas * coste) *4
    return salario

#Llamar a las funciones
horas = preguntar_horas ()
coste = preguntar_coste ()
salario_mensual = operaciones (horas, coste)

print ("Tu salario mensual es:", salario_mensual,"€")