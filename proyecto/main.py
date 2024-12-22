import os
import logging
import sys

# Asegurar que la ruta es correcta
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importar los módulos necesarios
from proyecto.utilidades import validate_input, validate_option, save_state, reset_state, calculate_final_price
from proyecto.sala_cine import SalaCine
from proyecto.mensajes import Mensajes

# Asegurar que el archivo debug.log es escribible
log_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'debug.log'))
if not os.path.exists(log_file_path):
    open(log_file_path, 'w').close()
os.chmod(log_file_path, 0o666)

# Configurar el logger
logging.basicConfig(filename=log_file_path, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

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
        day_num = validate_input(Mensajes.ingrese_dia(), int, range(1, 8))
        days = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        day = days[int(day_num) - 1]
        row = validate_input(Mensajes.ingrese_fila(), str, [])
        number = validate_input(Mensajes.ingrese_numero_asiento(), int, range(1, 11))
        print(cinema.agregar_asiento(day, row, number))
        logging.info(f"Asiento agregado: {day}, {row}, {number}")
    except ValueError as e:
        print(e)
        logging.error(f"Error al agregar asiento: {e}")

def reserve_seat():
    try:
        day_num = validate_input(Mensajes.ingrese_dia(), int, range(1, 8))
        days = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        day = days[int(day_num) - 1]
        row = validate_input(Mensajes.ingrese_fila(), str, [])
        number = validate_input(Mensajes.ingrese_numero_asiento(), int, range(1, 11))
        age = validate_input(Mensajes.ingrese_edad(), int, range(1, 101))
        print(cinema.reservar_asiento(day, row, number, age))
        logging.info(f"Asiento reservado: {day}, {row}, {number}")
    except ValueError as e:
        print(e)
        logging.error(f"Error al reservar asiento: {e}")

def cancel_reservation():
    try:
        day_num = validate_input(Mensajes.ingrese_dia(), int, range(1, 8))
        days = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        day = days[int(day_num) - 1]
        row = validate_input(Mensajes.ingrese_fila(), str, [])
        number = validate_input(Mensajes.ingrese_numero_asiento(), int, range(1, 11))
        print(cinema.cancelar_reserva(day, row, number))
        logging.info(f"Reserva cancelada: {day}, {row}, {number}")
    except ValueError as e:
        print(e)
        logging.error(f"Error al cancelar reserva: {e}")

def show_seats():
    try:
        day_num = validate_input(Mensajes.ingrese_dia(), int, range(1, 8))
        days = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        day = days[int(day_num) - 1]
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
        day_num = validate_input(Mensajes.ingrese_dia(), int, range(1, 8))
        days = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        day = days[int(day_num) - 1]
        row = validate_input(Mensajes.ingrese_fila(), str, [])
        number = validate_input(Mensajes.ingrese_numero_asiento(), int, range(1, 11))
        new_row = validate_input(Mensajes.ingrese_nueva_fila(), str, [])
        new_number = validate_input(Mensajes.ingrese_nuevo_numero_asiento(), int, range(1, 11))
        print(cinema.actualizar_asiento(day, row, number, new_row, new_number))
        logging.info(f"Asiento actualizado: {day}, {row}, {number} a {new_row}, {new_number}")
    except ValueError as e:
        print(e)
        logging.error(f"Error al actualizar asiento: {e}")

def generate_report():
    report = cinema.mostrar_asientos()
    for day, availability in report.items():
        libres = len([asiento for asiento in availability if not asiento['reservado']])
        reservados = len([asiento for asiento in availability if asiento['reservado']])
        no_agregados = 10 - (libres + reservados)
        print(Mensajes.reporte_disponibilidad(day, libres, reservados, no_agregados))
    logging.info("Reporte de disponibilidad generado.")

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