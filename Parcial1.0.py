matriz1=[[1,2],[3,4]]
matriz2=[[5,6],[7,8]]
fila1=[]
def kronecker(matriz1,matriz2):
    espaciosvacio=[]
    for i in range(len(matriz1)):
        espaciosvacio.append(["$"])
        #print(fila1)
        for v in fila1:
            espaciosvacio.append(v*2)
            print(v)

    print(espaciosvacio)
kronecker(matriz1,matriz2)