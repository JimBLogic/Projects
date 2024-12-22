import os
import logging
import sys
import json

# Asegurar que la ruta es correcta
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importar los módulos necesarios
from proyecto.utilidades import validate_input, save_state, reset_state
from proyecto.sala_cine import SalaCine
from proyecto.mensajes import Mensajes

# Asegurar que el archivo debug.log es escribible
log_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'debug.log'))
if not os.path.exists(log_file_path):
    open(log_file_path, 'w').close()
os.chmod(log_file_path, 0o666)

# Configurar el logger
logging.basicConfig(filename=log_file_path, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

MAX_ROWS = 6

def main_menu():
    while True:
        print(Mensajes.bienvenida())
        print("Seleccione una opción:")
        print("1. Gestionar asientos")
        print("2. Generar reporte de disponibilidad")
        print("3. Resetear estado")
        print("4. Salir")
        
        try:
            option = int(input("Seleccione una opción: "))
        except ValueError:
            print(Mensajes.opcion_invalida())
            continue
        
        if option == 1:
            manage_seats()
        elif option == 2:
            generate_report()
        elif option == 3:
            reset_state('estado_sala.json', {day: [] for day in ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]})
        elif option == 4:
            print(Mensajes.saliendo_sistema())
            break
        else:
            print(Mensajes.opcion_invalida())

def manage_seats():
    while True:
        print("\nSeleccione una opción de gestión de asientos:")
        print("1. Agregar asiento")
        print("2. Reservar asiento")
        print("3. Cancelar reserva")
        print("4. Mostrar asientos")
        print("5. Volver al menú principal")
        print("6. Actualizar información de asiento")
        
        try:
            option = int(input("Seleccione una opción: "))
        except ValueError:
            print(Mensajes.opcion_invalida())
            continue
        
        if option == 1:
            add_seat()
        elif option == 2:
            reserve_seat()
        elif option == 3:
            cancel_reservation()
        elif option == 4:
            show_seats()
        elif option == 5:
            break
        elif option == 6:
            update_seat_info()
        else:
            print(Mensajes.opcion_invalida())

def add_seat():
    try:
        day = select_day()
        row = select_row(day)
        number = select_seat(day, row)
        print(cinema.agregar_asiento(day, row, number))
        logging.info(f"Asiento agregado: {day}, {row}, {number}")
    except ValueError as e:
        print(e)
        logging.error(f"Error al agregar asiento: {e}")
    
    save_state('estado_sala.json', cinema.get_estado())

def reserve_seat():
    try:
        day = select_day()
        row = select_row(day)
        number = select_seat(day, row)
        age = validate_input(Mensajes.ingrese_edad(), int, range(1, 101))
        print(cinema.reservar_asiento(day, row, number, age))
        logging.info(f"Asiento reservado: {day}, {row}, {number}")
    except ValueError as e:
        print(e)
        logging.error(f"Error al reservar asiento: {e}")
    
    save_state('estado_sala.json', cinema.get_estado())

def cancel_reservation():
    try:
        day = select_day()
        row = select_row(day)
        number = select_seat(day, row)
        print(cinema.cancelar_reserva(day, row, number))
        logging.info(f"Reserva cancelada: {day}, {row}, {number}")
    except ValueError as e:
        print(e)
        logging.error(f"Error al cancelar reserva: {e}")
    
    save_state('estado_sala.json', cinema.get_estado())

def show_seats():
    try:
        day = select_day()
        if day in cinema.get_estado():
            for seat in cinema.get_estado()[day]:
                print(seat)
            logging.info(f"Asientos mostrados para el día: {day}")
        else:
            print(Mensajes.dia_invalido())
    except ValueError as e:
        print(e)
        logging.error(f"Error al mostrar asientos: {e}")

def update_seat_info():
    try:
        day = select_day()
        row = select_row(day)
        number = select_seat(day, row)
        new_row = validate_input(Mensajes.ingrese_nueva_fila(), str, [])
        new_number = validate_input(Mensajes.ingrese_nuevo_numero_asiento(), int, range(1, 11))
        print(cinema.actualizar_asiento(day, row, number, new_row, new_number))
        logging.info(f"Asiento actualizado: {day}, {row}, {number} a {new_row}, {new_number}")
    except ValueError as e:
        print(e)
        logging.error(f"Error al actualizar asiento: {e}")
    
    save_state('estado_sala.json', cinema.get_estado())

def generate_report():
    report = cinema.mostrar_asientos()
    for day, availability in report.items():
        libres = len([asiento for asiento in availability if not asiento['reservado']])
        reservados = len([asiento for asiento in availability if asiento['reservado']])
        no_agregados = MAX_ROWS * 10 - (libres + reservados)
        print(Mensajes.reporte_disponibilidad(day, libres, reservados, no_agregados))
    logging.info("Reporte de disponibilidad generado.")

def select_day():
    while True:
        try:
            day_num = validate_input(Mensajes.ingrese_dia(), int, range(1, 8))
            days = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
            return days[int(day_num) - 1]
        except ValueError:
            print(Mensajes.dia_invalido())

def select_row(day):
    while True:
        try:
            row = validate_input(Mensajes.ingrese_fila(), str, [])
            if row.upper() not in "ABCDEF":
                raise ValueError("Fila inválida. Debe ser una letra entre A y F.")
            if len(cinema.get_estado()[day]) >= MAX_ROWS:
                print("Número máximo de filas alcanzado. Seleccione otro día.")
                continue
            return row
        except ValueError as e:
            print(e)

def select_seat(day, row):
    while True:
        try:
            number = validate_input(Mensajes.ingrese_numero_asiento(), int, range(1, 11))
            if any(asiento.get_fila() == row and asiento.get_numero() == number for asiento in cinema.get_estado()[day]):
                print("El asiento ya existe en el sistema. Seleccione otro asiento.")
                continue
            return number
        except ValueError:
            print("Número de asiento inválido. Por favor, intente de nuevo.")

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

def main():
    """
    Función principal que gestiona la interacción con el usuario para la gestión de asientos en la sala de cine.
    """
    # Crear una instancia de la clase SalaCine para gestionar los asientos
    global cinema
    cinema = SalaCine()
    
    # Inicializar el estado si no existe
    if not os.path.exists('estado_sala.json'):
        reset_state('estado_sala.json', {day: [] for day in ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]})
    
    # Mostrar un mensaje de bienvenida al usuario
    print(Mensajes.bienvenida())
    logging.info("Mensaje de bienvenida mostrado.")

    main_menu()

if __name__ == "__main__":
    main()