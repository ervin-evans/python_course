matriz = [
    [1, 2, 3],
    [2, 4, 7],
    [3, 7, 9]
]
print(matriz[0])
print(matriz[0][1])

# Recorrer con for anidados
print("Recorriendo matriz...")
for fila in matriz:
    for valor in fila:
        print(valor, end="")
    print()
