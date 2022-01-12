#Creacion de la matriz--------------------------------------------
import random
nfilas=eval(input("Digite el numero de filas de la matriz:"))
ncolumnas=eval(input("Digite el numero de columnas de la matriz:"))
matriz=[]
for i in range(nfilas+1):
    filas=[]
    for j in range(ncolumnas+1):
        filas.append(random.randint(0,20))
    matriz.append(filas)
print(matriz)
#-----------------------------------------------------------------
def SumaH():
    sumH=0
    max=0
    listH=[]
    for i in range(nfilas+1):
        for j in range(ncolumnas+1):
            sumH+=matriz[i][j]
        listH.append(sumH)
        sumH=0
    print(listH)
    for i in listH:
        if i>max:
            max=i
    return max
def SumV():
    sumV=0
    max=0
    listV=[]
    for j in range(ncolumnas+1):
        for i in range(nfilas+1):
            sumV+=matriz[i][j]
        listV.append(sumV)
        sumV=0
    print(listV)
    for i in listV:
        if i>max:
            max=i
    return max
def SumD():
    sumD=0
    a=0
    max=0
    listD=[]
    for i in range(nfilas+1):
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
    for i in range(nfilas+1,0,-1):
        for j in range(ncolumnas,ncolumnas-2,-1):
            sumAD+=matriz[i][j+a]
        a+=1
        listAD.append(sumAD)
    print(listAD)
    for i in listAD:
        if i>max:
            max=i
    return max
maxlistH=SumaH()
maxlistV=SumV()
maxlistD=SumD()
maxlistAD=SumAD()
print(maxlistH)
print(maxlistV)
print(maxlistD)
