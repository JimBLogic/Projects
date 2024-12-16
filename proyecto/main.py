from proyecto.utilidades import validate_input, validate_option, save_state, reset_state
from proyecto.sala_cine import SalaCine
from proyecto.mensajes import Mensajes
import logging

# Configurar el logger
logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_input(prompt, input_type, valid_range):
    while True:
        try:
            user_input = input_type(input(prompt))
            if user_input not in range(valid_range[0], valid_range[1] + 1):
                raise ValueError
            return user_input
        except ValueError:
            print(f"Entrada inválida: El valor debe estar entre {valid_range[0]} y {valid_range[1]}. Ejemplo: {valid_range[0]}")

def main():
    """
    Función principal que gestiona la interacción con el usuario para la gestión de asientos en la sala de cine.
    """
    # Crear una instancia de la clase SalaCine para gestionar los asientos
    cinema = SalaCine()
    
    # Mostrar un mensaje de bienvenida al usuario
    print(Mensajes.bienvenida())
    logging.info("Mensaje de bienvenida mostrado.")

    # Bucle principal para la interacción con el usuario
    while True:
        # Mostrar el menú de opciones al usuario
        print("\nSeleccione una opción:")
        print("1. Gestionar asientos")
        print("2. Generar reporte de disponibilidad")
        print("3. Resetear estado")
        print("4. Salir")

        # Validar la opción seleccionada por el usuario
        try:
            option = validate_input("Seleccione una opción (1-4): ", int, (1, 4))
        except ValueError as e:
            print(Mensajes.max_intentos())
            logging.error(e)
            continue
        logging.info(f"Opción seleccionada: {option}")

        if option == 1:
            # Submenú para gestionar asientos
            while True:
                print("\nSeleccione una opción de gestión de asientos:")
                print("1. Agregar asiento")
                print("2. Reservar asiento")
                print("3. Cancelar reserva")
                print("4. Mostrar asientos")
                print("5. Volver al menú principal")
                print("6. Actualizar información de asiento")

                try:
                    sub_option = validate_input("Seleccione una opción (1-6): ", int, (1, 6))
                except ValueError as e:
                    print(Mensajes.max_intentos())
                    logging.error(e)
                    continue
                logging.info(f"Sub-opción seleccionada: {sub_option}")

                if sub_option == 1:
                    # Agregar un asiento
                    try:
                        day_num = validate_input(Mensajes.ingrese_dia(), int, (1, 7))
                        days = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
                        day = days[day_num - 1]
                        row = validate_input(Mensajes.ingrese_fila(), int, (1, 10))
                        number = validate_input(Mensajes.ingrese_numero_asiento(), int, (1, 10))
                        print(cinema.add_seat(day, row, number))
                        logging.info(f"Asiento agregado: {day}, {row}, {number}")
                    except ValueError as e:
                        print(e)
                        logging.error(f"Error al agregar asiento: {e}")
                        continue
                elif sub_option == 2:
                    # Reservar un asiento
                    try:
                        day_num = validate_input(Mensajes.ingrese_dia(), int, (1, 7))
                        days = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
                        day = days[day_num - 1]
                        row = validate_input(Mensajes.ingrese_fila(), int, (1, 10))
                        number = validate_input(Mensajes.ingrese_numero_asiento(), int, (1, 10))
                        age = validate_input(Mensajes.ingrese_edad(), int, valid_range=range(1, 11))
                        print(cinema.reserve_seat(day, row, number, age))
                        logging.info(f"Asiento reservado: {day}, {row}, {number}")
                    except ValueError as e:
                        print(e)
                        logging.error(f"Error al reservar asiento: {e}")
                        continue
                elif sub_option == 3:
                    # Cancelar una reserva
                    try:
                        day_num = validate_input(Mensajes.ingrese_dia(), int, (1, 7))
                        days = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
                        day = days[day_num - 1]
                        row = validate_input(Mensajes.ingrese_fila(), int, (1, 10))
                        number = validate_input(Mensajes.ingrese_numero_asiento(), int, (1, 10))
                        print(cinema.cancel_reservation(day, row, number))
                        logging.info(f"Reserva cancelada: {day}, {row}, {number}")
                    except ValueError as e:
                        print(e)
                        logging.error(f"Error al cancelar reserva: {e}")
                        continue
                elif sub_option == 4:
                    # Mostrar los asientos de un día específico
                    try:
                        day_num = validate_input(Mensajes.ingrese_dia(), int, (1, 7))
                        days = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
                        day = days[day_num - 1]
                        if day in cinema.get_state():
                            for seat in cinema.get_state()[day]:
                                print(seat.to_dict())
                            logging.info(f"Asientos mostrados para el día: {day}")
                        else:
                            print(Mensajes.dia_invalido())
                            logging.warning(f"Día inválido ingresado: {day}")
                    except ValueError as e:
                        print(e)
                        logging.error(f"Error al mostrar asientos: {e}")
                        continue
                elif sub_option == 5:
                    # Volver al menú principal
                    break
                elif sub_option == 6:
                    # Actualizar información de un asiento
                    try:
                        day_num = validate_input(Mensajes.ingrese_dia(), int, (1, 7))
                        days = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
                        day = days[day_num - 1]
                        row = validate_input(Mensajes.ingrese_fila(), int, (1, 10))
                        number = validate_input(Mensajes.ingrese_numero_asiento(), int, (1, 10))
                        new_row = validate_input(Mensajes.ingrese_nueva_fila(), int, (1, 10))
                        new_number = validate_input(Mensajes.ingrese_nuevo_numero_asiento(), int, (1, 10))
                        print(cinema.update_seat(day, row, number, new_row, new_number))
                        logging.info(f"Asiento actualizado: {day}, {row}, {number} a {new_row}, {new_number}")
                    except ValueError as e:
                        print(e)
                        logging.error(f"Error al actualizar asiento: {e}")
                        continue

        elif option == 2:
            # Generar un reporte de disponibilidad de asientos
            report = cinema.availability_report()
            for day, availability in report.items():
                print(Mensajes.availability_report(day, availability["libres"], availability["reservados"], availability["no_agregados"]))
            logging.info("Reporte de disponibilidad generado.")
        elif option == 3:
            # Resetear el estado de la sala
            confirmation = input(Mensajes.confirmar_reseteo()).lower()
            if confirmation == 'si':
                initial_state = {day: [] for day in ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]}
                reset_state('state_hall.json', initial_state)
                cinema.set_state(initial_state)
                print(Mensajes.estado_reseteado())
                logging.info("Estado de la sala reseteado.")
            else:
                print(Mensajes.reseteo_cancelado())
                logging.info("Reseteo de estado cancelado.")
        elif option == 4:
            # Salir del sistema
            save = input(Mensajes.confirmar_guardado()).lower()
            if save == 'si':
                save_state('state_hall.json', cinema.get_state())
                print(Mensajes.estado_guardado())
                logging.info("Estado de la sala guardado.")
            print(Mensajes.saliendo_sistema())
            logging.info("Sistema cerrado por el usuario.")
            break

if __name__ == "__main__":
    main()