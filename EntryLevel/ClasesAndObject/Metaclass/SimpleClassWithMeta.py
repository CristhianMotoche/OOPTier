from MetaClass import *

class MetaCar(object, metaclass=AttributeInitType):
    @property
    def description(self):
        """ Return a description of this car. """
        return " ".join(str(value) for value in self.__dict__.values())
