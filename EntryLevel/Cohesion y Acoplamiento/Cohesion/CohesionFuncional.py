# La única unidad de sw está agrupada dentro de la clase
class Sqrt:
    def __init__(self):
        pass
    def sqrt(self, val):
        return val**(1/2)

sqrt = Sqrt()
print(sqrt.sqrt(4))
