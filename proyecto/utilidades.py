import logging
from mensajes import Mensajes

# Configurar el logger
logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def calcular_descuento(precio_base, edad, dia):
    """
    Calcula el descuento aplicable según el día de la semana y la edad del espectador.

    Args:
        precio_base (float): El precio base del asiento.
        edad (int): La edad del espectador.
        dia (str): El día de la semana.

    Returns:
        float: El descuento aplicable.
    """
    descuento = 0
    if dia.lower() == "miércoles":
        descuento += 0.20
    if edad >= 65:
        descuento += 0.30
    return descuento

def validar_entrada(mensaje, tipo=int, rango=None):
    """
    Valida la entrada del usuario asegurándose de que sea del tipo y rango especificados.

    Args:
        mensaje (str): El mensaje a mostrar al usuario.
        tipo (type): El tipo de dato esperado.
        rango (tuple, optional): Un rango de valores permitidos.

    Returns:
        tipo: La entrada validada del usuario.
    """
    intentos = 0
    while intentos < 3:
        try:
            entrada = tipo(input(mensaje))
            if rango and (entrada < rango[0] or entrada > rango[1]):
                raise ValueError
            if tipo == int and (entrada < 0):
                raise ValueError
            return entrada
        except ValueError:
            intentos += 1
            logging.debug(Mensajes.opcion_invalida())
            print(Mensajes.opcion_invalida())
    logging.error(Mensajes.max_intentos())
    raise ValueError(Mensajes.max_intentos())

def validar_opcion(mensaje, opciones_validas):
    """
    Valida que la opción ingresada por el usuario esté dentro de las opciones válidas.

    Args:
        mensaje (str): El mensaje a mostrar al usuario.
        opciones_validas (list): Una lista de opciones válidas.

    Returns:
        str: La opción validada del usuario.
    """
    intentos = 0
    while intentos < 3:
        entrada = input(mensaje).strip().lower()
        if entrada in opciones_validas:
            return entrada
        intentos += 1
        logging.debug(Mensajes.opcion_invalida())
        print(Mensajes.opcion_invalida())
    raise ValueError(Mensajes.max_intentos())