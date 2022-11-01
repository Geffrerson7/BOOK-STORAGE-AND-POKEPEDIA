from funciones_tarea1 import *
from funciones_utilidades import *
lista_libros=[]

while True:
    opcion = validarLeerInt("Ingrese la opción:")
    if opcion == 1:
        lista_libros.extend(CargarArchivo())
        id = 0
    elif opcion == 3:
        id=crearId(len(lista_libros))
        print("Ingrese datos del libro:")
        titulo=validarLeerStrings(" -Título:")
        genero=validarLeerStrings(" -Género: ")
        isbn=validarLeerStrings(" -ISBN: ")
        editorial=validarLeerStrings(" -Editorial: ")
        nroAutores=validarLeerInt(" -Nro de autores:")
        autores=leerArrayStrings("  ->Autor ",nroAutores)
        libro=agregarLibro(id,titulo,genero,isbn,editorial,autores)
        lista_libros.append(libro)
        print("[*** Libro agregado ****]")
    elif opcion==6:
        print("*** Libros Ordenados Por titulo ****")
        titulos=ordenarLibrosPorTitulo(lista_libros)
        for i,titulo in enumerate(titulos,1):
            print(i,titulo)
    if opcion == 11:
        break
for item in lista_libros:
    print(item.get_titulo())