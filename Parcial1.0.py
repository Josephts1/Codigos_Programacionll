#Creacion de la matriz--------------------------------------------
import random
nfilas=eval(input("Digite el numero de filas de la matriz:"))
ncolumnas=eval(input("Digite el numero de columnas de la matriz:"))
matriz=[]
for i in range(nfilas):
    filas=[]
    for j in range(ncolumnas):
        filas.append(random.randint(0,20))
    matriz.append(filas)
print(matriz)
#-----------------------------------------------------------------
def SumaH():
    sumH=0
    max=0
    listH=[]
    for i in range(nfilas):
        for j in range(ncolumnas):
            sumH+=matriz[i][j]
        listH.append(sumH)
        sumH=0
    #print(listH)
    for i in listH:
        if i>max:
            max=i
    return max
def SumV():
    sumV=0
    max=0
    listV=[]
    for j in range(ncolumnas):
        for i in range(nfilas):
            sumV+=matriz[i][j]
        listV.append(sumV)
        sumV=0
    #print(listV)
    for i in listV:
        if i>max:
            max=i
    return max
def SumD():
    sumD=0
    a=0
    max=0
    listD=[]
    for i in range(nfilas):
        for j in range(0,1):
            sumD+=matriz[i][j+a]
        a+=1
        listD.append(sumD)
    for i in listD:
        if i>max:
            max=i
    return max
def SumAD():
    sumAD=0
    a=0
    max=0
    listAD=[]
    for i in range(nfilas):
        for j in range(ncolumnas-1,ncolumnas-2,-1):
            sumAD+=matriz[i][j-a]
        a+=1
        listAD.append(sumAD)
    print(listAD)
    for i in listAD:
        if i>max:
            max=i
    return max
def numMaximo():
    maxlistH=SumaH()
    maxlistV=SumV()
    maxlistD=SumD()
    maxlistAD=SumAD()
    nummaximos=[maxlistH,maxlistV,maxlistD,maxlistAD]
    print(f"Esta es la lista con los numeros mayores de cada suma: {nummaximos}")
    m=0
    for i in nummaximos:
        if i>m:
            m=i
    return m
numeroMaximo=numMaximo()
print(numeroMaximo)












#Creacion de la matriz--------------------------------------------
import random
nfilas=eval(input("Digite el numero de filas de la matriz:"))
ncolumnas=eval(input("Digite el numero de columnas de la matriz:"))
matriz=[]
for i in range(nfilas):
    filas=[]
    for j in range(ncolumnas):
        filas.append(random.randint(0,20))
    matriz.append(filas)
print(matriz)
#FUNCION PARA HALLAR MAYOR
def hallarMayor(lista):
    m=0
    for i in lista:
        if i>m:
            m=i
    return m
#-----------------------------------------------------------------
def SumaH():
    sumH=0
    listH=[]
    for i in range(nfilas):
        for j in range(ncolumnas):
            sumH+=matriz[i][j]
        listH.append(sumH)
        sumH=0
    maxH=hallarMayor(listH)
    return maxH
def SumV():
    sumV=0
    listV=[]
    for j in range(ncolumnas):
        for i in range(nfilas):
            sumV+=matriz[i][j]
        listV.append(sumV)
        sumV=0
    maxV=hallarMayor(listV)
    return maxV
def SumD():
    sumD=0
    a=0
    listD=[]
    for i in range(nfilas):
        for j in range(0,1):
            sumD+=matriz[i][j+a]
        a+=1
        listD.append(sumD)
    maxD=hallarMayor(listD)
    return maxD
def SumAD():
    sumAD=0
    a=0
    listAD=[]
    for i in range(nfilas):
        for j in range(ncolumnas-1,ncolumnas-2,-1):
            sumAD+=matriz[i][j-a]
        a+=1
        listAD.append(sumAD)
    print(listAD)
    maxAD=hallarMayor(listAD)
    return maxAD
def numMaximo():
    maxlistH=SumaH()
    maxlistV=SumV()
    maxlistD=SumD()
    maxlistAD=SumAD()
    nummaximos=[maxlistH,maxlistV,maxlistD,maxlistAD]
    print(f"Esta es la lista con los numeros mayores de cada suma: {nummaximos}")
    m=0
    maxT=hallarMayor(nummaximos)
    return maxT
numeroMaximo=numMaximo()
print(numeroMaximo)
