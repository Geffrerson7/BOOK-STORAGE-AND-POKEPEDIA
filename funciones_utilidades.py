import os

def regresarmenu():
    input("Presione una tecla para regresar ...")
    
def funcionlimpiar():
#os.name (define el sistema operativo), var es la palabra para limpiar pantalla 
    if os.name == "posix":
        var = "clear"       
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        var = "cls"
    os.system(var)

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

def validarRangoInt(inicio:int,final:int,mensaje:str)->int:
    """Valida que una opcion ingresada este en el rango indicado y valida que sea un entero"""
    while True:
        variable=validarLeerInt(mensaje)
        if variable>=inicio and variable<=final:
            return variable
        print("[El número ingresado no está en el rango indicado]")  

def leerArrayStrings(mensaje:str,longitud:int)->list[str]:
    """Recibe un mensaje para el input y la longitud del array a recorrer, solo es para valores de tipo str"""
    lista=[]
    for i in range(1,longitud+1):
        variable=validarLeerStrings(mensaje+str(i)+":")
        lista.append(variable)
    return lista

def creacionMenu(opciones:list[str])->None:
    for i,opcion in enumerate(opciones,start=1):
        print(str(i)+") "+opcion)