"""Un diccionario es una colección de pares clave-valor. Muy útil para representar entidades con propiedades."""

persona = {
    "nombre": "Pedro",
    "edad": 43,
    "ciudad": "Yucatan"
}

# Acceder
print(persona["nombre"])

# Agregar
persona["profesion"] = "Ingeniero"

# modificar
persona["nombre"] = "Pedro Solis"

# Eliminar
del persona["ciudad"]

# Recorrer
for clave, valor in persona.items():
    print(f"{clave} - {valor}")
