#!/usr/bin/env python3

# Ahora, vamos a resolver este problema de repetición de código con composición:
class AnimalBeing(object):
    def __init__(self, name, birthday):
        pass

class Barker(object):
    def __init__(self):
        pass

    def barks(self):
        print("guaffff guaffff")

class Swimmer(object):
    def __init__(self):
        pass

    def swim(self):
        print("yeah! i can swim")

class Meower(object):
    def __init__(self):
        pass

    def meow(self):
        print("meowwww")

class Flyer(object):
    def __init__(self):
        pass

    def fly(self):
        pass

class LayEgger(object):
    def __init__(self):
        pass

    def lay_eggs(self):
        pass

# Ahora, definamos clases a partir de todas las anteriores:
class Cat(object):
    def __init__(self, name, birthday):
        self.animal_being = AnimalBeing(name, birthday)
        self.meower_system = Meower()

class Dog(object):
    def __init__(self, name, birthday):
        self.animal_being = AnimalBeing(name, birthday)
        self.barker_system = Barker()

class Parrot(object):
    def __init__(self, name, birthday):
        self.animal_being = AnimalBeing(name, birthday)
        self.flyer_system = Flyer()

    def sing(self):
        pass

# Y el ornitorrinco?
class PlatyPus(object):
    def __init__(self, name, birthday):
        self.animal_being = AnimalBeing(name, birthday)
        self.swimmer_system = Swimmer()
        self.lay_egger_system = LayEgger()

# Genial! Nuestro ornitorrinco ahora solo tiene sus propiedades natas.
# Sin embargo, los atributos no parecen tener mucha semántica.
# ¿Un ornitorrinco tiene un sistema de poner huevos? Tal vez exista
# un mejor nombre para ello.
