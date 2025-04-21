from datetime import datetime, timedelta

ahora = datetime.now()
print(ahora)  # imprime la fecha y la hora actual

# Acceder a partes especificas
print(f"Fecha: {ahora.year}-{ahora.month}-{ahora.day}")
print(f"Hora: {ahora.hour}:{ahora.minute}:{ahora.second}")


# sumar o restar dias
maniana = ahora + timedelta(days=1)
ayer = ahora - timedelta(days=1)

print(f"Maniana: {maniana}")
print(f"Ayer: {ayer}")
