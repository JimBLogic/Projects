class Mensajes:
    """
    Clase que centraliza todos los mensajes al usuario.
    """
    
    @staticmethod
    def bienvenida():
        """
        Mensaje de bienvenida al sistema.
        
        Returns:
            str: El mensaje de bienvenida.
        """
        return "Bienvenido al sistema de gestión de asientos del cine."

    @staticmethod
    def opcion_invalida():
        """
        Mensaje de opción inválida.
        
        Returns:
            str: El mensaje de opción inválida.
        """
        return "Opción inválida. Por favor, intente de nuevo."

    @staticmethod
    def asiento_agregado():
        """
        Mensaje de asiento agregado correctamente.
        
        Returns:
            str: El mensaje de asiento agregado.
        """
        return "Asiento agregado correctamente."

    @staticmethod
    def asiento_reservado():
        """
        Mensaje de asiento reservado correctamente.
        
        Returns:
            str: El mensaje de asiento reservado.
        """
        return "Asiento reservado correctamente."

    @staticmethod
    def reserva_cancelada():
        """
        Mensaje de reserva cancelada correctamente.
        
        Returns:
            str: El mensaje de reserva cancelada.
        """
        return "Reserva cancelada correctamente."

    @staticmethod
    def reporte_disponibilidad(dia, libres, reservados, no_agregados):
        """
        Mensaje de reporte de disponibilidad de asientos.
        
        Args:
            dia (str): El día de la semana.
            libres (int): La cantidad de asientos libres.
            reservados (int): La cantidad de asientos reservados.
            no_agregados (int): La cantidad de asientos no agregados.
        
        Returns:
            str: El mensaje de reporte de disponibilidad.
        """
        return f"{dia.capitalize()}: {libres} asientos libres, {reservados} asientos reservados, {no_agregados} asientos no agregados."

    @staticmethod
    def max_intentos():
        """
        Mensaje de número máximo de intentos alcanzado.
        
        Returns:
            str: El mensaje de número máximo de intentos alcanzado.
        """
        return "Número máximo de intentos alcanzado. Por favor, intente de nuevo más tarde."

    @staticmethod
    def confirmar_reseteo():
        """
        Mensaje de confirmación de reseteo de estado.
        
        Returns:
            str: El mensaje de confirmación de reseteo.
        """
        return "¿Está seguro de que desea resetear el estado? Esto borrará todos los datos. (si/no):"

    @staticmethod
    def reseteo_cancelado():
        """
        Mensaje de reseteo cancelado.
        
        Returns:
            str: El mensaje de reseteo cancelado.
        """
        return "Reseteo de estado cancelado."

    @staticmethod
    def confirmar_guardado():
        """
        Mensaje de confirmación de guardado de estado.
        
        Returns:
            str: El mensaje de confirmación de guardado.
        """
        return "¿Desea guardar el estado actual antes de salir? (si/no):"

    @staticmethod
    def estado_guardado():
        """
        Mensaje de estado guardado correctamente.
        
        Returns:
            str: El mensaje de estado guardado.
        """
        return "Estado guardado correctamente."

    @staticmethod
    def estado_reseteado():
        """
        Mensaje de estado reseteado correctamente.
        
        Returns:
            str: El mensaje de estado reseteado.
        """
        return "Estado reseteado correctamente."

    @staticmethod
    def saliendo_sistema():
        """
        Mensaje de salida del sistema.
        
        Returns:
            str: El mensaje de salida del sistema.
        """
        return "Saliendo del sistema..."

    @staticmethod
    def ingrese_dia():
        """
        Mensaje para ingresar el día.
        
        Returns:
            str: El mensaje para ingresar el día.
        """
        return "Ingrese el día (1: lunes, 2: martes, 3: miércoles, 4: jueves, 5: viernes, 6: sábado, 7: domingo): "

    @staticmethod
    def ingrese_fila():
        """
        Mensaje para ingresar la fila.
        
        Returns:
            str: El mensaje para ingresar la fila.
        """
        return "Ingrese la fila: "

    @staticmethod
    def ingrese_numero_asiento():
        """
        Mensaje para ingresar el número de asiento.
        
        Returns:
            str: El mensaje para ingresar el número de asiento.
        """
        return "Ingrese el número de asiento: "

    @staticmethod
    def dia_invalido():
        """
        Mensaje de día inválido.
        
        Returns:
            str: El mensaje de día inválido.
        """
        return "Día inválido. Por favor, intente de nuevo."

    @staticmethod
    def asiento_no_encontrado():
        """
        Mensaje de asiento no encontrado.
        
        Returns:
            str: El mensaje de asiento no encontrado.
        """
        return "El asiento no se encuentra en el sistema."

    @staticmethod
    def asiento_ya_reservado():
        """
        Mensaje de asiento ya reservado.
        
        Returns:
            str: El mensaje de asiento ya reservado.
        """
        return "El asiento ya está reservado."

    @staticmethod
    def asiento_ya_existe():
        """
        Mensaje de asiento ya existente.
        
        Returns:
            str: El mensaje de asiento ya existente.
        """
        return "El asiento ya existe en el sistema."