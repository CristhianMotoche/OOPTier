from abc import abstractmethod, ABCMeta

class Interface(metaclass=ABCMeta):
  @abstractmethod
  def method(self):
    pass

@Interface.register
class Concrete(Interface):
    def __init__(self):
        pass
#    def method(self):
#        pass

myConcrete = Concrete()
