#!/usr/bin/env python3

# Esta clase está abierta a la modificación y cerrada a la extensión. Si
# quisieramos utilizar una forma diferente para imprimir el valor. Por ejemplo,
# deberíamos cambiar el objecto `printer` de un Print a un PrettyPrinter.
class Debug(object):
    def __init__(self):
        pass
    def debugger(self, value):
        printer = Print()
        # printer = PrettyPrinter()
        printer.myPrint(value)

class Print(object):
    def __init__(self):
        pass
    def myPrint(self, value):
        print(value)

class PrettyPrinter(object):
    def __init__(self):
        pass
    def myPrint(self, value):
        print("Let's say this module prints nice:")
        print(value)

# Solo puedo instanciar un Debug que solamente va a poder imprimir de una forma.
db = Debug()
db.debugger(3)
