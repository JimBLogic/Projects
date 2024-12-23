import os
import json
import logging
from proyecto.utilidades import load_state_file, save_state_file

# Configurar el logger
logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def create_state_file(filename, initial_state):
    """
    Crea un archivo de estado con un estado inicial.
    
    Args:
        filename (str): El nombre del archivo.
        initial_state (list): El estado inicial.
    """
    with open(filename, 'w') as file:
        json.dump(initial_state, file, indent=4)
    logging.debug(f'Archivo de estado creado en {filename}.')

def delete_state_file(filename):
    """
    Elimina un archivo de estado.
    
    Args:
        filename (str): El nombre del archivo.
    """
    try:
        os.remove(filename)
        logging.debug(f'Archivo de estado {filename} eliminado.')
    except FileNotFoundError:
        logging.error(f'Archivo {filename} no encontrado.')

def reset_state_file(filename, initial_state):
    """
    Restablece el estado inicial en un archivo.
    
    Args:
        filename (str): El nombre del archivo.
        initial_state (list): El estado inicial a establecer.
    """
    save_state_file(filename, initial_state)
    logging.debug(f'Estado restablecido en {filename}.')