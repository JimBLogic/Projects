from sala_cine import SalaCine, guardar_estado, cargar_estado, reset_estado
from utilidades import validar_entrada, validar_opcion, agregar_asientos_en_rango, reporte_disponibilidad
from mensajes import mostrar_menu, solicitar_datos_asiento, solicitar_datos_reserva, mostrar_mensaje, mostrar_error

def main():
    """
    Función principal que maneja la interacción con el usuario.
    Carga el estado de la sala de cine y presenta un menú de opciones para gestionar los asientos.
    """
    sala = cargar_estado()
    print("¡Bienvenido al Sistema de Reservas para un Cine!")
    print("Las filas van del 1 al 10 y los asientos de cada fila van del 1 al 20.")
    print("Recuerda que los miércoles hay un 20% de descuento y los mayores de 65 años tienen un 30% de descuento adicional.")

    dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

    while True:
        mostrar_menu()
        opcion = validar_entrada("Seleccione una opción (1-7): ", int, (1, 7))

        try:
            if opcion == 1:
                dia = validar_entrada("Seleccione el día de la semana (1. Lunes, 2. Martes, 3. Miércoles, 4. Jueves, 5. Viernes, 6. Sábado, 7. Domingo): ", int, (1, 7))
                dia_semana = dias_semana[dia - 1]

                fila = validar_entrada("Seleccione la fila (1-10): ", int, (1, 10))
                numero = validar_entrada("Seleccione el número del asiento (1-20): ", int, (1, 20))
                try:
                    sala.agregar_asiento(numero, fila, dia_semana)
                    mostrar_mensaje("Asiento agregado correctamente.")
                except Exception as e:
                    mostrar_error(e)

            elif opcion == 2:
                dia = validar_entrada("Seleccione el día de la semana (1. Lunes, 2. Martes, 3. Miércoles, 4. Jueves, 5. Viernes, 6. Sábado, 7. Domingo): ", int, (1, 7))
                dia_semana = dias_semana[dia - 1]

                fila = validar_entrada("Seleccione la fila (1-10): ", int, (1, 10))
                numero = validar_entrada("Seleccione el número del asiento (1-20): ", int, (1, 20))
                edad = validar_entrada("Ingrese la edad del cliente (1-120): ", int, (1, 120))
                try:
                    sala.reservar_asiento(numero, fila, dia_semana, edad)
                    mostrar_mensaje("Asiento reservado correctamente.")
                except Exception as e:
                    mostrar_error(e)

            elif opcion == 3:
                dia = validar_entrada("Seleccione el día de la semana (1. Lunes, 2. Martes, 3. Miércoles, 4. Jueves, 5. Viernes, 6. Sábado, 7. Domingo): ", int, (1, 7))
                dia_semana = dias_semana[dia - 1]

                fila = validar_entrada("Seleccione la fila (1-10): ", int, (1, 10))
                numero = validar_entrada("Seleccione el número del asiento (1-20): ", int, (1, 20))
                try:
                    sala.cancelar_reserva(numero, fila, dia_semana, "si")
                    mostrar_mensaje("Reserva cancelada correctamente.")
                except Exception as e:
                    mostrar_error(e)

            elif opcion == 4:
                while True:
                    dia = validar_entrada("Seleccione el día de la semana para mostrar asientos (1. Lunes, 2. Martes, 3. Miércoles, 4. Jueves, 5. Viernes, 6. Sábado, 7. Domingo, 8. Volver al menú): ", int, (1, 8))
                    if dia == 8:
                        break
                    dia_semana = dias_semana[dia - 1]
                    sala.mostrar_asientos(dia_semana)

            elif opcion == 5:
                reporte_disponibilidad(sala)

            elif opcion == 6:
                reset_estado()
                sala = SalaCine()
                mostrar_mensaje("Estado reseteado correctamente. Todos los asientos han sido eliminados.")

            elif opcion == 7:
                mostrar_mensaje("Saliendo del sistema...")
                guardar = validar_opcion("¿Desea guardar el estado antes de salir? (si/no): ", ["si", "no"])
                if guardar == "si":
                    guardar_estado(sala)
                    mostrar_mensaje("Estado guardado correctamente.")
                break

            else:
                mostrar_error("Opción no válida. Por favor, intente de nuevo.")

        except ValueError as e:
            mostrar_error(f"Error: {e}")

        except Exception as e:
            mostrar_error(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()