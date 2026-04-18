#Obtener los valores del usuario de su canción favorita
titulo_de_la_cancion = input ("¿Cuál es tu canción favorita? ")
artista = input ("¿Cuál es su artista? ")
album = input ("¿A qué álbum pertenece? ")
año_de_lanzamiento = input ("¿En qué año se lanzó? ")
duracion_en_segundos = int (input ("¿Cuántos segundos dura? "))
tiene_videoclip = input ("¿Tiene videoclip? (True o False) ")

#imprimir resultados de su canción favorita
print("----> RESUMEN DE LA CANCIÓN QUE MÁS TE GUSTA")
print("Tu canción favorita es", titulo_de_la_cancion)
print("El artista es", artista)
print("Pertenece al álbum", album)
print("Se lanzó en el año", año_de_lanzamiento)
print("La canción dura", duracion_en_segundos, "segundos")
print("¿Tiene videclip?", tiene_videoclip)


#Obtener los valores del usuario de la cación que menos le gusta v.2peor
peor_titulo_de_la_cancion = input ("¿Cuál es la canción que menos te gusta? ")
peor_artista = input ("¿Cuál es su artista? ")
peor_album = input ("¿A qué álbum pertenece? ")
peor_año_de_lanzamiento = input ("¿En qué año se lanzó? ")
peor_duracion_en_segundos = int (input ("¿Cuántos segundos dura? "))
peor_tiene_videoclip = input ("¿Tiene videoclip? (True o False) ")

#imprimir resultados de la cación que menos le gusta v.2peor
print("----> RESUMEN DE LA CANCIÓN QUE MENOS TE GUSTA")
print("La canción que menos te gusta es", peor_titulo_de_la_cancion)
print("El artista es", peor_artista)
print("Pertenece al álbum", peor_album)
print("Se lanzó en el año", peor_año_de_lanzamiento)
print("La canción dura", peor_duracion_en_segundos, "segundos")
print("¿Tiene videclip?", peor_tiene_videoclip)