#Función calcular el precio total aplicando descuento e IVA
def calcular_precio_total (precio_por_unidad, cantidad_a_comprar):
    resultado = (precio_por_unidad * cantidad_a_comprar)
    return resultado


#Solicitud de parámetros al usuario
precio_por_unidad = float (input ("¿Qué precio tiene una unidad? "))
cantidad_a_comprar = float (input ("¿Cuántos vas a comprar? "))

#Guardar el resultado como variable 
resultado = calcular_precio_total (precio_por_unidad, cantidad_a_comprar)

#Imprimir resultado
print ("El total del producto es " , resultado)