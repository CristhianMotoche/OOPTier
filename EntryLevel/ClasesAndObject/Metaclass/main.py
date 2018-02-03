from SimpleClassWithMeta import *
from SimpleClass import *

car = Car('Toyota', 'Prius', 2005, 'Green')
metaCar = MetaCar(make='Toyota', model='Prius', year=2005, color='Green')

print(car.description)
print(metaCar.description)
