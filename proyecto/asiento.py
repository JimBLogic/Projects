import json
import logging

# Configurar el logger
logging.basicConfig(filename='debug.log', level=logging.DEBUG)

class Asiento:
    """
    Clase que representa un asiento en la sala de cine.
    
    Atributos:
        numero (int): El número del asiento.
        fila (str): La fila del asiento.
        reservado (bool): Estado de la reserva (True o False).
        precio (float): El precio del asiento.
    """
    
    def __init__(self, numero, fila, precio_base):
        """
        Inicializa un nuevo asiento con el número, fila, estado de reserva y precio base especificados.
        
        Args:
            numero (int): El número del asiento.
            fila (str): La fila del asiento.
            precio_base (float): El precio base del asiento.
        """
        self.__numero = numero
        self.__fila = fila
        self.__reservado = False
        self.__precio_base = precio_base
        self.__precio_actual = precio_base

    @property
    def numero(self):
        return self.__numero

    @property
    def fila(self):
        return self.__fila

    @property
    def reservado(self):
        return self.__reservado

    @property
    def precio(self):
        return self.__precio_actual

    def reservar(self, descuento=0):
        """
        Reserva el asiento si está libre, aplicando el descuento especificado.
        
        Args:
            descuento (float): El porcentaje de descuento a aplicar.
        
        Raises:
            Exception: Si el asiento ya está reservado.
        """
        if self.__reservado:
            raise Exception("Este asiento ya está reservado.")
        self.__precio_actual = self.__precio_base * (1 - descuento)
        self.__reservado = True
        logging.debug(f'Asiento {self.__numero} en fila {self.__fila} reservado con descuento {descuento}.')
        return "Asiento reservado correctamente."

    def cancelar_reserva(self):
        """
        Cancela la reserva del asiento si está reservado.
        
        Raises:
            Exception: Si el asiento no está reservado.
        """
        if not self.__reservado:
            raise Exception("Este asiento no está reservado.")
        self.__reservado = False
        self.__precio_actual = self.__precio_base
        logging.debug(f'Reserva del asiento {self.__numero} en fila {self.__fila} cancelada.')
        return "Reserva cancelada correctamente."

    def __str__(self):
        estado = "Reservado" if self.__reservado else "Disponible"
        return f"Asiento {self.__numero} en fila {self.__fila}: {estado} - Precio: {self.__precio_actual:.2f}€"

    def to_dict(self):
        """
        Convierte el objeto Asiento a un diccionario.
        
        Returns:
            dict: Un diccionario con los atributos del asiento.
        """
        return {
            "numero": self.__numero,
            "fila": self.__fila,
            "reservado": self.__reservado,
            "precio": self.__precio_actual
        }

    @classmethod
    def from_dict(cls, data):
        """
        Crea un objeto Asiento a partir de un diccionario.
        
        Args:
            data (dict): Un diccionario con los atributos del asiento.
        
        Returns:
            Asiento: Un objeto Asiento inicializado con los datos del diccionario.
        """
        return cls(data["numero"], data["fila"], data["precio"])

    @staticmethod
    def guardar_estado(asientos, filename='estado_cine.json'):
        """
        Guarda el estado de los asientos en un archivo .json.
        
        Args:
            asientos (list): Lista de objetos Asiento.
            filename (str): Nombre del archivo .json donde se guardará el estado.
        """
        estado = [asiento.to_dict() for asiento in asientos]
        with open(filename, 'w') as file:
            json.dump(estado, file, indent=4)
        logging.debug(f'Estado de los asientos guardado en {filename}.')