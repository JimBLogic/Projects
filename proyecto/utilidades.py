import json
import logging

# Configurar el logger
logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_discount(price, age, day):
    """
    Calcula el descuento aplicable basado en la edad y el día de la semana.
    
    Args:
        price (float): El precio base.
        age (int): La edad del espectador.
        day (str): El día de la semana.
    
    Returns:
        float: El porcentaje de descuento a aplicar.
    """
    discount = 0
    if day.lower() == "miércoles":
        discount += 0.20
    if age >= 65:
        discount += 0.30
    logging.debug(f'Calculado descuento de {discount} para edad {age} y día {day}.')
    return discount

def calculate_final_price(price, age, day):
    """
    Calcula el precio final aplicando el descuento correspondiente.
    
    Args:
        price (float): El precio base.
        age (int): La edad del espectador.
        day (str): El día de la semana.
    
    Returns:
        float: El precio final después de aplicar el descuento.
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
        valid_range (tuple): El rango válido de valores.
    
    Returns:
        input_type: El valor validado.
    """
    while True:
        try:
            value = input_type(input(prompt))
            if value not in valid_range:
                raise ValueError
            logging.debug(f'Entrada validada: {value}')
            return value
        except ValueError:
            logging.error('Entrada inválida. Inténtalo de nuevo.')

def validate_option(prompt, options):
    """
    Valida que la opción seleccionada por el usuario sea válida.
    
    Args:
        prompt (str): El mensaje a mostrar al usuario.
        options (list): La lista de opciones válidas.
    
    Returns:
        str: La opción validada.
    """
    while True:
        option = input(prompt).strip().lower()
        if option in options:
            logging.debug(f'Opción validada: {option}')
            return option
        logging.error('Opción inválida. Inténtalo de nuevo.')

def save_state(filename, state):
    """
    Guarda el estado en un archivo.
    
    Args:
        filename (str): El nombre del archivo.
        state (dict): El estado a guardar.
    """
    with open(filename, 'w') as file:
        json.dump(state, file, indent=4)
    logging.debug(f'Estado guardado en {filename}.')

def reset_state(filename, initial_state):
    """
    Restablece el estado inicial en un archivo.
    
    Args:
        filename (str): El nombre del archivo.
        initial_state (dict): El estado inicial a establecer.
    """
    save_state(filename, initial_state)
    logging.debug(f'Estado restablecido en {filename}.')

def load_state_file(filename):
    """
    Carga el estado desde un archivo.
    
    Args:
        filename (str): El nombre del archivo.
    
    Returns:
        dict: El estado cargado.
    """
    try:
        with open(filename, 'r') as file:
            state = json.load(file)
        logging.debug(f'Estado cargado desde {filename}.')
        return state
    except FileNotFoundError:
        logging.error(f'Archivo {filename} no encontrado.')
        return None
    except json.JSONDecodeError:
        logging.error(f'Error al decodificar JSON desde {filename}.')
        return None

def save_state_file(filename, state):
    """
    Guarda el estado en un archivo.
    
    Args:
        filename (str): El nombre del archivo.
        state (dict): El estado a guardar.
    """
    save_state(filename, state)