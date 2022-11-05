from funciones_tarea1 import *
from funciones_utilidades import *


def menu():
    lista_libros = []
    while True:
        funcionlimpiar()
        print("***** BIBLIOTECA *******")
        creacionMenu(
            [
                "Leer archivo de disco duro",
                "Listar libros",
                "Agregar libro",
                "Eliminar libro",
                "Buscar libro por ISBN o por título",
                "Ordenar libros por título",
                "Buscar libros por autor, editorial o género",
                "Buscar libros por número de autores",
                "Editar o actualizar datos de un libro",
                "Guardar libros en archivo",
                "Salir"
            ]
        )
        opcion = validarRangoInt(1, 11, "Ingrese la opción: ")
        if opcion == 1:
            funcionlimpiar()
            print("***** CARGAR EL ARCHIVO DE LIBROS *******")
            CargarArchivo(lista_libros)
            regresarmenu()
        elif opcion == 2:
            funcionlimpiar()
            print("******* LISTAR LIBRO ********")
            listar(lista_libros)
            regresarmenu()
        elif opcion == 3:
            funcionlimpiar()
            print("******* AGREGRAR LIBRO ********")
            libro = crearLibro(lista_libros)
            lista_libros.append(libro)
            print("[*** Libro agregado ****]")
            regresarmenu()
        elif opcion == 4:
            funcionlimpiar()
            print("******* ELIMINAR LIBRO ********")
            isbn = ingresarISBN(" -Ingrese ISBN del libro a eliminar: ")
            eliminarLibro(isbn, lista_libros)
            regresarmenu()
        elif opcion == 5:
            funcionlimpiar()
            print("******* BUSCAR LIBRO POR ISBN O POR TITULO ********")
            Buscar_libro_por_ISBN_o_título(lista_libros)
            regresarmenu()

        elif opcion == 6:
            funcionlimpiar()
            print("*** LIBROS ORDENADOS POR TÍTULO ****")
            ordenarLibrosPorTitulo(lista_libros)
            regresarmenu()
        elif opcion == 7:
            funcionlimpiar()
            print("******* BUSCAR LIBRO POR AUTOR, EDITORIAL O GENERO ********")
            Buscar_libro_por_autor_editorial_o_título(lista_libros)
            regresarmenu()
        elif opcion == 8:
            funcionlimpiar()
            print("******* BUSCAR LIBRO POR AUTOR, EDITORIAL O GENERO ********")
            Buscar_por_numero_autores(lista_libros)
            regresarmenu()
        elif opcion == 9:
            funcionlimpiar()
            print("****** EDITAR LIBRO ******")
            isbn = validarLeerStrings(" -Ingrese ISBN del libro a editar: ")
            libroActualizar, index = buscarLibro(isbn, lista_libros)
            if libroActualizar is not None:
                print("***** OPCIONES DE EDICIÓN ***** ")
                creacionMenu(
                    [
                        "Editar todos los datos del libro",
                        "Actualizar un dato en especifico",
                        "Cancelar",
                    ]
                )
                op = validarRangoInt(1, 3, "Ingrese una opción: ")
                if op == 1:
                    lista_libros[index] = crearLibro(lista_libros)
                    print("[*** Libro editado ****]")
                if op == 2:
                    libro = actualizarLibro(libroActualizar)
                    lista_libros[index] = libro
            else:
                print("[El ISBN ingresado no está registrado en el sistema]")
            regresarmenu()
        elif opcion == 10:
            funcionlimpiar()
            print("****** GUARDAR LIBROS EN EL DISCO DURO ******")
            guardarlibros(lista_libros)
            regresarmenu()
        elif opcion == 11:
            break


def main():
    funcionlimpiar()
    menu()


if __name__ == "__main__":
    main()
