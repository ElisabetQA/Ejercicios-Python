#Solicitud de parámetros al usuario
nombre_del_producto = input ("¿Cuál es el nombre del producto? ")
precio_por_unidad = float (input ("¿Cuánto es el precio de una unidad? "))
cantidad_a_comprar = int (input ("¿Cuántos vas a comprar? "))
descuento_en_porcentaje = float (input ("¿Qué porcentaje de descuento tiene? "))
IVA_en_porcentaje = float (input ("¿Qué porcentaje de IVA tiene? "))

#Función calcular el precio total aplicando descuento e IVA
def calcular_operaciones (precio_por_unidad, cantidad_a_comprar, descuento_en_porcentaje, IVA_en_porcentaje):
    total_producto = precio_por_unidad * cantidad_a_comprar
    total_descuento = (total_producto - (total_producto * descuento_en_porcentaje)/100)
    total_con_IVA = (total_descuento + (total_descuento * IVA_en_porcentaje)/100)
    return total_con_IVA

# Guardar el resultado en una variable
total_compra = calcular_operaciones (precio_por_unidad, cantidad_a_comprar, descuento_en_porcentaje, IVA_en_porcentaje)

#Imprimir total compra
print("El total de la compra es ", total_compra, "euros")