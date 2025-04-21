"""Una lista es una colección ordenada y mutable (puedes cambiarla) que puede contener elementos duplicados."""
frutas = ["Manzanas", "Uvas", "Sandia"]

# Acceder
print(frutas[0])

# Agregar
frutas.append("Naranjas")

# Insertar un elemento en una posicion especifica
frutas.insert(2, "Mandarinas")

# Recorrer
for fruta in frutas:
    print(fruta)

# Eliminar por valor
frutas.remove("Manzanas")

# Eliminar por posicion
del frutas[3]


print(frutas)
