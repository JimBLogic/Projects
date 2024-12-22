import json
import logging
import os
import sys

# Asegurar que la ruta es correcta
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importar el módulo SalaCine
from proyecto.sala_cine import SalaCine
from proyecto.utilidades import save_state_file, reset_state_file

MAX_ROWS = 10
MAX_SEATS_PER_ROW = 10

def load_state_file(filename):
    """
    Carga el estado desde un archivo JSON.
    
    Args:
        filename (str): El nombre del archivo.
    
    Returns:
        dict: El estado cargado.
    """
    if not os.path.exists(filename):
        logging.warning(f"Archivo {filename} no encontrado.")
        return {}
    try:
        with open(filename, 'r') as f:
            state = json.load(f)
        logging.info(f"Archivo {filename} cargado correctamente.")
        return state
    except Exception as e:
        logging.error(f"Error al cargar el archivo {filename}: {e}")
        return {}

def create_state_file(filename, state):
    """
    Crea un archivo de estado JSON con el estado inicial.
    
    Args:
        filename (str): El nombre del archivo.
        state (dict): El estado inicial a guardar.
    """
    try:
        with open(filename, 'w') as f:
            json.dump(state, f, indent=4)
        logging.info(f"Archivo {filename} creado con el estado inicial.")
    except Exception as e:
        logging.error(f"Error al crear el archivo {filename}: {e}")

def delete_state_file(filename):
    """
    Elimina el archivo de estado JSON.
    
    Args:
        filename (str): El nombre del archivo.
    """
    try:
        if os.path.exists(filename):
            os.remove(filename)
            logging.info(f"Archivo {filename} eliminado.")
        else:
            logging.warning(f"Archivo {filename} no encontrado.")
    except Exception as e:
        logging.error(f"Error al eliminar el archivo {filename}: {e}")

def load_cinema_state():
    """
    Carga el estado de la sala de cine desde el archivo.
    """
    cinema = SalaCine()
    state = load_state_file('estado_sala.json')
    cinema.set_state(state)
    return cinema.get_state()

def create_cinema_state():
    """
    Crea un archivo de estado inicial para la sala de cine.
    """
    cinema = SalaCine()
    initial_state = cinema.get_state()
    create_state_file('estado_sala.json', initial_state)
    return initial_state

def add_seat(cinema, day, row, number):
    """
    Agrega un asiento a la sala de cine si no excede los límites.
    
    Args:
        cinema (SalaCine): La instancia de la sala de cine.
        day (str): El día de la semana.
        row (str): La fila del asiento.
        number (int): El número del asiento.
    
    Returns:
        str: Un mensaje indicando si el asiento fue agregado correctamente o si excede los límites.
    """
    if len(cinema.get_estado()[day]) >= MAX_ROWS:
        return "Número máximo de filas alcanzado."
    if any(asiento.get_fila() == row and asiento.get_numero() == number for asiento in cinema.get_estado()[day]):
        return "El asiento ya existe en el sistema."
    return cinema.agregar_asiento(day, row, number)
