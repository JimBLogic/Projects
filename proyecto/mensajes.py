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
        return int(input("Ingrese el número del asiento: "))

    @staticmethod
    def solicitar_fila_asiento():
        """
        Solicita al usuario la fila del asiento.
        
        Returns:
            str: La fila del asiento ingresada por el usuario.
        """
        return input("Ingrese la fila del asiento: ")

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
        return input("Ingrese el día de la semana: ")

    @staticmethod
    def mostrar_precio_final(precio):
        """
        Muestra el precio final de la reserva.
        
        Args:
            precio (float): El precio final a mostrar.
        """
        print(f"El precio final de la reserva es: {precio:.2f}€")