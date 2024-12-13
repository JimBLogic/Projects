import json
import logging
from asiento import Asiento
from mensajes import Mensajes

class SalaCine:
    """
    Clase que representa una sala de cine y gestiona los asientos.
    
    Atributos:
        archivo_estado (str): El nombre del archivo donde se guarda el estado de la sala.
        estado (dict): Un diccionario que contiene el estado de los asientos por día.
    """
    
    def __init__(self, archivo_estado='estado_sala.json'):
        """
        Inicializa una nueva sala de cine y carga el estado desde un archivo.
        
        Args:
            archivo_estado (str): El nombre del archivo donde se guarda el estado de la sala.
        """
        self.archivo_estado = archivo_estado
        self.estado = self.cargar_estado()

    def cargar_estado(self):
        """
        Carga el estado de la sala desde un archivo JSON.
        
        Returns:
            dict: Un diccionario con el estado de los asientos por día.
        """
        try:
            with open(self.archivo_estado, 'r') as file:
                data = json.load(file)
                for dia, asientos in data.items():
                    data[dia] = [Asiento.from_dict(asiento) for asiento in asientos]
                return data
        except FileNotFoundError:
            logging.warning("Archivo de estado no encontrado, creando nuevo estado.")
            return {dia: [] for dia in ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]}

    def guardar_estado(self):
        """
        Guarda el estado de la sala en un archivo JSON.
        """
        with open(self.archivo_estado, 'w') as file:
            data = {dia: [asiento.to_dict() for asiento in asientos] for dia, asientos in self.estado.items()}
            json.dump(data, file, indent=4)

    def agregar_asiento(self, dia, fila, numero):
        """
        Agrega un asiento a la sala en el día especificado.
        
        Args:
            dia (str): El día de la semana.
            fila (str): La fila del asiento.
            numero (int): El número del asiento.
        
        Returns:
            str: Un mensaje indicando si el asiento fue agregado correctamente.
        
        Raises:
            ValueError: Si el día es inválido o el asiento ya existe.
        """
        if dia not in self.estado:
            raise ValueError(Mensajes.dia_invalido())
        for asiento in self.estado[dia]:
            if asiento.fila == fila and asiento.numero == numero:
                raise ValueError(Mensajes.asiento_ya_existe())
        self.estado[dia].append(Asiento(fila, numero))
        self.guardar_estado()
        logging.info(f"Asiento agregado: {dia}, {fila}, {numero}")
        return Mensajes.asiento_agregado()

    def reservar_asiento(self, dia, fila, numero):
        """
        Reserva un asiento en el día especificado.
        
        Args:
            dia (str): El día de la semana.
            fila (str): La fila del asiento.
            numero (int): El número del asiento.
        
        Returns:
            str: Un mensaje indicando si la reserva fue exitosa o si el asiento no fue encontrado.
        """
        for asiento in self.estado[dia]:
            if asiento.fila == fila and asiento.numero == numero:
                logging.info(f"Asiento reservado: {dia}, {fila}, {numero}")
                return asiento.reservar()
        return Mensajes.asiento_no_encontrado()

    def cancelar_reserva(self, dia, fila, numero):
        """
        Cancela la reserva de un asiento en el día especificado.
        
        Args:
            dia (str): El día de la semana.
            fila (str): La fila del asiento.
            numero (int): El número del asiento.
        
        Returns:
            str: Un mensaje indicando si la cancelación fue exitosa o si el asiento no fue encontrado.
        """
        for asiento in self.estado[dia]:
            if asiento.fila == fila and asiento.numero == numero:
                logging.info(f"Reserva cancelada: {dia}, {fila}, {numero}")
                return asiento.cancelar()
        return Mensajes.asiento_no_encontrado()

    def reporte_disponibilidad(self):
        """
        Genera un reporte de la disponibilidad de asientos por día.
        
        Returns:
            dict: Un diccionario con la cantidad de asientos libres y reservados por día.
        """
        reporte = {}
        total_asientos = 100  # Suponiendo que hay 100 asientos en total
        for dia, asientos in self.estado.items():
            libres = sum(1 for asiento in asientos if asiento.estado == "libre")
            reservados = sum(1 for asiento in asientos if asiento.estado == "reservado")
            no_agregados = total_asientos - (libres + reservados)
            reporte[dia] = {"libres": libres, "reservados": reservados, "no_agregados": no_agregados}
        return reporte