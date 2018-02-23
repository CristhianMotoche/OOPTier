import sys
from abc import ABCMeta, abstractmethod

class Printer(metaclass=ABCMeta):
    @abstractmethod
    def printChar(self,c):
        pass

class Reader(metaclass=ABCMeta):
    @abstractmethod
    def readChar(self):
        pass

@Printer.register
class STDOUTPrinter(Printer):
    def printChar(self,c):
        print(c)

@Reader.register
class STDINReader(Reader):
    def readChar(self):
        return sys.stdin.read(1)

@Printer.register
class FilePrinter(Printer):
    def __init__(self, filepath):
        self.file = open(filepath, 'a')
    def printChar(self,c):
        self.file.write(c)

def copy(printer, reader):
  c = ''
  while True:
    c = reader.readChar()
    if not c:
        break
    printer.printChar(c)

#copy(STDOUTPrinter(), STDINReader())
copy(FilePrinter('./file.txt'), STDINReader())
