import logging
import json
import sys
import os

# Asegurar que la ruta es correcta
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importar los módulos necesarios
from proyecto.mensajes import Mensajes

# Configurar el logger
logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

MAX_ROWS = 10
MAX_SEATS_PER_ROW = 10

def calculate_discount(price, age, day):
    """
    Calcula el descuento basado en el precio, la edad y el día de la semana.
    
    Args:
        price (float): El precio base del asiento.
        age (int): La edad del espectador.
        day (str): El día de la semana.
    
    Returns:
        float: El porcentaje de descuento a aplicar.
    """
    discount = 0.0
    if day == "miércoles":
        discount = 0.2
    if age >= 65:
        discount += 0.3
    logging.debug(f"Descuento calculado: {discount} para precio: {price}, edad: {age}, día: {day}")
    return discount

def calculate_final_price(price, age, day):
    """
    Calcula el precio final aplicando el descuento correspondiente.
    
    Args:
        price (float): El precio base del asiento.
        age (int): La edad del espectador.
        day (str): El día de la semana.
    
    Returns:
        float: El precio final después de aplicar el descuento.
    """
    discount = calculate_discount(price, age, day)
    final_price = price * (1 - discount)
    logging.debug(f"Precio final calculado: {final_price} para precio: {price}, edad: {age}, día: {day}")
    return final_price

def validate_input(prompt, input_type, valid_range):
    attempts = 0
    while attempts < 3:
        try:
            user_input = input(prompt)
            if input_type == str:
                return user_input
            value = input_type(user_input)
            if isinstance(valid_range, range):
                if value in valid_range:
                    return value
                else:
                    print(f"Entrada inválida: El valor debe estar entre {valid_range.start} y {valid_range.stop - 1}. Ejemplo: {valid_range.start}")
            else:
                return value
        except ValueError:
            print(f"Entrada inválida: invalid literal for {input_type.__name__}() with base 10: '{user_input}'")
        except StopIteration:
            raise ValueError("Número máximo de intentos alcanzado")
        attempts += 1
    raise ValueError("Número máximo de intentos alcanzado")

def validate_option(prompt, options):
    """
    Valida que la opción ingresada esté dentro de las opciones permitidas.
    
    Args:
        prompt (str): El mensaje a mostrar al usuario.
        options (list): Una lista de opciones válidas.
    
    Returns:
        str: La opción validada del usuario.
    
    Raises:
        ValueError: Si la opción no es válida después de tres intentos.
    """
    attempts = 3
    while attempts > 0:
        option = input(prompt).lower()
        if option in options:
            return option
        else:
            print(f"Opción inválida. Las opciones válidas son: {', '.join(options)}")
            logging.error(f"Opción inválida: {option}")
            attempts -= 1
    raise ValueError("Número máximo de intentos alcanzado")

def update_seat(cinema, day, row, number, new_row, new_number):
    """
    Actualiza la información de un asiento específico.
    
    Args:
        cinema (SalaCine): La instancia de la sala de cine.
        day (str): El día de la semana.
        row (str): La fila del asiento.
        number (int): El número del asiento.
        new_row (str): La nueva fila del asiento.
        new_number (int): El nuevo número del asiento.
    
    Returns:
        str: Un mensaje indicando si la actualización fue exitosa o si el asiento no fue encontrado.
    """
    if len(cinema.get_estado()[day]) >= MAX_ROWS:
        return "Número máximo de filas alcanzado."
    if any(asiento.get_fila() == new_row and asiento.get_numero() == new_number for asiento in cinema.get_estado()[day]):
        return "El asiento ya existe en el sistema."
    return cinema.actualizar_asiento(day, row, number, new_row, new_number)

def save_state_file(file, state):
    """
    Guarda el estado en un archivo JSON.
    
    Args:
        file (str): El nombre del archivo.
        state (dict): El estado a guardar.
    """
    try:
        with open(file, 'w') as f:
            json.dump(state, f, indent=4)
        logging.info(f"Estado guardado en el archivo {file}.")
    except Exception as e:
        logging.error(f"Error al guardar el archivo {file}: {e}")

def reset_state_file(file, initial_state):
    """
    Resetea el archivo de estado JSON con el estado inicial.
    
    Args:
        file (str): El nombre del archivo.
        initial_state (dict): El estado inicial a guardar.
    """
    try:
        with open(file, 'w') as f:
            json.dump(initial_state, f, indent=4)
        logging.info(f"Archivo {file} reseteado con el estado inicial.")
    except Exception as e:
        logging.error(f"Error al resetear el archivo {file}: {e}")

def save_state(filename, state):
    """
    Guarda el estado en un archivo JSON.
    
    Args:
        filename (str): El nombre del archivo.
        state (dict): El estado a guardar.
    """
    save_state_file(filename, state)

def reset_state(filename, initial_state):
    """
    Resetea el estado en un archivo JSON.
    
    Args:
        filename (str): El nombre del archivo.
        initial_state (dict): El estado inicial a guardar.
    """
    reset_state_file(filename, initial_state)