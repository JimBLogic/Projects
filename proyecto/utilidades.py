import logging
import os

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
            logging.debug(f"Entrada inválida. Por favor, ingrese un {tipo.__name__} válido.")
            print(f"Entrada inválida. Por favor, ingrese un {tipo.__name__} válido.")
    raise ValueError("Número máximo de intentos alcanzado. Por favor, intente de nuevo más tarde.")

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
        logging.debug(f"Opción inválida. Las opciones válidas son: {', '.join(opciones_validas)}.")
        print(f"Opción inválida. Las opciones válidas son: {', '.join(opciones_validas)}.")
    raise ValueError("Número máximo de intentos alcanzado. Por favor, intente de nuevo más tarde.")

def agregar_asientos_en_rango(sala, dias, filas, numeros):
    """
    Agrega múltiples asientos a la sala de cine en los días, filas y números especificados.

    Args:
        sala (SalaCine): La instancia de la sala de cine.
        dias (list): Una lista de días de la semana.
        filas (list): Una lista de filas.
        numeros (list): Una lista de números de asientos.
    """
    for dia in dias:
        for fila in filas:
            for numero in numeros:
                try:
                    mensaje = sala.agregar_asiento(numero, fila, dia)
                    print(mensaje)
                except ValueError as e:
                    logging.debug(f"Error: {e}")
                    print(f"Error: {e}")

def reporte_disponibilidad(sala):
    """
    Genera un reporte de la disponibilidad de asientos por día.

    Args:
        sala (SalaCine): La instancia de la sala de cine.
    """
    dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    reporte = {dia: {"sin_agregar": 0, "disponibles": 0} for dia in dias_semana}

    for dia, asientos in sala.to_dict().items():
        for asiento in asientos:
            if asiento["reservado"]:
                continue
            if asiento["precio"] == 0:
                reporte[dia]["sin_agregar"] += 1
            else:
                reporte[dia]["disponibles"] += 1

    for dia, disponibilidad in reporte.items():
        print(f"{dia.capitalize()}: {disponibilidad['sin_agregar']} asientos sin agregar, {disponibilidad['disponibles']} asientos disponibles para reservar")