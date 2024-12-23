import logging
from proyecto.asiento import Asiento
from proyecto.utilidades import calculate_discount, load_state_file, save_state_file

# Configurar el logger
logging.basicConfig(filename='debug.log', level=logging.DEBUG)

class SalaCine:
    """
    Clase que representa una sala de cine y gestiona los asientos.
    
    Atributos:
        asientos (list): Lista de objetos Asiento.
        precio_base (float): El precio base de los asientos.
    """
    
    def __init__(self, precio_base, archivo_estado=None):
        self.__asientos = []
        self.__precio_base = precio_base
        self.__archivo_estado = archivo_estado
        if archivo_estado:
            self.cargar_estado()

    @property
    def asientos(self):
        return self.__asientos

    @property
    def precio_base(self):
        return self.__precio_base

    def cargar_estado(self):
        """
        Carga el estado de los asientos desde un archivo.
        """
        estado = load_state_file(self.__archivo_estado)
        self.__asientos = [Asiento.from_dict(asiento_data) for asiento_data in estado]
        logging.debug(f'Estado cargado desde {self.__archivo_estado}.')

    def guardar_estado(self):
        """
        Guarda el estado de los asientos en un archivo.
        """
        estado = [asiento.to_dict() for asiento in self.__asientos]
        save_state_file(self.__archivo_estado, estado)
        logging.debug(f'Estado guardado en {self.__archivo_estado}.')

    def agregar_asiento(self, numero, fila):
        """
        Agrega un asiento a la sala de cine.
        
        Args:
            numero (int): El número del asiento.
            fila (str): La fila del asiento.
        
        Raises:
            ValueError: Si el asiento ya existe o si los parámetros son inválidos.
        """
        if not (1 <= numero <= 10):
            raise ValueError("El número del asiento debe estar entre 1 y 10.")
        if fila not in "ABCDEFGHIJ":
            raise ValueError("La fila del asiento debe estar entre A y J.")
        if self.buscar_asiento(numero, fila) is None:
            nuevo_asiento = Asiento(numero, fila, False, self.__precio_base)
            self.__asientos.append(nuevo_asiento)
            logging.debug(f'Asiento {numero}{fila} agregado.')
            self.guardar_estado()
        else:
            logging.error(f'Asiento {numero}{fila} ya existe.')
            raise ValueError("El asiento ya existe.")

    def reservar_asiento(self, numero, fila, edad, dia):
        """
        Reserva un asiento en la sala de cine.
        
        Args:
            numero (int): El número del asiento.
            fila (str): La fila del asiento.
            edad (int): La edad del espectador.
            dia (str): El día de la semana.
        
        Raises:
            ValueError: Si el asiento no se encuentra en el sistema o si los parámetros son inválidos.
            Exception: Si el asiento ya está reservado.
        """
        if not (1 <= numero <= 10):
            raise ValueError("El número del asiento debe estar entre 1 y 10.")
        if fila not in "ABCDEFGHIJ":
            raise ValueError("La fila del asiento debe estar entre A y J.")
        if not (1 <= edad <= 100):
            raise ValueError("La edad debe estar entre 1 y 100.")
        asiento = self.buscar_asiento(numero, fila)
        if asiento:
            descuento = calculate_discount(self.__precio_base, edad, dia)
            asiento.reservar(descuento)
            self.guardar_estado()
        else:
            logging.error(f'Asiento {numero}{fila} no encontrado.')
            raise ValueError("El asiento no se encuentra en el sistema.")

    def cancelar_reserva(self, numero, fila):
        """
        Cancela la reserva de un asiento en la sala de cine.
        
        Args:
            numero (int): El número del asiento.
            fila (str): La fila del asiento.
        
        Raises:
            ValueError: Si el asiento no se encuentra en el sistema.
            Exception: Si el asiento no está reservado.
        """
        if not (1 <= numero <= 10):
            raise ValueError("El número del asiento debe estar entre 1 y 10.")
        if fila not in "ABCDEFGHIJ":
            raise ValueError("La fila del asiento debe estar entre A y J.")
        asiento = self.buscar_asiento(numero, fila)
        if asiento:
            asiento.cancelar_reserva()
            self.guardar_estado()
        else:
            logging.error(f'Asiento {numero}{fila} no encontrado.')
            raise ValueError("El asiento no se encuentra en el sistema.")

    def mostrar_asientos(self):
        """
        Muestra todos los asientos en la sala de cine.
        """
        for asiento in self.__asientos:
            print(asiento)

    def buscar_asiento(self, numero, fila):
        """
        Busca un asiento en la sala de cine.
        
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