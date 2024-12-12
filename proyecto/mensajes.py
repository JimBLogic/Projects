class Mensajes:
    """
    Clase para centralizar los mensajes al usuario.
    """

    @staticmethod
    def asiento_agregado(numero, fila, dia_semana):
        return f"Asiento {numero} en fila {fila} para el día {dia_semana} agregado correctamente."

    @staticmethod
    def error_asiento_no_encontrado(numero, fila, dia_semana):
        return f"Error: Asiento {numero} en fila {fila} para el día {dia_semana} no encontrado."

    @staticmethod
    def descuentos_aplicados(descuentos):
        return f"Descuentos aplicados: {', '.join(descuentos)}"

    @staticmethod
    def precio_final(precio):
        return f"Precio final: €{precio:.2f}"

    @staticmethod
    def estado_guardado():
        return "Estado de la sala guardado correctamente."

    @staticmethod
    def estado_no_encontrado():
        return "No se encontró un estado previo de la sala. Iniciando una nueva sala."

    @staticmethod
    def estado_cargado():
        return "Estado de la sala cargado correctamente."

    @staticmethod
    def estado_error_carga(error):
        return f"Error al cargar el estado de la sala: {error}"

    @staticmethod
    def estado_reseteado():
        return "Estado de la sala reseteado correctamente. Todos los asientos han sido eliminados."

def mostrar_menu():
    """
    Muestra el menú principal de opciones al usuario.
    """
    print("\nOpciones:")
    print("1. Agregar asiento")
    print("2. Reservar asiento")
    print("3. Cancelar reserva")
    print("4. Mostrar todos los asientos")
    print("5. Generar reporte de disponibilidad")
    print("6. Resetear estado")
    print("7. Salir")

def solicitar_datos_asiento():
    """
    Solicita al usuario los datos de un asiento (número y fila).

    Returns:
        tuple: Una tupla con el número y la fila del asiento.
    """
    try:
        numero = int(input("Ingrese el número del asiento (1-20): "))
        fila = int(input("Ingrese la fila del asiento (1-10): "))
        return numero, fila
    except ValueError:
        mostrar_error("Entrada inválida. Por favor, ingrese números válidos.")
        return solicitar_datos_asiento()

def solicitar_datos_reserva():
    """
    Solicita al usuario los datos para reservar un asiento (número, fila, edad y día).

    Returns:
        tuple: Una tupla con el número, la fila, la edad del cliente y el día de la semana.
    """
    try:
        numero = int(input("Ingrese el número del asiento (1-20): "))
        fila = int(input("Ingrese la fila del asiento (1-10): "))
        edad = int(input("Ingrese la edad del cliente (1-120): "))
        dia = int(input("Ingrese el día de la semana (1-7): "))
        return numero, fila, edad, dia
    except ValueError:
        mostrar_error("Entrada inválida. Por favor, ingrese números válidos.")
        return solicitar_datos_reserva()

def mostrar_mensaje(mensaje):
    """
    Muestra un mensaje al usuario.

    Args:
        mensaje (str): El mensaje a mostrar.
    """
    print(mensaje)

def mostrar_error(error):
    """
    Muestra un mensaje de error al usuario.

    Args:
        error (str): El mensaje de error a mostrar.
    """
    print(f"Error: {error}")