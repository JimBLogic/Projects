import logging
import os

# Reiniciar el archivo de depuración
if os.path.exists('debug.log'):
    os.remove('debug.log')

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
    while True:
        try:
            entrada = tipo(input(mensaje))
            if rango and (entrada < rango[0] or entrada > rango[1]):
                raise ValueError
            return entrada
        except ValueError:
            logging.debug(f"Entrada inválida. Por favor, ingrese un {tipo.__name__} válido.")

def validar_opcion(mensaje, opciones_validas):
    """
    Valida que la opción ingresada por el usuario esté dentro de las opciones válidas.

    Args:
        mensaje (str): El mensaje a mostrar al usuario.
        opciones_validas (list): Una lista de opciones válidas.

    Returns:
        str: La opción validada del usuario.
    """
    while True:
        entrada = input(mensaje).strip().lower()
        if entrada in opciones_validas:
            return entrada
        logging.debug(f"Opción inválida. Las opciones válidas son: {', '.join(opciones_validas)}.")

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

def simulador_precios(precio_base, dia_semana, edad):
    """
    Simula el precio de un asiento aplicando descuentos según el día de la semana y la edad del espectador.

    Args:
        precio_base (float): El precio base del asiento.
        dia_semana (str): El día de la semana.
        edad (int): La edad del espectador.

    Returns:
        tuple: El precio final y una lista de descuentos aplicados.
    """
    descuento = 0.0
    descuentos_aplicados = []

    if dia_semana == "miércoles":
        descuento += 0.2
        descuentos_aplicados.append("20% de descuento los miércoles")
    if edad > 65:
        descuento += 0.3
        descuentos_aplicados.append("30% de descuento para mayores de 65 años")

    precio_final = precio_base * (1 - descuento)
    return precio_final, descuentos_aplicados

def reporte_disponibilidad(sala):
    """
    Genera un reporte de la disponibilidad de asientos por día.

    Args:
        sala (SalaCine): La instancia de la sala de cine.
    """
    dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    reporte = {dia: 0 for dia in dias_semana}

    for asiento in sala.to_dict():
        if not asiento["reservado"]:
            reporte[asiento["dia_semana"]] += 1

    for dia, disponibles in reporte.items():
        print(f"{dia.capitalize()}: {disponibles} asientos disponibles")