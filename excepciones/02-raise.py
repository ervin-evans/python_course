def verificar_edad(edad):
    """Metodo que verifica que la edad sea valida"""
    if edad < 0:
        raise ValueError("Edad no valida")
    print("Edad valida")


verificar_edad(-3)
