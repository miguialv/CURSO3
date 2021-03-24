from autor import * 

class Libro:
  def __init__(self, autor, titulo, anyo):
      self.__autor = autor 
      self.__titulo = titulo
      self.__anyo = anyo
      
  def get_Autor():
      return self.__autor.get_NombreAutor()

  def get_anyo(self):
       return self.__anyo

  def get_Titulo(self):
      return self.__titulo