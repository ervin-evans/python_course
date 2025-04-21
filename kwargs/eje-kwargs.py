def crear_usuario(nombre, *hobbies, **datos):
    print(f"Nombre: {nombre}")
    print(f"Hobbies: {hobbies}")
    for clave, valor in datos.items():
        print(f"{clave} - {valor}")


crear_usuario("Sandra", "Jugar videojuegos", "Jugar futbol",
              "Programar", edad=23, ciudad="Madrid")
