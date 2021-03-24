from libro import *


def get_list():
    myList={}
    f = open("palabras.txt", mode="rt", encoding="utf-8")
    words= [word for line in f for word in line.split(" ")]
    lengths=[]

    for word in words:
        for i in words:
        return [len(i) for i in lengths]
        myList[i]={lengths[i]:words[i]}

        
    
    f.close()
  return res



def mas_antiguos(lista, anyo):
    listaFinal=[]

    for i in lista:
        if libro.get_anyo() <= anyo:
            listaFinal[i].append(lista.get_Titulo())

    return listaFinal

