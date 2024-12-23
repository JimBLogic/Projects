class Mensajes:
    """
    Clase que centraliza todos los mensajes al usuario.
    """
    
    @staticmethod
    def mostrar_bienvenida():
        """
        Muestra el mensaje de bienvenida.
        """
        print("Bienvenido al sistema de reservas de la sala de cine.")

    @staticmethod
    def mostrar_despedida():
        """
        Muestra el mensaje de despedida.
        """
        print("Gracias por usar el sistema de reservas de la sala de cine.")

    @staticmethod
    def mostrar_error(mensaje):
        """
        Muestra un mensaje de error.
        
        Args:
            mensaje (str): El mensaje de error a mostrar.
        """
        print(f"Error: {mensaje}")

    @staticmethod
    def mostrar_exito(mensaje):
        """
        Muestra un mensaje de éxito.
        
        Args:
            mensaje (str): El mensaje de éxito a mostrar.
        """
        print(f"Éxito: {mensaje}")

    @staticmethod
    def mostrar_asientos(asientos):
        """
        Muestra la lista de asientos.
        
        Args:
            asientos (list): La lista de asientos a mostrar.
        """
        for asiento in asientos:
            print(asiento)

    @staticmethod
    def solicitar_numero_asiento():
        """
        Solicita al usuario el número del asiento.
        
        Returns:
            int: El número del asiento ingresado por el usuario.
        """
        return int(input("Ingrese el número del asiento (1-10): "))

    @staticmethod
    def solicitar_fila_asiento():
        """
        Solicita al usuario la fila del asiento.
        
        Returns:
            str: La fila del asiento ingresada por el usuario.
        """
        return input("Ingrese la fila del asiento (A-J): ")

    @staticmethod
    def solicitar_edad():
        """
        Solicita al usuario la edad.
        
        Returns:
            int: La edad ingresada por el usuario.
        """
        return int(input("Ingrese su edad: "))

    @staticmethod
    def solicitar_dia():
        """
        Solicita al usuario el día de la semana.
        
        Returns:
            str: El día de la semana ingresado por el usuario.
        """
        return input("Ingrese el día de la semana (1: lunes, 2: martes, 3: miércoles, 4: jueves, 5: viernes, 6: sábado, 7: domingo): ")

    @staticmethod
    def mostrar_precio_final(precio):
        """
        Muestra el precio final de la reserva.
        
        Args:
            precio (float): El precio final a mostrar.
        """
        print(f"El precio final de la reserva es: {precio:.2f}€")

    @staticmethod
    def asiento_actualizado():
        """
        Devuelve el mensaje de asiento actualizado.
        
        Returns:
            str: El mensaje de asiento actualizado.
        """
        return "Asiento actualizado correctamente."

    @staticmethod
    def asiento_agregado():
        """
        Devuelve el mensaje de asiento agregado.
        
        Returns:
            str: El mensaje de asiento agregado.
        """
        return "Asiento agregado correctamente."

    @staticmethod
    def asiento_eliminado():
        """
        Devuelve el mensaje de asiento eliminado.
        
        Returns:
            str: El mensaje de asiento eliminado.
        """
        return "Asiento eliminado correctamente."

    @staticmethod
    def asiento_no_encontrado():
        """
        Devuelve el mensaje de asiento no encontrado.
        
        Returns:
            str: El mensaje de asiento no encontrado.
        """
        return "El asiento no se encuentra en el sistema."

    @staticmethod
    def asiento_reservado():
        """
        Devuelve el mensaje de asiento reservado.
        
        Returns:
            str: El mensaje de asiento reservado.
        """
        return "Asiento reservado correctamente."

    @staticmethod
    def asiento_ya_existe():
        """
        Devuelve el mensaje de asiento ya existente.
        
        Returns:
            str: El mensaje de asiento ya existente.
        """
        return "El asiento ya existe en el sistema."

    @staticmethod
    def asiento_ya_reservado():
        """
        Devuelve el mensaje de asiento ya reservado.
        
        Returns:
            str: El mensaje de asiento ya reservado.
        """
        return "El asiento ya está reservado."

    @staticmethod
    def bienvenida():
        """
        Devuelve el mensaje de bienvenida.
        
        Returns:
            str: El mensaje de bienvenida.
        """
        return "Bienvenido al sistema de gestión de asientos del cine."

    @staticmethod
    def confirmar_guardado():
        """
        Devuelve el mensaje de confirmación de guardado.
        
        Returns:
            str: El mensaje de confirmación de guardado.
        """
        return "¿Desea guardar el estado actual antes de salir? (si/no):"

    @staticmethod
    def confirmar_reseteo():
        """
        Devuelve el mensaje de confirmación de reseteo.
        
        Returns:
            str: El mensaje de confirmación de reseteo.
        """
        return "¿Está seguro de que desea resetear el estado? Esto borrará todos los datos. (si/no):"

    @staticmethod
    def dia_invalido():
        """
        Devuelve el mensaje de día inválido.
        
        Returns:
            str: El mensaje de día inválido.
        """
        return "Día inválido. Por favor, intente de nuevo."

    @staticmethod
    def estado_guardado():
        """
        Devuelve el mensaje de estado guardado.
        
        Returns:
            str: El mensaje de estado guardado.
        """
        return "Estado guardado correctamente."

    @staticmethod
    def estado_reseteado():
        """
        Devuelve el mensaje de estado reseteado.
        
        Returns:
            str: El mensaje de estado reseteado.
        """
        return "Estado reseteado correctamente."

    @staticmethod
    def ingrese_dia():
        """
        Devuelve el mensaje para ingresar el día.
        
        Returns:
            str: El mensaje para ingresar el día.
        """
        return "Ingrese el día (1: lunes, 2: martes, 3: miércoles, 4: jueves, 5: viernes, 6: sábado, 7: domingo):"

    @staticmethod
    def ingrese_edad():
        """
        Devuelve el mensaje para ingresar la edad del espectador.
        
        Returns:
            str: El mensaje para ingresar la edad del espectador.
        """
        return "Ingrese la edad del espectador:"

    @staticmethod
    def ingrese_fila():
        """
        Devuelve el mensaje para ingresar la fila.
        
        Returns:
            str: El mensaje para ingresar la fila.
        """
        return "Ingrese la fila (A-J):"

    @staticmethod
    def ingrese_nueva_fila():
        """
        Devuelve el mensaje para ingresar la nueva fila.
        
        Returns:
            str: El mensaje para ingresar la nueva fila.
        """
        return "Ingrese la nueva fila (A-J):"

    @staticmethod
    def ingrese_nuevo_numero_asiento():
        """
        Devuelve el mensaje para ingresar el nuevo número de asiento.
        
        Returns:
            str: El mensaje para ingresar el nuevo número de asiento.
        """
        return "Ingrese el nuevo número de asiento (1-10):"

    @staticmethod
    def ingrese_numero_asiento():
        """
        Devuelve el mensaje para ingresar el número de asiento.
        
        Returns:
            str: El mensaje para ingresar el número de asiento.
        """
        return "Ingrese el número de asiento (1-10):"

    @staticmethod
    def max_intentos():
        """
        Devuelve el mensaje de número máximo de intentos alcanzado.
        
        Returns:
            str: El mensaje de número máximo de intentos alcanzado.
        """
        return "Número máximo de intentos alcanzado. Por favor, intente de nuevo más tarde."

    @staticmethod
    def opcion_invalida():
        """
        Devuelve el mensaje de opción inválida.
        
        Returns:
            str: El mensaje de opción inválida.
        """
        return "Opción inválida. Por favor, intente de nuevo."

    @staticmethod
    def reporte_disponibilidad(dia, libres, reservados, no_agregados):
        """
        Devuelve el mensaje de reporte de disponibilidad.
        
        Args:
            dia (str): El día de la semana.
            libres (int): Número de asientos libres.
            reservados (int): Número de asientos reservados.
            no_agregados (int): Número de asientos no agregados.
        
        Returns:
            str: El mensaje de reporte de disponibilidad.
        """
        return f"{dia.capitalize()}: {libres} asientos libres, {reservados} asientos reservados, {no_agregados} asientos no agregados."

    @staticmethod
    def reserva_cancelada():
        """
        Devuelve el mensaje de reserva cancelada.
        
        Returns:
            str: El mensaje de reserva cancelada.
        """
        return "Reserva cancelada correctamente."

    @staticmethod
    def reseteo_cancelado():
        """
        Devuelve el mensaje de reseteo cancelado.
        
        Returns:
            str: El mensaje de reseteo cancelado.
        """
        return "Reseteo de estado cancelado."

    @staticmethod
    def saliendo_sistema():
        """
        Devuelve el mensaje de salida del sistema.
        
        Returns:
            str: El mensaje de salida del sistema.
        """
        return "Saliendo del sistema..."