import sys

class PrintChar(object):
  def __init__(self):
    pass

  def printChar(self,c):
      print(c)

class ReadChar(object):
  def __init__(self):
    pass

  def readChar(self):
    return sys.stdin.read(1)

def copy():
  c = ''
  reader = ReadChar()
  printer = PrintChar()
  while True:
    c = reader.readChar()
    if not c:
        break
    printer.printChar(c)

copy()
