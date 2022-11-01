import re
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

def Buscar_en_libros(cadena: str, libros: list, tipo_separador: str, tipo_key: str):
    cadena_list = cadena.split(tipo_separador)
    indice_libros = []

    for palabra in cadena_list:
      srch_result = 0
      for indice,libro in enumerate(libros):
        srch_result = libro[tipo_key].lower().find(palabra)
        if srch_result != -1:
          indice_libros.append(indice)
    indices_libros = set(indice_libros)   
    
    result = []
    for indice in indices_libros:
      result.append(libros[indice])
    return result


def Buscar_libro_por_ISBN_o_título(input_user: str, data):
    ISBN = re.search("^(?=(?:\D*\d){10}(?:(?:\D*\d){3})?$)[\d-]+$", input_user)

    if ISBN:
       return Buscar_en_libros(input_user, data, '-','ISBN')
    else:
      return Buscar_en_libros(input_user, data, ' ','titulo')

print(Buscar_libro_por_ISBN_o_título('978-1-56619-909-4', libros))