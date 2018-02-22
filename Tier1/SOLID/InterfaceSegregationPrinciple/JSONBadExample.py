from abc import abstractmethod, ABCMeta

class ProcessJSON(metaclass=ABCMeta):
    @abstractmethod
    def fromJSON(self):
        pass

    @abstractmethod
    def toJSON(self):
        pass

@ProcessJSON.register
class Computer(ProcessJSON):
    def __init__(self, color, size, year):
        self.color = color
        self.size = size
        self.year = year

    def toJSON(self):
        return "{'color': %s, 'size': %f, 'year': %d}" % (self.color, self.size, self.year)

    # Estamos obligados a implementar este métodos, caso contrario el programa 
    # no se ejecutará
    def fromJSON(self):
        pass

# El resto de la aplicación solo requiere un JSON a partir de Computer
computer = Computer('Black', 15.4, 2006)
print(computer.toJSON())
