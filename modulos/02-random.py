import random


print(random.randint(1, 10))  # Numero aleatorio entre 1 y 10
print(random.uniform(1.4, 3.4))  # Numero decimal aleatorio
print(random.choice([1, 2, 3, 4, 7, 8, 9]))  # Elige un numero al azar
# 7 numeros sin repetir (toma los numeros entre 1 y 70)
print(random.sample(range(1, 70), 7))
