"""
    Haz una función llamada calcular_media(lista) que
    Reciba una lista de números
    Devuelva la media aritmética
    Si la lista está vacía, lance un ValueError
"""


def calcular_media(lista):
    if not lista:
        raise ValueError("La lista esta vacia")
    return sum(lista)/len(lista)


try:
    resultado = calcular_media([10, 20, 30])
    # resultado = calcular_media([])
except ValueError as e:
    print(f"{e}")
else:
    print(f"El resultado es: {resultado}")
