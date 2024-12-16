import json
import logging

class SalaCine:
    """
    Clase que representa una sala de cine y gestiona los asientos.
    
    Atributos:
        archivo_estado (str): El nombre del archivo donde se guarda el estado de la sala.
        estado (dict): Un diccionario que contiene el estado de los asientos por día.
        precio_base (float): El precio base de los asientos.
    """
    
    def __init__(self, archivo_estado='estado_sala.json', precio_base=10.0):
        """
        Inicializa una nueva sala de cine y carga el estado desde un archivo.
        
        Args:
            archivo_estado (str): El nombre del archivo donde se guarda el estado de la sala.
            precio_base (float): El precio base de los asientos.
        """
        self._archivo_estado = archivo_estado
        self._estado = self.cargar_estado()
        self._precio_base = precio_base

    def get_archivo_estado(self):
        return self._archivo_estado

    def set_archivo_estado(self, archivo_estado):
        self._archivo_estado = archivo_estado

    def get_estado(self):
        return self._estado

    def set_estado(self, estado):
        self._estado = estado

    def get_precio_base(self):
        return self._precio_base

    def set_precio_base(self, precio_base):
        self._precio_base = precio_base

    def cargar_estado(self):
        """
        Carga el estado de la sala desde un archivo JSON.
        
        Returns:
            dict: Un diccionario con el estado de los asientos por día.
        """
        from proyecto.asiento import Asiento
        try:
            with open(self._archivo_estado, 'r') as file:
                data = json.load(file)
                for dia, asientos in data.items():
                    data[dia] = [Asiento.from_dict(asiento) for asiento in asientos]
                return data
        except FileNotFoundError:
            logging.warning("Archivo de estado no encontrado, creando nuevo estado.")
            return {dia: [] for dia in ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]}
        except json.JSONDecodeError:
            logging.error("Error al decodificar el archivo JSON, creando nuevo estado.")
            return {dia: [] for dia in ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]}

    def guardar_estado(self):
        """
        Guarda el estado de la sala en un archivo JSON.
        """
        from proyecto.asiento import Asiento
        with open(self._archivo_estado, 'w') as file:
            data = {dia: [asiento.to_dict() for asiento in asientos] for dia, asientos in self._estado.items()}
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
        from proyecto.asiento import Asiento
        from proyecto.mensajes import Mensajes
        if not (fila.isalpha() and len(fila) == 1 and fila.upper() in "ABCDEFGHIJ"):
            raise ValueError("Fila inválida. Debe ser una letra entre A y J.")
        if not (1 <= int(numero) <= 10):
            raise ValueError("Número de asiento inválido. Debe estar entre 1 y 10.")
        if dia not in self._estado:
            raise ValueError(Mensajes.dia_invalido())
        for asiento in self._estado[dia]:
            if asiento.get_fila() == fila and asiento.get_numero() == numero:
                raise ValueError(Mensajes.asiento_ya_existe())
        self._estado[dia].append(Asiento(numero, fila, precio=self._precio_base))
        self.guardar_estado()
        logging.info(f"Asiento agregado: {dia}, {fila}, {numero}")
        return Mensajes.asiento_agregado()

    def reservar_asiento(self, dia, fila, numero, edad):
        """
        Reserva un asiento en el día especificado.
        
        Args:
            dia (str): El día de la semana.
            fila (str): La fila del asiento.
            numero (int): El número del asiento.
            edad (int): La edad del espectador.
        
        Returns:
            str: Un mensaje indicando si la reserva fue exitosa o si el asiento no fue encontrado.
        """
        from proyecto.utilidades import calcular_precio_final
        from proyecto.mensajes import Mensajes
        for asiento in self._estado[dia]:
            if asiento.get_fila() == fila and asiento.get_numero() == numero:
                precio_final = calcular_precio_final(self._precio_base, edad, dia)
                asiento.set_precio(precio_final)
                asiento.set_reservado(True)
                logging.info(f"Asiento reservado: {dia}, {fila}, {numero}, precio: {precio_final}")
                return Mensajes.asiento_reservado()
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
        from proyecto.mensajes import Mensajes
        for asiento in self._estado[dia]:
            if asiento.get_fila() == fila and asiento.get_numero() == numero:
                asiento.set_precio(self._precio_base)  # Resetear el precio al cancelar la reserva
                asiento.set_reservado(False)
                logging.info(f"Reserva cancelada: {dia, fila, numero}")
                return Mensajes.reserva_cancelada()
        return Mensajes.asiento_no_encontrado()

    def mostrar_asientos(self):
        """
        Muestra todos los asientos, indicando si están reservados y su precio.
        
        Returns:
            dict: Un diccionario con la información de los asientos por día.
        """
        asientos_info = {}
        for dia, asientos in self._estado.items():
            asientos_info[dia] = [asiento.to_dict() for asiento in asientos]
        return asientos_info

    def buscar_asiento(self, dia, fila, numero):
        """
        Busca un asiento por número y fila en un día específico.
        
        Args:
            dia (str): El día de la semana.
            fila (str): La fila del asiento.
            numero (int): El número del asiento.
        
        Returns:
            dict: Un diccionario con la información del asiento si se encuentra.
        """
        from proyecto.mensajes import Mensajes
        for asiento in self._estado[dia]:
            if asiento.get_fila() == fila and asiento.get_numero() == numero:
                return asiento.to_dict()
        return Mensajes.asiento_no_encontrado()

    def actualizar_asiento(self, dia, fila, numero, nueva_fila, nuevo_numero):
        """
        Actualiza la información de un asiento específico.
        """
        from proyecto.mensajes import Mensajes
        for asiento in self._estado[dia]:
            if asiento.get_fila() == fila and asiento.get_numero() == numero:
                asiento.set_fila(nueva_fila)
                asiento.set_numero(nuevo_numero)
                self.guardar_estado()
                logging.info(f"Asiento actualizado: {dia}, {fila}, {numero} a {nueva_fila}, {nuevo_numero}")
                return Mensajes.asiento_actualizado()
        return Mensajes.asiento_no_encontrado()

    def eliminar_asiento(self, dia, fila, numero):
        """
        Elimina un asiento de la sala en el día especificado.
        
        Args:
            dia (str): El día de la semana.
            fila (str): La fila del asiento.
            numero (int): El número del asiento.
        
        Returns:
            str: Un mensaje indicando si el asiento fue eliminado correctamente o si no fue encontrado.
        
        Raises:
            ValueError: Si el día es inválido.
        """
        from proyecto.mensajes import Mensajes
        if dia not in self._estado:
            raise ValueError(Mensajes.dia_invalido())
        for asiento in self._estado[dia]:
            if asiento.get_fila() == fila and asiento.get_numero() == numero:
                self._estado[dia].remove(asiento)
                self.guardar_estado()
                logging.info(f"Asiento eliminado: {dia}, {fila}, {numero}")
                return Mensajes.asiento_eliminado()
        return Mensajes.asiento_no_encontrado()