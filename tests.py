import unittest
from libro import *


def test_anyo(self):
    l1 = Libro(autor= Autor(id_autor = "1", nombre = "Miguel", apellido = "Alvarez"), titulo = "El libro", anyo = 2019)
    x1 = 1900
    x2 = 2020
    number = [x1:x2]
    self.assertEqual(l1.get_anyo(), number) 

def test_miFuncion(self):


def test_libro(self):
    self.assertRaisesRegex(ValueError, "El rango de años tiene que ser mayor que  1900 ", Libro, Autor(id_autor = "1", nombre = "Miguel", apellido = "Alvarez"),"Mi Libro",1899)
    self.assertRaisesRegex(ValueError, "El rango de años tiene que ser menor que  2020 ", Libro, Autor(id_autor = "1", nombre = "Miguel", apellido = "Alvarez"),"Mi Libro",2021)