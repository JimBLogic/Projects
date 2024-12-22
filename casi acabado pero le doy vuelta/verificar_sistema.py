import json
import logging
import os

# Importar el módulo SalaCine
from proyecto.sala_cine import SalaCine

def load_state_file(filename):
    """
    Carga el estado de la sala de cine desde un archivo JSON.
    
    Args:
        filename (str): El nombre del archivo JSON.
    
    Returns:
        dict: El estado de la sala de cine.
    """
    try:
        with open(filename, 'r') as file:
            state = json.load(file)
        logging.info(f"Archivo {filename} cargado correctamente.")
        return state
    except FileNotFoundError:
        logging.error(f"Archivo {filename} no encontrado.")
        return None
    except json.JSONDecodeError:
        logging.error(f"Error al decodificar el archivo {filename}.")
        return None

def create_state_file(filename, initial_state):
    """
    Crea un archivo JSON con el estado inicial de la sala de cine.
    
    Args:
        filename (str): El nombre del archivo JSON.
        initial_state (dict): El estado inicial de la sala de cine.
    """
    with open(filename, 'w') as file:
        json.dump(initial_state, file, indent=4)
    logging.info(f"Archivo {filename} creado con el estado inicial.")

def delete_state_file(filename):
    """
    Elimina el archivo JSON que contiene el estado de la sala de cine.
    
    Args:
        filename (str): El nombre del archivo JSON.
    """
    if os.path.exists(filename):
        os.remove(filename)
        logging.info(f"Archivo {filename} eliminado.")
    else:
        logging.error(f"Archivo {filename} no encontrado para eliminar.")

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

def update_state_file(filename, day, row, number, new_row, new_number):
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
