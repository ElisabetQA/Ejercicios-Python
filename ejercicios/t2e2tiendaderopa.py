#Datos
camiseta = 10
sudadera = 20.5
gorra = 5.5

#Preguntar cantidad al usuario
cantidad_camiseta = int (input ("¿Cuántas camisetas vas a comprar? "))
cantidad_sudadera = int (input ("¿Cuántas sudaderas vas a comprar? "))
cantidad_gorra = int (input ("¿Cuántas gorras vas a comprar? "))

#Total compra
total_camiseta = camiseta * cantidad_camiseta
total_sudadera = sudadera * cantidad_sudadera
total_gorra = gorra * cantidad_gorra
Total_compra = total_camiseta + total_sudadera + total_gorra

#Añadir el IVA
Total_compra_con_IVA = Total_compra +((Total_compra * 21)/100)


#imprimir total compra
print("Total compra", Total_compra_con_IVA, "euros")