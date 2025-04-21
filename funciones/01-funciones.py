import os


def sumar(num1: int, num2: int):
    """Funcion que suma 2 numeros"""
    return num1 + num2


def restar(num1: int, num2: int):
    """Funcion que resta 2 numeros"""
    return num1-num2


def multiplicar(num1: int, num2: int):
    """Funcion que multiplica 2 numeros"""
    return num1 * num2


def dividir(num1: int, num2: int):
    """Funcion que divide 2 numeros"""
    if num2 == 0:
        raise ZeroDivisionError("La division por 0 no se puede efectuar")
    return num1 / num2


def clear_terminal():
    """Limpia la terminal"""
    os.system("cls" if os.name == "nt" else "clear")


def get_int(message: str) -> int:
    """Solicita el usuario un entero y valida la entrada"""
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Entrada invalida. Por favor, ingrese un numero entero")


def main():
    """Funcion principal"""
    operaciones = {
        1: ("sumar", sumar),
        2: ("restar", restar),
        3: ("multiplicar", multiplicar),
        4: ("dividir", dividir)
    }
    print("Selecciones un operacion")
    for clave, (nombre, _) in operaciones.items():
        print(f"{clave}.{nombre}")
    opcion = get_int("Elige una opcion (1-4)")
    if opcion not in operaciones:
        print("Opcion no valida")
        return
    clear_terminal()
    num1 = get_int("Ingrese el primer numero: ")
    num2 = get_int("Ingrese el segundo numero: ")
    try:
        nombre_op, funcion = operaciones[opcion]
        resultado = funcion(num1, num2)
        print(f"El resultado de la {nombre_op.lower()} es {resultado:,.2f}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
