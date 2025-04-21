"""
    reduce() aplica una función acumulativa a los elementos de un iterable para reducirlo a un solo valor.
    Nota: Para usar reduce(), debes importarla del módulo functools.
"""
from functools import reduce


numeros = [1, 2, 7, 3, 9, 7, 1, 8, 4]
suma_total = reduce(lambda a, b: a+b, numeros)
print(suma_total)
