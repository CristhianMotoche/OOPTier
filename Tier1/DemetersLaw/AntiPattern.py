class A(object):
    def __init__(self):
        pass

    # Por intentar seguir la ley de demeter, se generó
    # el antipatrón de los métodos privados en capa
    def a_method(self, b):
        self.__private_call_c(b.c)

    def __private_call_c(self,c):
        c.c_method()

class B(object):
    def __init__(self):
        self.c = C()

class C(object):
    def __init__(self):
        pass

    def c_method(self):
        print("Hello world")

a = A()
b = B()

a.a_method(b)
