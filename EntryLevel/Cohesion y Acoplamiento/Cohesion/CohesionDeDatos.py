class HoldDato(object):
    dato = None
    def __init__(self, dato):
        pass
    # En este caso todas las funciones están agrupadas por estar involucradas
    # con el atributo 'dato'
    def printDato(self):
        print(dato)

    def setDato(self, value):
        self.dato = value

    def getDato(self):
        return self.dato
