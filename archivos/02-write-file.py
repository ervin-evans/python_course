"""Sustituyendo el contendio de un archivo"""


def file_content(filename):
    """Lee el contenido del un archivo"""
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


print("El contenido del archivo antes: ")
print(file_content("datos.txt"))
with open("datos.txt", "w", encoding="utf-8") as file:
    file.write("\nEstamos sustituyendo el contenido del archivo")

print("Contenido del archivo despues: ")
print(file_content("datos.txt"))
