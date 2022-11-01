
def validarLeerStrings(mensaje:str)->str:
    """Recibe un mensaje para el input y valida que el dato ingresado no sea un str vacio"""
    while True:
        variableLeer=input(mensaje)
        if(variableLeer!=""):
            return variableLeer
        print("[El valor a ingresar no debe ser vacio]")

def validarLeerInt(mensaje:str)->int:
    """Recibe un mensaje para el input y valida que el dato ingresado no sea una variable de tipo str"""
    while True:
        variableLeer=input(mensaje)
        if(variableLeer.isnumeric()):
            variableLeer=int(variableLeer)
            return variableLeer
        print("[El valor a ingresar debe ser un NÚMERO]")

def leerArrayStrings(mensaje:str,longitud:int)->list[str]:
    """Recibe un mensaje para el input y la longitud del array a recorrer, solo es para valores de tipo str"""
    lista=[]
    for i in range(1,longitud+1):
        variable=validarLeerStrings(mensaje+str(i)+":")
        lista.append(variable)
    return lista
