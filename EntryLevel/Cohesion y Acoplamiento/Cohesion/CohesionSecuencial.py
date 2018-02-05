#!/usr/bin/env python3
from functools import reduce

class Factura(object):
    costos = []
    def __init__(self, costos):
        self.costos = costos

    # Los resultados de calcularTotal se utilizan para calcularCostoIVA
    def calcularTotal(self):
        costosConIVA = self.calcularCostoIVA(self.costos)
        return reduce((lambda x,y: x+y), costosConIVA)

    def calcularCostoIVA(self, costos):
        return map(lambda x: x*1.12, costos)


costos = [10,20,30]
factura = Factura(costos)
total = factura.calcularTotal()
print("El total de la factura es: %d"%(total))
