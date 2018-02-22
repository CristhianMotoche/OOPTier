from abc import abstractmethod, ABCMeta

class FromJSON(metaclass=ABCMeta):
    @abstractmethod
    def fromJSON(self):
        pass

class ToJSON(metaclass=ABCMeta):
    @abstractmethod
    def toJSON(self):
        pass

@ToJSON.register
class Computer(ToJSON):
    def __init__(self, color, size, year):
        self.color = color
        self.size = size
        self.year = year

    def toJSON(self):
        return "{'color': %s, 'size': %f, 'year': %d}" % (self.color, self.size, self.year)

computer = Computer('Black', 15.4, 2006)
print(computer.toJSON())
