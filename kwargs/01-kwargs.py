""" **kwargs permite recibir un número variable de argumentos nombrados (clave: valor)."""


def mostrar_info(**kwargs):
    """Muestra informacion dada en formato clave:valor"""
    for clave, valor in kwargs.items():
        print(f"{clave} - {valor}")


mostrar_info(nombre="Carlos", edad=30, pais="Guatemala")
