from mensajes import Mensajes

class Asiento:
    """
    Clase que representa un asiento en la sala de cine.
    
    Atributos:
        fila (str): La fila del asiento.
        numero (int): El número del asiento.
        estado (str): El estado del asiento ('libre' o 'reservado').
    """
    
    def __init__(self, fila, numero, estado="libre"):
        """
        Inicializa un nuevo asiento con la fila, número y estado especificados.
        
        Args:
            fila (str): La fila del asiento.
            numero (int): El número del asiento.
            estado (str): El estado del asiento (por defecto es 'libre').
        
        Raises:
            ValueError: Si el estado no es 'libre' o 'reservado'.
        """
        if estado not in ["libre", "reservado"]:
            raise ValueError("El estado debe ser 'libre' o 'reservado'.")
        self.fila = fila
        self.numero = numero
        self.estado = estado

    def reservar(self):
        """
        Reserva el asiento si está libre.
        
        Returns:
            str: Un mensaje indicando si la reserva fue exitosa o si el asiento ya estaba reservado.
        
        Raises:
            Exception: Si el asiento ya está reservado.
        """
        if self.estado == "libre":
            self.estado = "reservado"
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
        if self.estado == "reservado":
            self.estado = "libre"
            return Mensajes.reserva_cancelada()
        raise Exception("El asiento no está reservado.")

    def to_dict(self):
        """
        Convierte el objeto Asiento a un diccionario.
        
        Returns:
            dict: Un diccionario con los atributos del asiento.
        """
        return {
            "fila": self.fila,
            "numero": self.numero,
            "estado": self.estado
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
            ValueError: Si el estado no es 'libre' o 'reservado'.
        """
        if "fila" not in data or "numero" not in data or "estado" not in data:
            raise KeyError("El diccionario debe contener las claves 'fila', 'numero' y 'estado'.")
        if data["estado"] not in ["libre", "reservado"]:
            raise ValueError("El estado debe ser 'libre' o 'reservado'.")
        return cls(data["fila"], data["numero"], data["estado"])