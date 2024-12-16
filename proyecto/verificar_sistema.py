import json
import logging
import os

# Limitar el número de filas y asientos para gestionar mejor la sala de cine y evitar asientos infinitos o duplicados.

def load_state_file(file):
    """
    Carga el estado desde un archivo JSON.
    
    Args:
        file (str): El nombre del archivo.
    
    Returns:
        dict: El estado cargado desde el archivo.
    """
    try:
        with open(file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.warning(f"Archivo {file} no encontrado.")
        return {}
    except json.JSONDecodeError:
        logging.error(f"Error al decodificar el archivo {file}.")
        return {}

def create_state_file(file, initial_state):
    """
    Crea un archivo JSON con el estado inicial.
    
    Args:
        file (str): El nombre del archivo.
        initial_state (dict): El estado inicial a guardar.
    """
    with open(file, 'w') as f:
        json.dump(initial_state, f, indent=4)
    logging.info(f"Archivo {file} creado con el estado inicial.")

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

def delete_state_file(file):
    """
    Elimina el archivo de estado JSON.
    
    Args:
        file (str): El nombre del archivo.
    """
    try:
        os.remove(file)
        logging.info(f"Archivo {file} eliminado.")
    except FileNotFoundError:
        logging.warning(f"Archivo {file} no encontrado.")
    except Exception as e:
        logging.error(f"Error al eliminar el archivo {file}: {e}")

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

def cargar_archivo_estado():
    """
    Carga el estado de la sala de cine desde el archivo.
    """
    from sala_cine import SalaCine
    sala_cine = SalaCine()
    return sala_cine.get_estado()

def crear_archivo_estado():
    """
    Crea un archivo de estado inicial para la sala de cine.
    """
    from sala_cine import SalaCine
    sala_cine = SalaCine()
    sala_cine.guardar_estado()
    return sala_cine.get_estado()
