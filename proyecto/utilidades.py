import logging
from proyecto.mensajes import Mensajes

# Configurar el logger
logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def calcular_descuento(precio, edad, dia):
    """
    Calcula el descuento basado en el precio, la edad y el día de la semana.
    """
    descuento = 0.0
    if dia == "miércoles":
        if edad >= 60:
            descuento = 0.5
        elif edad < 18:
            descuento = 0.2
    elif dia in ["lunes", "domingo"]:
        if edad >= 60:
            descuento = 0.3
    logging.debug(f"Descuento calculado: {descuento} para precio: {precio}, edad: {edad}, día: {dia}")
    return descuento

def calcular_precio_final(precio, edad, dia):
    """
    Calcula el precio final aplicando el descuento correspondiente.
    """
    descuento = calcular_descuento(precio, edad, dia)
    precio_final = precio * (1 - descuento)
    logging.debug(f"Precio final calculado: {precio_final} para precio: {precio}, edad: {edad}, día: {dia}")
    return precio_final

def validar_entrada(mensaje, tipo, rango=None):
    """
    Valida la entrada del usuario.
    """
    intentos = 3
    while intentos > 0:
        entrada = input(mensaje)
        try:
            entrada = tipo(entrada)
            if rango and (entrada < rango[0] or entrada > rango[1]):
                raise ValueError(f"El valor debe estar entre {rango[0]} y {rango[1]}. Ejemplo: {rango[0]}")
            return entrada
        except ValueError as e:
            print(f"Entrada inválida: {e}")
            logging.error(f"Entrada inválida: {e}")
            intentos -= 1
    raise ValueError("Número máximo de intentos alcanzado")

def validar_opcion(mensaje, opciones):
    """
    Valida que la opción ingresada esté dentro de las opciones permitidas.
    """
    intentos = 3
    while intentos > 0:
        opcion = input(mensaje).lower()
        if opcion in opciones:
            return opcion
        else:
            print(f"Opción inválida. Las opciones válidas son: {', '.join(opciones)}")
            logging.error(f"Opción inválida: {opcion}")
            intentos -= 1
    raise ValueError("Número máximo de intentos alcanzado")

def actualizar_asiento(sala_cine, dia, fila, numero, nueva_fila, nuevo_numero):
    """
    Actualiza la información de un asiento específico.
    
    Args:
        sala_cine (SalaCine): La instancia de la sala de cine.
        dia (str): El día de la semana.
        fila (str): La fila del asiento.
        numero (int): El número del asiento.
        nueva_fila (str): La nueva fila del asiento.
        nuevo_numero (int): El nuevo número del asiento.
    
    Returns:
        str: Un mensaje indicando si la actualización fue exitosa o si el asiento no fue encontrado.
    """
    return sala_cine.actualizar_asiento(dia, fila, numero, nueva_fila, nuevo_numero)

def guardar_estado(archivo, estado):
    """
    Guarda el estado en un archivo JSON.
    
    Args:
        archivo (str): El nombre del archivo.
        estado (dict): El estado a guardar.
    """
    from proyecto.verificar_sistema import save_state_file
    save_state_file(archivo, estado)

def resetear_estado(archivo, estado_inicial):
    """
    Resetea el estado en un archivo JSON.
    
    Args:
        archivo (str): El nombre del archivo.
        estado_inicial (dict): El estado inicial a guardar.
    """
    from proyecto.verificar_sistema import reset_state_file
    reset_state_file(archivo, estado_inicial)

def validate_input(value):
    # ...existing code...
    pass

def validate_option(option):
    # ...existing code...
    pass

def save_state(state):
    # ...existing code...
    pass

def reset_state():
    # ...existing code...
    pass

def calculate_final_price(price, discount):
    # ...existing code...
    pass