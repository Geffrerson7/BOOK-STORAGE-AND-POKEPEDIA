from funciones_tarea1 import *
lista_libros=[]

while True:
    opcion = input("Ingrese la opcion: ")
    opcion = int(opcion)
        #validacion numerica
    if opcion == 1:
        lista_libros.extend(CargarArchivo())
        id = 0
    if opcion == 3:
        break
for item in lista_libros:
    print(item)