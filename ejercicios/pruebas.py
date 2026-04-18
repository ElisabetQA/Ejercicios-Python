#Variables mi película favorita
titulo_de_la_pelicula = "Aladdin"
director_de_la_pelicula = "Ron Clements y John Musker"
año_de_lanzamiento = 1992
genero = "Animación, Fantasía, Musical"
duracion_en_minutos = 90
tiene_premios = False

#Cambio de los valores en inglés
nuevo_titulo_de_la_pelicula = titulo_de_la_pelicula.replace ("Aladdin", "Aladdin")
nuevo_director_de_la_pelicula = director_de_la_pelicula.replace ("Ron Clements y John Musker", "Ron Clements and John Musker")
nuevo_genero = genero.replace ("Animación, Fantasía, Musical", "Animation, Fantasy, Musical")

#Imprimir los valores en inglés
print ("Ahora en inglés :D")
print("Title: ", nuevo_titulo_de_la_pelicula)
print("Director of the film: ", nuevo_director_de_la_pelicula)
print("Year: ", año_de_lanzamiento)
print("Genre: ", nuevo_genero)
print("Duration in minutes:", duracion_en_minutos)
print("Has awards?: ", tiene_premios)
