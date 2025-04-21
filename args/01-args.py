"""*args permite recibir un número variable de argumentos posicionales (no nombrados) en una función."""


def suma_total(*args):
    """Suma todos los argumentos posicionales"""
    return sum(args)


print(suma_total(1, 2, 3))
print(suma_total(1, 2, 3, 4, 7, 8, 9))
