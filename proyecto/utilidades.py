import logging
import json

# Configurar el logger
logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

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
    """
    Valida la entrada del usuario.
    
    Args:
        prompt (str): El mensaje que se muestra al usuario.
        input_type (type): El tipo de dato que se espera.
        valid_range (range): El rango de valores válidos.
    
    Returns:
        input_type: El valor ingresado por el usuario.
    
    Raises:
        ValueError: Si la entrada no es válida.
    """
    while True:
        try:
            user_input = input_type(input(prompt))
            if valid_range and user_input not in valid_range:
                raise ValueError
            return user_input
        except ValueError:
            print("Entrada inválida. Por favor, intente de nuevo.")
            logging.error("Entrada inválida.")

def validate_option(prompt, options):
    """
    Valida la opción seleccionada por el usuario.
    
    Args:
        prompt (str): El mensaje que se muestra al usuario.
        options (list): La lista de opciones válidas.
    
    Returns:
        str: La opción seleccionada por el usuario.
    
    Raises:
        ValueError: Si la opción no es válida.
    """
    while True:
        user_input = input(prompt)
        if user_input in options:
            return user_input
        else:
            print("Opción inválida. Por favor, intente de nuevo.")
            logging.error("Opción inválida.")

def save_state(filename, state):
    """
    Guarda el estado de la sala de cine en un archivo JSON.
    
    Args:
        filename (str): El nombre del archivo JSON.
        state (dict): El estado de la sala de cine.
    """
    # Convertir objetos Asiento a diccionarios
    state_dict = {dia: [asiento.to_dict() for asiento in asientos] for dia, asientos in state.items()}
    with open(filename, 'w') as file:
        json.dump(state_dict, file, indent=4)
    logging.info(f"Estado guardado en el archivo {filename}.")

def reset_state(filename, initial_state):
    """
    Resetea el estado del archivo JSON con el estado inicial proporcionado.
    
    Args:
        filename (str): El nombre del archivo JSON.
        initial_state (dict): El estado inicial para resetear el archivo.
    """
    with open(filename, 'w') as file:
        json.dump(initial_state, file, indent=4)
    logging.info(f"Archivo {filename} reseteado con el estado inicial.")

def reset_state_file(filename, initial_state):
    """
    Resetea el estado del archivo JSON con el estado inicial proporcionado.
    
    Args:
        filename (str): El nombre del archivo JSON.
        initial_state (dict): El estado inicial para resetear el archivo.
    """
    with open(filename, 'w') as file:
        json.dump(initial_state, file, indent=4)
    logging.info(f"Archivo {filename} reseteado con el estado inicial.")

def update_state(filename, day, row, number, new_row, new_number):
    """
    Actualiza la información de un asiento específico en el archivo JSON.
    
    Args:
        filename (str): El nombre del archivo JSON.
        day (str): El día de la semana.
        row (str): La fila del asiento.
        number (int): El número del asiento.
        new_row (str): La nueva fila del asiento.
        new_number (int): El nuevo número del asiento.
    """
    state = load_state_file(filename)
    if state:
        for asiento in state[day]:
            if asiento['fila'] == row and asiento['numero'] == number:
                asiento['fila'] = new_row
                asiento['numero'] = new_number
                save_state_file(filename, state)
                logging.info(f"Asiento actualizado en el archivo {filename}: {day, row, number} a {new_row, new_number}")
                return
        logging.error(f"Asiento no encontrado en el archivo {filename}: {day, row, number}")
    else:
        logging.error(f"No se pudo cargar el archivo {filename} para actualizar el asiento.")

def load_state_file(filename):
    """
    Carga el estado de la sala de cine desde un archivo JSON.
    
    Args:
        filename (str): El nombre del archivo JSON.
    
    Returns:
        dict: El estado de la sala de cine.
    """
    with open(filename, 'r') as file:
        state = json.load(file)
    logging.info(f"Estado cargado desde el archivo {filename}.")
    return state

def save_state_file(filename, state):
    """
    Guarda el estado de la sala de cine en un archivo JSON.
    
    Args:
        filename (str): El nombre del archivo JSON.
        state (dict): El estado de la sala de cine.
    """
    with open(filename, 'w') as file:
        json.dump(state, file, indent=4)
    logging.info(f"Estado guardado en el archivo {filename}.")