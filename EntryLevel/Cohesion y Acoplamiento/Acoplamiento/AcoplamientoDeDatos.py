class Value(object):
    compartido = 10

    def __init__(self):
        pass

    # doubleValue y squareValue están acoplados por compartido
    def doubleValue(self, valor):
        self.compartido = valor*2

    def squareValue(self, valor):
        self.compartido = valor**2

value = Value()
value.doubleValue(4)
print(value.compartido)
value.squareValue(4)
print(value.compartido)
