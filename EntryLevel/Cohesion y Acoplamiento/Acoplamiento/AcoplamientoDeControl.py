#!/usr/bin/env python3

# Esta función está acoplada al parámetro boolean.
# Dependiendo de su valor de verdad se ejecutará una operación u otra.
def splitByConditional(value, boolean):
    if boolean:
        return value*2
    else:
        return value**2

val = splitByConditional(5, True)
print(val)

val = splitByConditional(5, False)
print(val)

# Se puede resolver con un acoplamiento normal
def needDouble(val):
    return prod(val,2)

def needSquare(val):
    return square(val,2)

def prod(a,b):
    return a*b

def square(a,n):
    return a**n

val = needDouble(5)
print(val)

val = needSquare(5)
print(val)
