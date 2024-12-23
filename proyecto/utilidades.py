import json
import logging
import os

# Configurar el logger
logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_discount(price, age, day):
    """
    Calcula el descuento basado en la edad y el día de la semana.
    
    Args:
        price (float): El precio base.
        age (int): La edad del espectador.
        day (str): El día de la semana.
    
    Returns:
        float: El porcentaje de descuento a aplicar.
    """
    discount = 0.0
    if day.lower() == "miércoles":
        discount += 0.2
    if age >= 65:
        discount += 0.3
    logging.debug(f'Calculado descuento de {discount} para edad {age} y día {day}.')
    return discount

def calculate_final_price(price, age, day):
    """
    Calcula el precio final aplicando los descuentos correspondientes.
    
    Args:
        price (float): El precio base.
        age (int): La edad del espectador.
        day (str): El día de la semana.
    
    Returns:
        float: El precio final después de aplicar los descuentos.
    """
    discount = calculate_discount(price, age, day)
    final_price = price * (1 - discount)
    logging.debug(f'Precio final calculado: {final_price} para precio base {price}, edad {age}, día {day}.')
    return final_price

def validate_input(prompt, input_type, valid_range):
    """
    Valida la entrada del usuario.
    
    Args:
        prompt (str): El mensaje a mostrar al usuario.
        input_type (type): El tipo de dato esperado.
        valid_range (range): El rango de valores válidos.
    
    Returns:
        input_type: El valor ingresado por el usuario.
    
    Raises:
        ValueError: Si el valor ingresado no es válido.
    """
    while True:
        try:
            value = input_type(input(prompt))
            if isinstance(valid_range, range) and value in valid_range:
                logging.debug(f'Entrada validada: {value}')
                return value
            elif isinstance(valid_range, str) and value.upper() in valid_range:
                logging.debug(f'Entrada validada: {value}')
                return value.upper()
            else:
                raise ValueError
        except ValueError:
            logging.error('Entrada inválida. Inténtalo de nuevo.')
            print("Entrada inválida. Inténtalo de nuevo.")

def validate_option(prompt, options):
    """
    Valida la opción ingresada por el usuario.
    
    Args:
        prompt (str): El mensaje a mostrar al usuario.
        options (list): Lista de opciones válidas.
    
    Returns:
        str: La opción seleccionada por el usuario.
    """
    while True:
        option = input(prompt).lower()
        if option in options:
            logging.debug(f'Opción validada: {option}')
            return option
        else:
            logging.error('Opción inválida. Inténtalo de nuevo.')
            print("Opción inválida. Inténtalo de nuevo.")

def save_state(filename, state):
    """
    Guarda el estado en un archivo .json.
    
    Args:
        filename (str): Nombre del archivo .json donde se guardará el estado.
        state (list): Lista de diccionarios con el estado.
    """
    with open(filename, 'w') as file:
        json.dump(state, file, indent=4)
    logging.debug(f'Estado guardado en {filename}.')

def reset_state(filename, initial_state):
    """
    Resetea el estado a su estado inicial.
    
    Args:
        filename (str): Nombre del archivo .json donde se guardará el estado.
        initial_state (list): Lista de diccionarios con el estado inicial.
    """
    save_state(filename, initial_state)
    logging.debug(f'Estado restablecido en {filename}.')

def load_state_file(filename):
    """
    Carga el estado desde un archivo JSON.
    
    Args:
        filename (str): El nombre del archivo.
    
    Returns:
        list: El estado cargado desde el archivo.
    """
    try:
        with open(filename, 'r') as file:
            state = json.load(file)
        logging.debug(f'Estado cargado desde {filename}.')
        return state
    except FileNotFoundError:
        logging.error(f'Archivo {filename} no encontrado.')
        return []

def save_state_file(filename, state):
    """
    Guarda el estado en un archivo JSON.
    
    Args:
        filename (str): El nombre del archivo.
        state (list): El estado a guardar.
    """
    with open(filename, 'w') as file:
        json.dump(state, file, indent=4)
    logging.debug(f'Estado guardado en {filename}.')

def reset_state_file(filename, initial_state):
    """
    Restablece el estado inicial en un archivo.
    
    Args:
        filename (str): El nombre del archivo.
        initial_state (dict): El estado inicial a establecer.
    """
    save_state_file(filename, initial_state)
    logging.debug(f'Estado restablecido en {filename}.')