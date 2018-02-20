#!/usr/bin/env python3

# Ahora, esta case está abierta a la extensión, ya que depende de un objecto
# printer, el cual se lo pasa como parámetro y maneja la impresión.
class Debug(object):
    def __init__(self, printer):
        self.printer = printer
        pass
    def debugger(self, value):
        self.printer.myPrint(value)

class Printer(object):
    def __init__(self):
        pass
    def myPrint(self, value):
        print(value)

class PrettyPrinter(object):
    def __init__(self):
        pass
    def myPrint(self, value):
        print("Let's say this module prints nice:", value)

pp = Printer()
db = Debug(pp)
db.debugger(3)

pp = PrettyPrinter()
db2 = Debug(pp)
db2.debugger(3)
