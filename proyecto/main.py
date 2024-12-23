import os
import sys
import logging

# Añadir el directorio 'proyecto' al PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utilidades import validate_input, save_state, reset_state, calculate_discount, calculate_final_price, load_state_file
from sala_cine import SalaCine
from mensajes import Mensajes

# Configurar el logger
logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s - %(nivelname)s - %(message)s')

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
    archivo_estado = os.path.abspath(os.path.join(os.path.dirname(__file__), 'estado_cine.json'))
    dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    salas = {dia: SalaCine(precio_base, archivo_estado) for dia in dias_semana}
    estado_guardado = False

    # Cargar el estado inicial desde el archivo
    estado_inicial = load_state_file(archivo_estado)
    for dia in dias_semana:
        salas[dia].cargar_estado()

    # Mostrar mensaje de bienvenida
    print(Mensajes.bienvenida())

    while True:
        print("\nOpciones:")
        print("1. Agregar asiento (Número: 1-10, Fila: A-J)")
        print("2. Reservar asiento (Número: 1-10, Fila: A-J)")
        print("3. Cancelar reserva (Número: 1-10, Fila: A-J)")
        print("4. Mostrar asientos")
        print("5. Resetear estado")
        print("6. Salir")

        opcion = validate_input("Seleccione una opción (1-6): ", int, range(1, 7))

        if opcion in [1, 2, 3]:
            dia = validate_input("Ingrese el día de la semana (1: lunes, 2: martes, 3: miércoles, 4: jueves, 5: viernes, 6: sábado, 7: domingo): ", int, range(1, 8))
            dia_nombre = dias_semana[dia - 1]
            sala = salas[dia_nombre]

        if opcion == 1:
            numero = validate_input("Ingrese el número del asiento (1-10): ", int, range(1, 11))
            fila = validate_input("Ingrese la fila del asiento (A-J): ", str, "ABCDEFGHIJ")
            try:
                sala.agregar_asiento(numero, fila)
                print(Mensajes.asiento_agregado())
                sala.guardar_estado()
                estado_guardado = True
            except ValueError as e:
                print(Mensajes.asiento_ya_existe())
                logging.error(e)

        elif opcion == 2:
            numero = validate_input("Ingrese el número del asiento (1-10): ", int, range(1, 11))
            fila = validate_input("Ingrese la fila del asiento (A-J): ", str, "ABCDEFGHIJ")
            edad = validate_input("Ingrese la edad del espectador: ", int, range(1, 101))
            try:
                sala.reservar_asiento(numero, fila, edad, dia_nombre)
                print(Mensajes.asiento_reservado())
                descuento = calculate_discount(precio_base, edad, dia_nombre)
                precio_final = calculate_final_price(precio_base, edad, dia_nombre)
                print(f"Precio base: {precio_base:.2f}€")
                if dia_nombre == "miércoles":
                    print("Descuento por día: 20%")
                if edad >= 65:
                    print("Descuento por edad: 30%")
                print(f"Precio final: {precio_final:.2f}€")
                sala.guardar_estado()
                estado_guardado = True
            except ValueError as e:
                print(Mensajes.asiento_no_encontrado())
                logging.error(e)
            except Exception as e:
                print(Mensajes.asiento_ya_reservado())
                logging.error(e)

        elif opcion == 3:
            numero = validate_input("Ingrese el número del asiento (1-10): ", int, range(1, 11))
            fila = validate_input("Ingrese la fila del asiento (A-J): ", str, "ABCDEFGHIJ")
            try:
                sala.cancelar_reserva(numero, fila)
                print(Mensajes.reserva_cancelada())
                sala.guardar_estado()
                estado_guardado = True
            except ValueError as e:
                print(Mensajes.asiento_no_encontrado())
                logging.error(e)
            except Exception as e:
                print(Mensajes.asiento_no_encontrado())
                logging.error(e)

        elif opcion == 4:
            for dia, sala in salas.items():
                print(f"\nAsientos para el día {dia.capitalize()}:")
                sala.mostrar_asientos()

        elif opcion == 5:
            confirmacion = input(Mensajes.confirmar_reseteo()).lower()
            if confirmacion == 'si':
                for sala in salas.values():
                    reset_state(archivo_estado, [])
                salas = {dia: SalaCine(precio_base, archivo_estado) for dia in dias_semana}
                print(Mensajes.estado_reseteado())
                estado_guardado = True
            else:
                print(Mensajes.reseteo_cancelado())

        elif opcion == 6:
            if not estado_guardado:
                confirmacion = input(Mensajes.confirmar_guardado()).lower()
                if confirmacion == 'si':
                    for sala in salas.values():
                        sala.guardar_estado()
                    print(Mensajes.estado_guardado())
            else:
                print(Mensajes.estado_guardado())
            print(Mensajes.saliendo_sistema())
            break

if __name__ == "__main__":
    main()