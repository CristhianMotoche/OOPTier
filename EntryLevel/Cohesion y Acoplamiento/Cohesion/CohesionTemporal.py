# En este caso las funciones están dentro del mismo módulo solamente
# porque se ejecutan al mismo tiempo.
def printList(lista):
    for item in lista:
        print(item)

def squareList(lista):
    return map((lambda x: x**2), lista)

def printSquareList(lista):
    printList(squareList(lista))
