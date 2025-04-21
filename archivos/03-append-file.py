with open("datos.txt", "a", encoding="utf-8") as file:
    file.write("Estamos agregando esta linea al contenido que ya estaba")

with open("datos.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
