# Pedirle al usuario una frase
frase = input("¿Cuál es tu color favorito? ")

#La longitud de la frase.
longitud = len(frase)

#La frase en mayúsculas.
mayusculas = frase.upper()

#La frase en minúsculas.
minuscula = frase.lower()

#Imprimir todas las muestras
print("Tu color favorito es el", frase)
print("Longitud", longitud)
print(mayusculas)
print(minuscula)