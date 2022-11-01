class Libro:
    def __init__(self, id : int , titulo : str, genero : str, ISBN : str , editorial: str, autores: list[str]) -> None:
        self.__id = id
        self.__titulo = titulo
        self.__genero = genero
        self.__ISBN = ISBN
        self.__editorial = editorial
        self.__autores = autores
    

    def get_ISBN(self)->str:
        return self.__ISBN
    def set_ISBN(self, ISBN)->None:
        self.__ISBN = ISBN

    def get_editorial(self)->str:
        return self.__editorial
    def set_editorial(self, editorial)->None:
        self.__editorial = editorial
    
    def get_autores(self)->List:
        return self.__autores
    def set_autores(self, autores)->None:
        self.__autores = autores