def obtener_csv_como_lista_de_diccionario(nombre_archivo):
    separador = ','
    with open(nombre_archivo, encoding="utf-8") as archivo:
        next(archivo) #omitir encabezao del archivo
        libros = []
        for linea in archivo:
            linea = linea.rstrip("\n") #Quitar el salto de linea
            columnas = linea.split(separador)
            titulo = columnas[0]
            ISBN = columnas[1]
            libros.append({
                "titulo": titulo,
                "ISBN": ISBN
            })
        return libros



def listar(libros_data):
   for libro in libros_data:
    titulo = libro['titulo']
    ISBN = libro['ISBN']
    print(f"El titulo del libro es {titulo} y su ISBN es {ISBN}")
libros = obtener_csv_como_lista_de_diccionario("./libros.csv")
listar(libros)