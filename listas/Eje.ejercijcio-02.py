# Tienes dos listas: nombres y edades
import operator


nombres = ["Sandra", "Martha", "Dominic", "Raul"]
edades = [12, 24, 78, 30]
# Únelas usando zip y crea un diccionario {nombre: edad}
dicc = {}
for nombre, edad in zip(nombres, edades):
    dicc.update({nombre: edad})
# Luego ordénalos por edad ascendente
dict_sorted = sorted(dicc.items(), key=operator.itemgetter(1))
print(dict_sorted)
