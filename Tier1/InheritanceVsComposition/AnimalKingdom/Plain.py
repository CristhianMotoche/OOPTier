#!/usr/bin/env python3

# En estos ejemplos podemos ver la necesidad de evitar repetir código:
#
# La mayoría de mamiferos comparte los mismos atributos y métodos.
# Y lo mismo ocurre con las aves.

## Mammals:
class Cat(object):
    def __init__(self, name, fur, birthday, breed):
        pass

    def meow(self):
        print("meowwww")

    def give_birth(self):
        pass


class Dog(object):
    def __init__(self, name, fur, birthday, breed):
        pass

    def barks(self):
        print("guaffff guaffff")

    def give_birth(self):
        pass

class Dolphin(object):
    def __init__(self, name, birthday, fur):
        pass

    def swim(self):
        print("yeah! i can swim")

    def whistles(self):
        print("iiiiiii")

    def give_birth(self):
        pass

class PlatyPus(object):
    def __init__(self, name, birthday, fur):
        pass

    def lay_eggs(self):
        print("Lay egg")

    def call(self):
        print("grrrr")

## Birds
class Pigeon(object):
    def __init__(self, name, birthday, plumage):
        pass

    def fly(self):
        pass

    def lay_eggs(self):
        pass

class Parrot(object):
    def __init__(self, name, birthday, plumage):
        pass

    def fly(self):
        pass

    def lay_eggs(self):
        pass

class Penguin(object):
    def __init__(self, name, birthday, plumage):
        pass

    def lay_eggs(self):
        pass

    def swim(self):
        pass
