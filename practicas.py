'''def preguntasusuario():
    nombretra=input("Nombre del trabajador: ")
    print(type(nombretra))
    pesosxhora=eval(input("Salario basico por hora:COP "))
    num_horas = eval(input("Horas trabajadas por semana: "))
    return num_horas, pesosxhora, nombretra
num_horas,pesosxporhora,nombre=preguntasusuario()
def salario():
    salariomen=(pesosxporhora*(num_horas*4))
    salariosem = (pesosxporhora * num_horas)
    if salariomen>1200000:
        print(nombre, ':\n')
        print(f"Salario mensual:{salariomen} COP")
    else:
        print(nombre, ':\n')
        print(f"Salario semanal:{salariosem} COP")
salario()

salario()
import random
def preguntasusuario():
    num_filas=eval(input("Numero de filas: "))
    num_columnas=eval(input("Numero de columnas: "))
    return num_filas, num_columnas
num_filas,num_columnas=preguntasusuario()
def crearmatriz():
    matriz1=[]
    for i in range(num_filas):
        matrizint=[]
        for v in range(num_columnas):
            matrizint.append(random.randint(0,10))
        matriz1.append(matrizint)
    return matriz1
matriz=crearmatriz()
print(matriz)
for i in range(len(matriz)):
    print(i)
    for v in range(len(matriz)):
        pass
        #print("su")

lista=[1,23,6,5,3,3,2]
indice=[0,4,6]
nueva_lista=[lista[i] for i in indice] #el iterador i toma los valores de indice, uno por uno,luego se remplaza en lista[i] y tomará el valor del elemento en la posición i y lo agregará en la nueva lista en la posición cero.
nueva_lista2=[lista[i] for i in range(len(indice))]#Aquí toma el numero de elementos que tiene la lista indice
print(nueva_lista)
nueva_lista[1]=8
print(nueva_lista)
lista1=[]
for i in lista:
    print(i)
    lista1.append(i)

print(lista1)

lista_2=[]
datos=input("Introducir todos los datos en una línea separados por espacios: ")
datos=datos.split()

import random
listarandom=[]
n=eval(input("De cuantas filas quiere su matriz?: "))
def creadormatriz(n):
    for i in range(n):
        listarandom.append(random.randint(0,20))
    return listarandom
creadormatriz(n)
print(listarandom)
def imparespares():
    par=0
    imp=0
    listapares=[]
    listaimpar=[]
    for i in listarandom:
        if (i%2 == 0):
            listapares.append(i)
            par+=1
            #print(i,end="$")
        elif (i%2!=0):
            listaimpar.append(i)
            imp+=1

    print(f"Los numeros pares son: {listapares}")
    print(f"Los numeros impares son: {listaimpar}")
    print(f"La cantidad de numeros pares es: {par}")
    print(f"La cantidad de numeros impares es: {imp}")
imparespares()'''
f=open("siks.txt")
print(f.readlines())
