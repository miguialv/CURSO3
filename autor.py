class Autor:
  def __init__(self, id_autor, nombre, apellido):
      self.__id_autor = id_autor 
      self.__nombre = nombre
      self.__apellido = apellido


   def get_NombreAutor(self):
        return self.__nombre
    

   def get_ApellidoAutor(self):
       return self.__apellido
    
   def get_Id(self):
       return self.__id_autor