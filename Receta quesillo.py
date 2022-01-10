def recetaQuesillo():
    n=eval(input("Cantidad estimada de personas que comeran el postre: "))
    ingredientes(n)
    return n
def ingredientes(n):
    print(f"{n*(1/5)} Taza de leche con densada")
    print(f"{n*(1/5)} Taza de leche liquida")
    print(f"{n} Huevos")
    print(f"{n*(1/5)} Cucharada de vainilla")
    print(f"{n*(1/4)}  Vaso de ron")
    print(f"{n} Cucharadas de azucar granulada")
#def preparacion():

n=recetaQuesillo()