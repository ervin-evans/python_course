"""filter() filtra elementos de un iterable según una condición.
 Solo devuelve aquellos elementos para los cuales la función (o lambda) devuelve True."""
numeros = [1, 2, 4, 7, 89, 9, 1, 33, 98, 2, 0, 1, 89]
numeros_filtrados = list(filter(lambda x: x > 20, numeros))
print(numeros_filtrados)
