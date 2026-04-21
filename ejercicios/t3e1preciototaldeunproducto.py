#Solicitud de parámetros al usuario
nombre_del_producto = input ("¿Cuál es el nombre del producto? ")
precio_por_unidad = float (input ("¿Cuánto es la inversión de una unidad? "))
cantidad_a_comprar = int (input ("¿Cuántos vas a comprar? "))
descuento_en_porcentaje = float (input ("¿Qué porcentaje de decuento tiene? "))
IVA_en_porcentaje = float (input ("¿Qué porcentaje de IVA tiene? "))

#Función calcular el precio total aplicando descuento e IVA
def calcular_precio_total (precio_por_unidad, cantidad_a_comprar, descuento_en_porcentaje, IVA_en_porcentaje):
    resultado = (precio_por_unidad * cantidad_a_comprar)
    return resultado

#Guardar el resultado como variable 
resultado = calcular_precio_total (precio_por_unidad, cantidad_a_comprar, descuento_en_porcentaje, IVA_en_porcentaje)


#Imprimir resultado
print("El total del producto es ", resultado)