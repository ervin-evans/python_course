# Leyendo todo el contenido de un archivo
with open("datos.txt", "r", encoding="utf-8") as file:
    contenido = file.read()
    print(contenido)

print("************ Leyendo el archivo linea por linea *****************")
# Leyendo el contenido linea por linea
with open("datos.txt", "r", encoding="utf-8") as file:
    for linea in file:
        print(linea.strip())  # .strip() elimina el \n al final.
