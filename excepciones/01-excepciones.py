try:
    numero = int(input("Ingrese un numero: "))
    resultado = 10/numero
except ZeroDivisionError:
    print("No puedes dividir entre cero")
except ValueError:
    print("Debes ingresar un numero")
else:
    print(f"El resultado es: {resultado}")
finally:
    print("Programa terminado")
