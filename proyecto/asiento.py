from proyecto.mensajes import Mensajes

class Asiento:
    """
    Clase que representa un asiento en la sala de cine.
    
    Atributos:
        numero (int): El número del asiento.
        fila (str): La fila del asiento.
        reservado (bool): Estado de la reserva (True o False).
        precio (float): El precio del asiento.
    """
    
    def __init__(self, numero, fila, reservado=False, precio=0.0):
        """
        Inicializa un nuevo asiento con el número, fila, estado de reserva y precio especificados.
        
        Args:
            numero (int): El número del asiento.
            fila (str): La fila del asiento.
            reservado (bool): El estado del asiento (por defecto es False).
            precio (float): El precio del asiento.
        """
        self._numero = numero
        self._fila = fila
        self._reservado = reservado
        self._precio = precio

    def get_numero(self):
        return self._numero

    def set_numero(self, numero):
        self._numero = numero

    def get_fila(self):
        return self._fila

    def set_fila(self, fila):
        self._fila = fila

    def is_reservado(self):
        return self._reservado

    def set_reservado(self, reservado):
        self._reservado = reservado

    def get_precio(self):
        return self._precio

    def set_precio(self, precio):
        self._precio = precio

    def reservar(self):
        """
        Reserva el asiento si está libre.
        
        Returns:
            str: Un mensaje indicando si la reserva fue exitosa o si el asiento ya estaba reservado.
        
        Raises:
            Exception: Si el asiento ya está reservado.
        """
        if not self.is_reservado():
            self.set_reservado(True)
            return Mensajes.asiento_reservado()
        raise Exception("El asiento ya está reservado.")

    def cancelar(self):
        """
        Cancela la reserva del asiento si está reservado.
        
        Returns:
            str: Un mensaje indicando si la cancelación fue exitosa o si el asiento no estaba reservado.
        
        Raises:
            Exception: Si el asiento no está reservado.
        """
        if self.is_reservado():
            self.set_reservado(False)
            return Mensajes.reserva_cancelada()
        raise Exception("El asiento no está reservado.")

    def actualizar(self, nueva_fila, nuevo_numero):
        """
        Actualiza la fila y el número del asiento.
        
        Args:
            nueva_fila (str): La nueva fila del asiento.
            nuevo_numero (int): El nuevo número del asiento.
        
        Returns:
            str: Un mensaje indicando que la actualización fue exitosa.
        """
        self.set_fila(nueva_fila)
        self.set_numero(nuevo_numero)
        return Mensajes.asiento_actualizado()

    def to_dict(self):
        """
        Convierte el objeto Asiento a un diccionario.
        
        Returns:
            dict: Un diccionario con los atributos del asiento.
        """
        return {
            "numero": self.get_numero(),
            "fila": self.get_fila(),
            "reservado": self.is_reservado(),
            "precio": self.get_precio()
        }

    @classmethod
    def from_dict(cls, data):
        """
        Crea un objeto Asiento a partir de un diccionario.
        
        Args:
            data (dict): Un diccionario con los atributos del asiento.
        
        Returns:
            Asiento: Un objeto Asiento inicializado con los datos del diccionario.
        
        Raises:
            KeyError: Si falta alguna clave en el diccionario.
        """
        if "numero" not in data or "fila" not in data or "reservado" not in data or "precio" not in data:
            raise KeyError("El diccionario debe contener las claves 'numero', 'fila', 'reservado' y 'precio'.")
        return cls(data["numero"], data["fila"], data["reservado"], data["precio"])