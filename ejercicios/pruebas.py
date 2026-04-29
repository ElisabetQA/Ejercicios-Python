#1 Pide a la usuaria cuántas notas desea introducir
cantidad = int(input("¿Cuántas notas deseas introducir?: "))

suma = 0

#2 Solicita cada nota
for i in range(cantidad):
    nota = float(input("Introduce una nota: "))
    suma = suma + nota

#3 Calcula la media
media = suma / cantidad

#4 Muestra la media
print("La media es:", media)