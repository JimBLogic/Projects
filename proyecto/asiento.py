class Asiento:
    """
    Clase que representa un asiento en una sala de cine.
    """

    def __init__(self, numero, fila, dia_semana):
        """
        Inicializa un asiento con su número, fila y día de la semana.

        Args:
            numero (int): El número del asiento.
            fila (int): La fila del asiento.
            dia_semana (str): El día de la semana en que el asiento está disponible.
        """
        self.__numero = numero
        self.__fila = fila
        self.__dia_semana = dia_semana
        self.__reservado = False
        self.__precio = 0.0
        self.__edad = 0
        self.__descuentos = []

    def get_numero(self):
        """
        Devuelve el número del asiento.

        Returns:
            int: El número del asiento.
        """
        return self.__numero

    def get_fila(self):
        """
        Devuelve la fila del asiento.

        Returns:
            int: La fila del asiento.
        """
        return self.__fila

    def get_dia_semana(self):
        """
        Devuelve el día de la semana del asiento.

        Returns:
            str: El día de la semana del asiento.
        """
        return self.__dia_semana

    def get_reservado(self):
        """
        Devuelve si el asiento está reservado.

        Returns:
            bool: True si el asiento está reservado, False en caso contrario.
        """
        return self.__reservado

    def get_precio(self):
        """
        Devuelve el precio del asiento.

        Returns:
            float: El precio del asiento.
        """
        return self.__precio

    def get_edad(self):
        """
        Devuelve la edad del espectador que reservó el asiento.

        Returns:
            int: La edad del espectador.
        """
        return self.__edad

    def get_descuentos(self):
        """
        Devuelve los descuentos aplicados al asiento.

        Returns:
            list: Una lista de descuentos aplicados.
        """
        return self.__descuentos

    def set_precio(self, precio):
        """
        Establece el precio del asiento.
        Lanza una excepción si el asiento ya está reservado.

        Args:
            precio (float): El precio del asiento.

        Raises:
            ValueError: Si el asiento ya está reservado.
        """
        if self.__reservado:
            raise ValueError("No se puede modificar el precio de un asiento reservado.")
        self.__precio = precio

    def set_edad(self, edad):
        """
        Establece la edad del espectador que reservó el asiento.
        Lanza una excepción si el asiento ya está reservado.

        Args:
            edad (int): La edad del espectador.

        Raises:
            ValueError: Si el asiento ya está reservado.
        """
        if self.__reservado:
            raise ValueError("No se puede modificar la edad de un asiento reservado.")
        self.__edad = edad

    def set_descuentos(self, descuentos):
        """
        Establece los descuentos aplicados al asiento.
        Lanza una excepción si el asiento ya está reservado.

        Args:
            descuentos (list): Una lista de descuentos aplicados.

        Raises:
            ValueError: Si el asiento ya está reservado.
        """
        if self.__reservado:
            raise ValueError("No se pueden modificar los descuentos de un asiento reservado.")
        self.__descuentos = descuentos

    def reservar(self):
        """
        Reserva el asiento.
        Lanza una excepción si el asiento ya está reservado.

        Returns:
            str: Un mensaje confirmando la reserva del asiento.

        Raises:
            ValueError: Si el asiento ya está reservado.
        """
        if not self.__reservado:
            self.__reservado = True
            return f"Asiento {self.__numero} en fila {self.__fila} reservado."
        else:
            raise ValueError(f"Asiento {self.__numero} en fila {self.__fila} ya está reservado.")

    def cancelar_reserva(self, confirmacion):
        """
        Cancela la reserva del asiento si la confirmación es "si".
        Lanza una excepción si el asiento no está reservado.

        Args:
            confirmacion (str): Confirmación de la cancelación ("si" para confirmar).

        Returns:
            str: Un mensaje confirmando la cancelación de la reserva.

        Raises:
            ValueError: Si el asiento no está reservado.
        """
        if confirmacion == "si":
            if self.__reservado:
                self.__reservado = False
                return f"Asiento {self.__numero} en fila {self.__fila} ahora está disponible."
            else:
                raise ValueError(f"Asiento {self.__numero} en fila {self.__fila} no está reservado.")
        else:
            return "Cancelación de reserva abortada."

    def __str__(self):
        """
        Devuelve una representación en cadena del asiento.

        Returns:
            str: Una cadena que representa el estado del asiento.
        """
        estado = "Reservado" if self.__reservado else "Disponible"
        descuentos = ", ".join(self.__descuentos) if self.__descuentos else "Sin descuentos"
        return f"Día: {self.__dia_semana}, Estado: {estado}, Fila: {self.__fila}, Asiento: {self.__numero}, Precio: €{self.__precio:.2f}, Edad: {self.__edad}, Descuentos: {descuentos}"

    def to_dict(self):
        """
        Convierte el asiento a un diccionario.

        Returns:
            dict: Un diccionario que representa el asiento.
        """
        return {
            "numero": self.__numero,
            "fila": self.__fila,
            "dia_semana": self.__dia_semana,
            "reservado": self.__reservado,
            "precio": self.__precio,
            "edad": self.__edad,
            "descuentos": self.__descuentos
        }

    @classmethod
    def from_dict(cls, data):
        """
        Crea un objeto Asiento a partir de un diccionario.

        Args:
            data (dict): Un diccionario que representa el asiento.

        Returns:
            Asiento: Un objeto Asiento.
        """
        asiento = cls(data["numero"], data["fila"], data["dia_semana"])
        asiento.__reservado = data["reservado"]
        asiento.__precio = data["precio"]
        asiento.__edad = data["edad"]
        asiento.__descuentos = data["descuentos"]
        return asiento