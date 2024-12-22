import os
import json
import logging
from proyecto.sala_cine import SalaCine

# Configurar el logger
logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

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

def create_state_file(filename, initial_state):
    """
    Crea un archivo de estado con el estado inicial especificado.
    
    Args:
        filename (str): El nombre del archivo.
        initial_state (dict): El estado inicial a establecer.
    """
    with open(filename, 'w') as file:
        json.dump(initial_state, file, indent=4)
    logging.debug(f'Archivo de estado creado en {filename}.')

def delete_state_file(filename):
    """
    Elimina el archivo de estado especificado.
    
    Args:
        filename (str): El nombre del archivo.
    """
    try:
        os.remove(filename)
        logging.debug(f'Archivo de estado {filename} eliminado.')
    except FileNotFoundError:
        logging.error(f'Archivo {filename} no encontrado.')

def save_state_file(filename, state):
    """
    Guarda el estado en un archivo.
    
    Args:
        filename (str): El nombre del archivo.
        state (dict): El estado a guardar.
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

def update_state_file(filename, day, row, number, new_row, new_number):
    """
    Actualiza el estado de un asiento en el archivo de estado.
    
    Args:
        filename (str): El nombre del archivo.
        day (str): El día de la semana.
        row (str): La fila del asiento.
        number (int): El número del asiento.
        new_row (str): La nueva fila del asiento.
        new_number (int): El nuevo número del asiento.
    """
    state = load_state_file(filename)
    if state:
        for asiento in state['asientos']:
            if asiento['fila'] == row and asiento['numero'] == number:
                asiento['fila'] = new_row
                asiento['numero'] = new_number
                save_state_file(filename, state)
                logging.debug(f'Estado del asiento actualizado en {filename}.')
                return
        logging.error(f'Asiento {number} en fila {row} no encontrado en {filename}.')