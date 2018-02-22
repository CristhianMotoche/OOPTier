class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def setWidth(self, newWidth):
        self.width = newWidth

    def setHeight(self, newHeight):
        self.height = newHeight

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def setWidth(self, side):
        self.width = side
        self.height = side

    def setHeight(self, side):
        self.width = side
        self.height = side

# El ejemplo no se nota claramente en un lenguaje de tipado dinámico como Python.
# Por tal motivo, altero la propiedad __class__ para hacer que shape sea un
# Rectángulo y se ejecute su función _setWidth_ que solamente altera la propiedad
# _width_. Esto provoca que solamente se modifique el width en el cuadrado, provocando
# que nuestro objecto sqr quede con _width_ y _heigth_ diferentes y así
# se pierden sus propiedades.
def f(shape):
    shape.__class__ = Rectangle
    shape.setWidth(3)

# El paso de parámetros en Python es por referencia.
sqr = Square(4)
f(sqr)
print("Cudrado:")
print("Alto:", sqr.height)
print("Ancho:", sqr.width)
print("...")
print("...")
print("...")
print("algo está mal...")
