#!/usr/bin/env python3

from Duck import Duck
from Pigeon import Pigeon

def expect_a_bird(duck):
    # Asking Forgiveness, Not Permission (EAFP)
    try:
        # It flies
        print("Does it fly?")
        duck.fly()
        # It makes noises
        print("What does the bird say?")
        duck.makenoise()
        # It must be...
        print("Mmm....")
        duck.it_is()
        print("")
    except AttributeError as e:
        print(e)

def main():
    duck = Duck()
    pigeon = Pigeon()
    expect_a_bird(duck)
    expect_a_bird(pigeon)
    expect_a_bird({})

if __name__ == '__main__':
    main()
