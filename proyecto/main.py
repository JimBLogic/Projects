import os
import logging
from proyecto.utilidades import validate_input, save_state, reset_state
from proyecto.sala_cine import SalaCine
from proyecto.mensajes import Mensajes

# Configurar el logger
logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Asegurar que el archivo debug.log es escribible
log_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'debug.log'))
if not os.path.exists(log_file_path):
    with open(log_file_path, 'w') as file:
        pass

def main():
    """
    Función principal para gestionar la sala de cine.
    """
    precio_base = 10.0  # Precio base de una entrada
    sala = SalaCine(precio_base)

    # Agregar algunos asientos
    sala.agregar_asiento(1, "A")
    sala.agregar_asiento(2, "A")
    sala.agregar_asiento(3, "B")

    # Reservar un asiento
    try:
        sala.reservar_asiento(1, "A", 70, "miércoles")  # Asiento con descuento para mayor y día de espectador
    except Exception as e:
        logging.error(e)
        print(e)

    # Mostrar todos los asientos
    sala.mostrar_asientos()

    # Cancelar una reserva
    try:
        sala.cancelar_reserva(1, "A")
    except Exception as e:
        logging.error(e)
        print(e)

    # Mostrar todos los asientos después de cancelar
    sala.mostrar_asientos()

if __name__ == "__main__":
    main()