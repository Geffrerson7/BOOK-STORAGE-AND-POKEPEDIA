from funciones_tarea1 import *
from funciones_utilidades import *
lista_libros = []
funcionlimpiar()
while True:
    funcionlimpiar()
    print("***** BIBLIOTECA *******")
    creacionMenu(["Leer archivo de disco duro", "Listar libros", "Agregar libro",
                 "Eliminar libro", "Buscar libro por ISBN o por título", "Ordenar libros por título",
                  "Buscar libros por autor, editorial o género", "Buscar libros por número de autores",
                  "Editar o actualizar datos de un libro", "Guardar libros en archivo","Salir"])
    opcion = validarRangoInt(1,11,"Ingrese la opción:")
    if opcion == 1:
        funcionlimpiar()
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
        isbn=validarLeerStrings(" -Ingrese ISBN del libro a eliminar: ")
        eliminarLibro(isbn, lista_libros)
        regresarmenu()
    elif opcion == 5:
        print("******* BUSCAR LIBRO POR ISBN O POR TITULO ********")
        Buscar_libro_por_ISBN_o_título(lista_libros)
    elif opcion == 6:
        funcionlimpiar()
        print("*** LIBROS ORDENADOS POR TÍTULO ****")
        ordenarLibrosPorTitulo(lista_libros)
        regresarmenu()
    elif opcion == 9:
        funcionlimpiar()
        print("****** EDITAR LIBRO ******")
        isbn=validarLeerStrings(" -Ingrese ISBN del libro a editar: ")
        libroActualizar,index=buscarISBN(isbn,lista_libros)
        if(libroActualizar is not None):
            print("***** OPCIONES DE EDICIÓN ***** ")
            creacionMenu(["Editar todos los datos del libro","Actualizar un dato en especifico","Cancelar"])
            op=validarRangoInt(1,3,"Ingrese una opción: ")
            if(op==1):
                lista_libros[index]=crearLibro(lista_libros)
                print("[*** Libro editado ****]")
            if(op==2):
                libro=actualizarLibro(libroActualizar)
                lista_libros[index]=libro       
        else:
            print("[El ISBN ingresado no está registrado en el sistema]")
        regresarmenu()
    elif opcion == 11:
        break
