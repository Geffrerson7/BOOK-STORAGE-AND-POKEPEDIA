from typing_extensions import Self


class Libro:
    def __init__(self, id, titulo, genero, ISBN, editorial, autores):
        self.__id = id
        self.__titulo = titulo
        self.__genero = genero
        self.__ISBN = ISBN
        self.__editorial = editorial
        self.__autores = autores
    
    
    def get_ISBN(self):
        return self.__ISBN
    def set_ISBN(self, ISBN):
        self.__ISBN = ISBN

    def get_editorial(self):
        return self.__editorial
    def set_editorial(self, editorial):
        self.__editorial = editorial
    
    def get_autores(self):
        return self.__autores
    def set_autores(self, autores):
        self.__autores = autores