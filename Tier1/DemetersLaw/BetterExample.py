class A(object):
    def __init__(self):
        pass

    # Ahora, se está siguiendo la ley de demeter,
    # aunque se podría inyectar esta dependencia...
    def a_method(self, b):
        c_call = C_Caller()
        c_call.call_c(b.c)

class C_Caller(object):
    def __init__(self):
        pass

    def call_c(self, c):
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

