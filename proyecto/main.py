from utilidades import validar_entrada, validar_opcion
from sala_cine import SalaCine
from mensajes import Mensajes
import logging

# Configurar el logger
logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """
    Función principal que gestiona la interacción con el usuario para la gestión de asientos en la sala de cine.
    """
    # Crear una instancia de la clase SalaCine para gestionar los asientos
    sala = SalaCine()
    
    # Mostrar un mensaje de bienvenida al usuario
    print(Mensajes.bienvenida())
    logging.info("Mensaje de bienvenida mostrado.")

    # Bucle principal para la interacción con el usuario
    while True:
        # Mostrar el menú de opciones al usuario
        print("\nSeleccione una opción:")
        print("1. Agregar asiento")
        print("2. Reservar asiento")
        print("3. Cancelar reserva")
        print("4. Mostrar asientos")
        print("5. Generar reporte de disponibilidad")
        print("6. Resetear estado")
        print("7. Salir")

        # Validar la opción seleccionada por el usuario
        try:
            opcion = validar_entrada("Seleccione una opción (1-7): ", int, (1, 7))
        except ValueError as e:
            print(Mensajes.max_intentos())
            logging.error(e)
            break
        logging.info(f"Opción seleccionada: {opcion}")

        if opcion == 1:
            # Agregar un asiento
            dia_num = validar_entrada(Mensajes.ingrese_dia(), int, (1, 7))
            dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
            dia = dias[dia_num - 1]
            fila = input(Mensajes.ingrese_fila())
            numero = validar_entrada(Mensajes.ingrese_numero_asiento(), int)
            try:
                print(sala.agregar_asiento(dia, fila, numero))
                logging.info(f"Asiento agregado: {dia}, {fila}, {numero}")
            except ValueError as e:
                print(e)
                logging.error(f"Error al agregar asiento: {e}")
        elif opcion == 2:
            # Reservar un asiento
            dia_num = validar_entrada(Mensajes.ingrese_dia(), int, (1, 7))
            dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
            dia = dias[dia_num - 1]
            fila = input(Mensajes.ingrese_fila())
            numero = validar_entrada(Mensajes.ingrese_numero_asiento(), int)
            print(sala.reservar_asiento(dia, fila, numero))
            logging.info(f"Asiento reservado: {dia}, {fila}, {numero}")
        elif opcion == 3:
            # Cancelar una reserva
            dia_num = validar_entrada(Mensajes.ingrese_dia(), int, (1, 7))
            dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
            dia = dias[dia_num - 1]
            fila = input(Mensajes.ingrese_fila())
            numero = validar_entrada(Mensajes.ingrese_numero_asiento(), int)
            print(sala.cancelar_reserva(dia, fila, numero))
            logging.info(f"Reserva cancelada: {dia}, {fila}, {numero}")
        elif opcion == 4:
            # Mostrar los asientos de un día específico
            dia_num = validar_entrada(Mensajes.ingrese_dia(), int, (1, 7))
            dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
            dia = dias[dia_num - 1]
            if dia in sala.estado:
                for asiento in sala.estado[dia]:
                    print(asiento.to_dict())
                logging.info(f"Asientos mostrados para el día: {dia}")
            else:
                print(Mensajes.dia_invalido())
                logging.warning(f"Día inválido ingresado: {dia}")
        elif opcion == 5:
            # Generar un reporte de disponibilidad de asientos
            reporte = sala.reporte_disponibilidad()
            for dia, disponibilidad in reporte.items():
                print(Mensajes.reporte_disponibilidad(dia, disponibilidad["libres"], disponibilidad["reservados"], disponibilidad["no_agregados"]))
            logging.info("Reporte de disponibilidad generado.")
        elif opcion == 6:
            # Resetear el estado de la sala
            confirmacion = input(Mensajes.confirmar_reseteo()).lower()
            if confirmacion == 'si':
                sala.estado = {dia: [] for dia in ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]}
                sala.guardar_estado()
                print(Mensajes.estado_reseteado())
                logging.info("Estado de la sala reseteado.")
            else:
                print(Mensajes.reseteo_cancelado())
                logging.info("Reseteo de estado cancelado.")
        elif opcion == 7:
            # Salir del sistema
            guardar = input(Mensajes.confirmar_guardado()).lower()
            if guardar == 'si':
                sala.guardar_estado()
                print(Mensajes.estado_guardado())
                logging.info("Estado de la sala guardado.")
            print(Mensajes.saliendo_sistema())
            logging.info("Sistema cerrado por el usuario.")
            break

if __name__ == "__main__":
    main()