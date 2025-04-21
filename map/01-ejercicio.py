"""Dada la lista edades = [18, 21, 16, 25, 30], 
    usa map() para crear una nueva lista que contenga las edades incrementadas en 1."""
edades = [18, 21, 16, 25, 30]
edades_actualizadas = list(map(lambda x: x+1, edades))
print(edades)
print(edades_actualizadas)
