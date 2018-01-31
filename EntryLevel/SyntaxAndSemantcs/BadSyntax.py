#! /usr/bin/python3
# This example has bad syntax:

x = 3

if x == 3
    print("The number 3")

# El resulado de intentar ejecutar este script será:

# $ python BadSyntax.py
#   File "BadSyntax.py", line 6
#     if x == 3
#             ^
# SyntaxError: invalid syntax

# El SyntaxError se produce debido a que el condicional en Python debe terminar
# en dos puntos ":".
