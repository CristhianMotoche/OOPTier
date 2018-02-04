#!/usr/bin/env python3

# Esta unidad de sw es independiente
def prod(a,b):
    return a*b

# Esta unidad de sw depende de prod
def fact(n):
    if n <= 1:
        return 1
    else:
        return prod(n, fact(n-1))

print(fact(10))
