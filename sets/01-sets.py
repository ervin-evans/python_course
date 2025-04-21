"""Un set es una colección no ordenada, sin elementos duplicados, y mutable."""
colores = {"rojo", "verde", "amarillo", "morado"}

print(colores)

# agregar
colores.add("rosa")

# Eliminar
colores.remove("verde")

# comprobar existencia
print("rojo" in colores)

# recorrer set
for color in colores:
    print(color)

# eliminar duplicados
numeros = [1, 1, 2, 8, 3, 0, 4, 8, 2, 9, 3, 8, 7, 2]
numeros_sin_repetir = set(numeros)
print(numeros_sin_repetir)
