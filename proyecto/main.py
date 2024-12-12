from sala_cine import SalaCine, guardar_estado, cargar_estado, reset_estado
from utilidades import validar_entrada, validar_opcion, agregar_asientos_en_rango, simulador_precios, reporte_disponibilidad
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
        opcion = validar_entrada("Seleccione una opción (1-8): ", int, (1, 8))

        try:
            if opcion == 1:
                numero, fila = solicitar_datos_asiento()
                dia = validar_entrada("Seleccione el día de la semana (1-7): ", int, (1, 7))
                dia_semana = dias_semana[dia - 1]
                try:
                    sala.agregar_asiento(numero, fila, dia_semana)
                    mostrar_mensaje("Asiento agregado correctamente.")
                except Exception as e:
                    mostrar_error(e)

            elif opcion == 2:
                numero, fila, edad, dia = solicitar_datos_reserva()
                dia_semana = dias_semana[dia - 1]
                try:
                    sala.reservar_asiento(numero, fila, dia_semana, edad)
                    mostrar_mensaje("Asiento reservado correctamente.")
                except Exception as e:
                    mostrar_error(e)

            elif opcion == 3:
                numero, fila = solicitar_datos_asiento()
                dia = validar_entrada("Seleccione el día de la semana (1-7): ", int, (1, 7))
                dia_semana = dias_semana[dia - 1]
                try:
                    sala.cancelar_reserva(numero, fila, dia_semana, "si")
                    mostrar_mensaje("Reserva cancelada correctamente.")
                except Exception as e:
                    mostrar_error(e)

            elif opcion == 4:
                sala.mostrar_asientos()

            elif opcion == 5:
                mostrar_mensaje("Saliendo del sistema...")
                guardar_estado(sala)
                break

            elif opcion == 6:
                precio_base = 10.0
                dia = validar_entrada("Seleccione el día de la semana (1-7): ", int, (1, 7))
                dia_semana = dias_semana[dia - 1]
                edad = validar_entrada("Ingrese la edad del cliente (1-120): ", int, (1, 120))
                precio_final, descuentos_aplicados = simulador_precios(precio_base, dia_semana, edad)
                mostrar_mensaje(f"Precio final: €{precio_final:.2f}")
                if descuentos_aplicados:
                    mostrar_mensaje(f"Descuentos aplicados: {', '.join(descuentos_aplicados)}")

            elif opcion == 7:
                reporte_disponibilidad(sala)

            elif opcion == 8:
                reset_estado()
                sala = SalaCine()
                mostrar_mensaje("Estado reseteado correctamente.")

            else:
                mostrar_error("Opción no válida. Por favor, intente de nuevo.")

        except ValueError as e:
            mostrar_error(f"Error: {e}")

        except Exception as e:
            mostrar_error(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()