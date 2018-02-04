# Ambas funciones dependen de la variable global 'a'
# Si no estuviera definida provocaría un error en tiempo de ejecución
def printGlobalA():
    global a
    print(a)

def printSquareGlobalA():
    global a
    print(a**2)

global a
a = 10

printGlobalA()
printSquareGlobalA()
