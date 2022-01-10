"""numeros=[]
def pedirnumeros():
    for i in range(1,8):
        num=eval(input(f"Digite el numero {i}:"))
        numeros.append(num)
    return numeros
numeros=pedirnumeros()
print(f"Se encontrará el numero mayor de esta lista de numeros {numeros}")
m=0
for i in numeros:
    if i>m:
        m=i
print(m)

vocales=["A","a","E","e","I","i","O","o","U","u"]
def identificarVocales():
    caracter=input("Digitar un caracter: ")
    for i in vocales:
        if caracter==i:
            m=True
        else:
            continue
    return m,caracter
m,caracter=identificarVocales()
if m == True:
    print(f"El caracter {caracter} es una vocal")
elif m == False:
    print(f"El caracter {caracter} no es una vocal")
"""
def crearMatriz():
    matriz=[]
    nf=eval(input("Cuantas filas quiere en su matriz: "))
    nc=eval(input("Cuantas columnas quiere en su matriz: "))
    for i in range(nf):
        lista=[]
        for v in range(nc):
            numeroMatriz=eval(input("Digite un numero: "))
            lista.append(numeroMatriz)
        matriz.append(lista)
    return matriz,nf,nc

#MATRIZ DE LA FORMA ALGEBRÁICA
matriz,nf,nc=crearMatriz()
for i in range(nf):
    for v in range(nc):
        print("|",matriz[i][v],end=" |")
    print()
    print("_______________")
    print()