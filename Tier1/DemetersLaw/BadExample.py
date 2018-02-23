class A(object):
    def __init__(self):
        pass
    def a_method(self, b):
        # Esta llamada rompe la ley de demeter
        b.c.c_method()

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
