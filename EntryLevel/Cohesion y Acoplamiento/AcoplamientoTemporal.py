class Temp(object):
    def __init__(self):
        pass

    def setAttr(self):
        self.attr = "Hello!"

    # Este método es dependiente de la ejecución de setAttr
    # Una vez que se ejecuta ese método, éste se puede ejecutar con libertad
    # Sale del _acoplamiento temporal_
    def printAttr(self):
        print(self.attr)

temp = Temp()
temp.setAttr()
temp.printAttr()
