"""La funcion map() aplica un funcion a todos los elementos de un iterable"""

numeros = [1, 2, 3, 4, 7, 8, 9]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)
