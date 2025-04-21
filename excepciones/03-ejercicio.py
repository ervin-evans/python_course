"""Nivel facil """
try:
    numerador = int(input("Ingrese el numerador: "))
    denominador = int(input("Ingrese el denominador: "))
    resultado = numerador/denominador
except ZeroDivisionError:
    print("No se puede dividir entre cero")
except ValueError:
    print("Debe ingresar un numero entero")
else:
    print(f"El resulado es: {resultado}")
finally:
    print("Fin del programa")
