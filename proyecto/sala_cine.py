import logging
from proyecto.asiento import Asiento
from proyecto.utilidades import calculate_discount

# Configurar el logger
logging.basicConfig(filename='debug.log', level=logging.DEBUG)

class SalaCine:
    """
    Clase que representa una sala de cine y gestiona los asientos.
    
    Atributos:
        asientos (list): Lista de objetos Asiento.
        precio_base (float): El precio base de los asientos.
    """
    
    def __init__(self, precio_base):
        """
        Inicializa una nueva sala de cine con el precio base especificado.
        
        Args:
            precio_base (float): El precio base de los asientos.
        """
        self.__asientos = []
        self.__precio_base = precio_base

    def agregar_asiento(self, numero, fila):
        """
        Agrega un nuevo asiento a la sala.
        
        Args:
            numero (int): El número del asiento.
            fila (str): La fila del asiento.
        
        Raises:
            Exception: Si el asiento ya está registrado.
        """
        if any(asiento.numero == numero and asiento.fila == fila for asiento in self.__asientos):
            raise Exception("Este asiento ya está registrado.")
        self.__asientos.append(Asiento(numero, fila, self.__precio_base))
        logging.debug(f'Asiento {numero} en fila {fila} agregado.')

    def reservar_asiento(self, numero, fila, edad, dia):
        """
        Reserva un asiento específico aplicando un descuento basado en la edad del espectador y el día de la semana.
        
        Args:
            numero (int): El número del asiento.
            fila (str): La fila del asiento.
            edad (int): La edad del espectador.
            dia (str): El día de la semana.
        
        Raises:
            Exception: Si el asiento no se encuentra.
        """
        asiento = self.buscar_asiento(numero, fila)
        if asiento is None:
            raise Exception("Asiento no encontrado.")
        descuento = calculate_discount(self.__precio_base, edad, dia)
        asiento.reservar(descuento)
        logging.debug(f'Asiento {numero} en fila {fila} reservado con descuento {descuento}.')

    def cancelar_reserva(self, numero, fila):
        """
        Cancela la reserva de un asiento específico.
        
        Args:
            numero (int): El número del asiento.
            fila (str): La fila del asiento.
        
        Raises:
            Exception: Si el asiento no se encuentra.
        """
        asiento = self.buscar_asiento(numero, fila)
        if asiento is None:
            raise Exception("Asiento no encontrado.")
        asiento.cancelar_reserva()
        logging.debug(f'Reserva del asiento {numero} en fila {fila} cancelada.')

    def mostrar_asientos(self):
        """
        Muestra todos los asientos en la sala.
        """
        for asiento in self.__asientos:
            print(asiento)
        logging.debug('Mostrando todos los asientos.')

    def buscar_asiento(self, numero, fila):
        """
        Busca un asiento específico por su número y fila.
        
        Args:
            numero (int): El número del asiento.
            fila (str): La fila del asiento.
        
        Returns:
            Asiento: El objeto Asiento si se encuentra, None en caso contrario.
        """
        for asiento in self.__asientos:
            if asiento.numero == numero and asiento.fila == fila:
                return asiento
        return None