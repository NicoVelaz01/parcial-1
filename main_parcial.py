from funciones_parcial import *
import os

while True:
    os.system("cls")
    

    match menu():
        case "1":
            os.system("cls")
            lista_movies = obtener_lista_movies("movies.csv")
            asignar_rating(lista_movies)
            asignar_genero(lista_movies)

        case "2":
            os.system("cls")
            mostrar_movies(lista_movies)

        case "3":
            os.system("cls")
            mostrar_datos(lista_movies, "rating")

        case "4":
            os.system("cls")
            mostrar_datos(lista_movies, "genero")

        case "5":
            os.system("cls")
            filtrar_movies("comedia", lista_movies)

        case "6":
            os.system("cls")
            ordenar_movies(lista_movies, "genero")
            mostrar_movies(lista_movies)

        case "7":
            os.system("cls")
            mostrar_nombre_dato(lista_movies, "rating")


        case "8":
            os.system("cls")


        case "9":
            os.system("cls")   
           

    os.system("pause")