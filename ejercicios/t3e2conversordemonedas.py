#Pedir al usuario una cantidad en euros
cantidad_en_euros = float ( input ("Dime una cantidad en euros "))

#Convertir la cantidad de euros en otras monedas 
dolares = 1.1
libras = 0.87

#Fórmula
def convertir (cantidad_en_euros, dolares, libras):
    total_dolares = cantidad_en_euros * dolares
    total_libras = cantidad_en_euros * libras
    return total_dolares, total_libras

#imprimir varios resultados
total_dolares, total_libras = convertir (cantidad_en_euros, dolares, libras)
print ("Total en dólares", total_dolares)
print ("Total en libras", total_libras)
