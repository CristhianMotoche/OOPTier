#!/usr/bin/env python3

# Ahora, vamos a resolver este problema de repetición de código con herencia:

# Partimos con que todo animal tiene un nombre (no es cierto, pero asumamos solo esto)
# y tiene una fecha de nacimiento:

class Animal(object):
    def __init__(self, name, birthday):
        pass


# Ahora, un mamífero tiene lo siguiente:
class Mammal(Animal):
    def __init__(self, fur):
        pass

    def give_birth(self):
        pass

# Y un ave lo siguiente:
class Bird(Animal):
    def __init__(self, plumage):
        pass

    def lay_eggs(self):
        pass

# Ahora, definamos clases a partir de Mammal:
class Cat(Mammal):
    def __init__(self):
        pass

    def meow(self):
        print("meowwww")

class Dog(Mammal):
    def __init__(self):
        pass

    def barks(self):
        print("guaffff guaffff")

class Dolphin(Mammal):
    def __init__(self):
        pass

    def swim(self):
        print("yeah! i can swim")

# Ahora, definamos clases a partir de Bird:
class Pigeon(Bird):
    def __init__(self):
        pass

    def fly(self):
        pass

class Parrot(object):
    def __init__(self):
        pass

    def sings(self):
        pass

class Penguin(object):
    def __init__(self):
        pass
    def swim(self):
        pass

# Todo bien hasta ahora, pero, ¿qué pasará con nuestro buen ornitorrinco?
# Es un mamífero, pero pone huevos en lugar de parir.

# Deberíamos hacer que herede de ambos?
# Ciertamente, aquí se pierde las razones por las cuales utilizar herencia:
# La semántica. Ya que no tiene sentido que un ornitorrinco herede cosas de un
# ave, ya que no lo es.
# La mecánica. Un ornitorrinco obtiene plumaje de la clase Ave, ¿cómo definimos esto?
# Un ornitorrinco también obtendría el método dar a luz de los mamiferos
class PlatyPusMultiInheritance(Mammal, Bird):
    def __init__(self):
        pass

    def call(self):
        print("grrrr")

# ¿Sería correcto establecer que el hecho de poner huevos es su forma de dar a luz?
# Tal vez, o tal vez no.
class PlatyPusOnlyMammal(Mammal):
    def __init__(self):
        pass

    def call(self):
        print("grrrr")

    def lay_eggs(self):
        pass

    def give_birth(self):
        lay_eggs()

# Aplicando solo herencia no parece ser la solución a este problema.
