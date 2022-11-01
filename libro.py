class Libro:
    def __init__(self, id : int , titulo : str, genero : str, ISBN : str , editorial: str, autores: list[str]) -> None:
        self.__id = id
        self.__titulo = titulo
        self.__genero = genero
        self.__ISBN = ISBN
        self.__editorial = editorial
        self.__autores = autores
        
