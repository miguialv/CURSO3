def get_list():
    myList={}
    f = open("palabras.txt", mode="rt", encoding="utf-8")
    words= [word for line in f for word in line.split(" ")]
    lengths=[]

    for word in words:
        for i in words:
        return [len(i) for i in lengths]

        
    
    f.close()
  return res