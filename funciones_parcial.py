from random import randint

def menu()-> str:
    print(f"{'Menu de Opciones':^50s}")
    print("1- Cargar archivo .CSV")
    print("2- Imprimir Lista")
    print("3- Asignar Rating")
    print("4- Asignar Genero")
    print("5- Filtrar por genero")
    print("6- Ordenar Peliculas")
    print("7- Informar mejor Rating")
    print("8- Guardar peliculas")
    print("9- Salir")

    return input("Ingrese una opcion: ")
# 1
def get_path_actual(nombre_archivo):
    import os
    direccion_actual = os.path.dirname(__file__)
    return os.path.join(direccion_actual, nombre_archivo)

def obtener_lista_movies(nombre_archivo):
    with open(get_path_actual(nombre_archivo), "r", encoding = "utf-8") as archivo:
        lista = []
        archivo.readline().strip("\n").split(",")
        
        for linea in archivo.readlines():
            movie = {}
            linea = linea.strip("\n").split(",")

            id, titulo, genero, rating = linea
            movie["id"] = int(id)
            movie["titulo"] = titulo
            movie["genero"] = genero
            movie["rating"] = float(rating)
            lista.append(movie)

        return lista
#2  
def mostrar_movies(lista_movies: list)-> None:
    tam = len(lista_movies)
    print("                ***Listado de Peliculas***")
    print()
    print("ID           Titulo                       Genero      Rating")
    print("-------------------------------------------------------------")
    for i in range(tam):
        mostrar_movies_item(lista_movies[i])
    print()

def mostrar_movies_item(una_movie: list):
    print(f"{una_movie['id']:<3}     {una_movie['titulo']:<30}  {una_movie['genero']:<14}  {una_movie['rating']:.2f}")

#3
def asignar_rating(lista):
    from random import randint
    for el in lista:
        el["rating"] = randint(1, 100) / 10

def mapear_movies(mapeadora, lista)-> list:
    lista_mapeada = []
    for el in lista:
        lista_mapeada.append(mapeadora(el))
    return lista_mapeada

def mostrar_datos(lista, dato):
    print(f"Titulo                               {dato.capitalize()}")
    for el in lista:
        print(f"{el['titulo']:<30}       {el[dato]}")
        

#4
def asignar_genero(lista):
    from random import randint
    for el in lista:
        aux = randint(1, 4)
        match aux:
            case 1:
                el["genero"] = "drama"
            case 2:
                el["genero"] = "comedia"
            case 3:
                el["genero"] = "accion"
            case 4:
                el["genero"] = "terror"

#5
def filtrar_movies(genero, lista: list)-> list:
    lista_filtrada = []
    for el in lista:
        if el["genero"] == genero:
            lista_filtrada.append(el)
    return lista_filtrada

def crear_archivo_generos(lista, nombre_archivo):
    with open(get_path_actual(nombre_archivo), "w", encoding = "utf-8") as archivo:
        archivo.writelines(lista)

#6
def swap_lista(lista: list, i:int, j:int)-> None:
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux

def ordenar_movies(movies: list, campo: str):
    tam = len(movies)
    for i in range(tam - 1):
        for j in range(i + 1):
            if movies[i][campo] > movies [j][campo]:
                swap_lista(movies, i, j)
#7
def obtener_mejor_rating(lista, dato):
    pelicula = None
    mayor_rating = 0
    flag_mayor_rating = True
    for el in lista:
        if flag_mayor_rating or el[dato] > mayor_rating:
            mayor_rating = el[dato]
            pelicula = el
            flag_mayor_rating = False
    return pelicula

def mostrar_nombre_dato(lista, dato):
    pelicula = obtener_mejor_rating(lista, dato)
    print(f"Pelicula con mejor {dato.capitalize()}")
    print(f"Titulo: {pelicula['titulo'].capitalize()} | {dato.capitalize()}: {pelicula[dato]}")
#8
