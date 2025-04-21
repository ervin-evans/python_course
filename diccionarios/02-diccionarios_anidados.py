alumnos = {
    "Ana": {"edad": 18, "nota": 10},
    "Pedro": {"edad": 19, "nota": 8},
    "Juan": {"edad": 29, "nota": 9}
}
print(alumnos["Juan"]["nota"])
# Recorriendo un diccionario anidado
for nombre, datos in alumnos.items():
    print(f"Nombre: {nombre} - Edad: {datos["edad"]} - nota: {datos["nota"]}")
