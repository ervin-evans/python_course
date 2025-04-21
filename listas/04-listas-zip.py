"""zip une dos listas elemento a elemento"""
nombres = ["ana", "luis", "martha"]
notas = [10, 9, 7]
for nombre, nota in zip(nombres, notas):
    print(f"{nombre} saco {nota}")
