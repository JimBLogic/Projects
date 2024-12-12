import json
import os
from asiento import Asiento
from mensajes import Mensajes
from utilidades import calcular_descuento

class SalaCine:
    """
    Clase que representa una sala de cine con múltiples asientos.
    """
    MAX_FILA = 10  # Número máximo de filas en la sala
    MAX_ASIENTO = 20  # Número máximo de asientos por fila

    def __init__(self, precio_base=10.0):
        """
        Inicializa una sala de cine con un precio base para los asientos.

        Args:
            precio_base (float): El precio base de los asientos.
        """
        self.__asientos = {dia: [] for dia in ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]}
        self.__precio_base = precio_base  # Precio base de los asientos

    def agregar_asiento(self, numero, fila, dia_semana):
        """
        Agrega un asiento a la sala de cine.
        Lanza una excepción si el número de fila o asiento está fuera de los límites permitidos,
        o si el asiento ya ha sido agregado para el mismo día.

        Args:
            numero (int): El número del asiento.
            fila (int): La fila del asiento.
            dia_semana (str): El día de la semana en que el asiento está disponible.

        Returns:
            str: Un mensaje confirmando que el asiento ha sido agregado.

        Raises:
            ValueError: Si el número de fila o asiento está fuera de los límites permitidos,
                        o si el asiento ya ha sido agregado para el mismo día.
        """
        if fila > self.MAX_FILA or fila < 1:
            raise ValueError(f"Error: La fila debe estar entre 1 y {self.MAX_FILA}.")
        if numero > self.MAX_ASIENTO or numero < 1:
            raise ValueError(f"Error: El número de asiento debe estar entre 1 y {self.MAX_ASIENTO}.")

        for a in self.__asientos[dia_semana]:
            if a.get_numero() == numero and a.get_fila() == fila:
                raise ValueError(f"Asiento {numero} en fila {fila} para el día {dia_semana} ya está agregado.")

        asiento = Asiento(numero, fila, dia_semana)
        self.__asientos[dia_semana].append(asiento)
        return Mensajes.asiento_agregado(numero, fila, dia_semana)

    def reservar_asiento(self, numero, fila, dia_semana, edad):
        """
        Reserva un asiento en la sala de cine.
        Lanza una excepción si el asiento no ha sido agregado o ya está reservado.
        Calcula el precio final del asiento aplicando descuentos según el día de la semana y la edad del espectador.

        Args:
            numero (int): El número del asiento.
            fila (int): La fila del asiento.
            dia_semana (str): El día de la semana en que el asiento está disponible.
            edad (int): La edad del espectador.

        Returns:
            str: Un mensaje confirmando que el asiento ha sido reservado.

        Raises:
            ValueError: Si el asiento no ha sido agregado o ya está reservado.
        """
        asiento = self.buscar_asiento(numero, fila, dia_semana)
        if asiento is None:
            raise ValueError(Mensajes.error_asiento_no_encontrado(numero, fila, dia_semana))

        if asiento.get_reservado():
            raise ValueError(f"Asiento {numero} en fila {fila} para el día {dia_semana} ya está reservado.")

        descuento = calcular_descuento(self.__precio_base, edad, dia_semana)
        precio_final = self.__precio_base * (1 - descuento)
        descuentos_aplicados = []

        if dia_semana == "miércoles":
            descuentos_aplicados.append("20% de descuento los miércoles")
        if edad >= 65:
            descuentos_aplicados.append("30% de descuento para mayores de 65 años")

        asiento.set_precio(precio_final)
        asiento.set_edad(edad)
        asiento.set_descuentos(descuentos_aplicados)
        mensaje_reserva = asiento.reservar()

        if descuentos_aplicados:
            print(Mensajes.descuentos_aplicados(descuentos_aplicados))
        print(Mensajes.precio_final(precio_final))
        return mensaje_reserva

    def cancelar_reserva(self, numero, fila, dia_semana, confirmacion):
        """
        Cancela la reserva de un asiento en la sala de cine.
        Lanza una excepción si el asiento no ha sido encontrado.

        Args:
            numero (int): El número del asiento.
            fila (int): La fila del asiento.
            dia_semana (str): El día de la semana en que el asiento está disponible.
            confirmacion (str): Confirmación de la cancelación ("si" para confirmar).

        Returns:
            str: Un mensaje confirmando que la reserva ha sido cancelada.

        Raises:
            ValueError: Si el asiento no ha sido encontrado.
        """
        asiento = self.buscar_asiento(numero, fila, dia_semana)
        if asiento:
            return asiento.cancelar_reserva(confirmacion)
        else:
            raise ValueError(Mensajes.error_asiento_no_encontrado(numero, fila, dia_semana))

    def mostrar_asientos(self, filtro_dia=None, filtro_estado=None, filtro_precio=None):
        """
        Muestra los asientos de la sala de cine, aplicando filtros opcionales por día, estado y precio.

        Args:
            filtro_dia (str, optional): Filtra los asientos por día de la semana.
            filtro_estado (str, optional): Filtra los asientos por estado ("reservado" o "disponible").
            filtro_precio (float, optional): Filtra los asientos por precio máximo.
        """
        asientos_filtrados = []
        if filtro_dia:
            asientos_filtrados = self.__asientos[filtro_dia]
        else:
            for dia in self.__asientos:
                asientos_filtrados.extend(self.__asientos[dia])

        if filtro_estado:
            asientos_filtrados = [a for a in asientos_filtrados if a.get_reservado() == (filtro_estado == "reservado")]
        if filtro_precio:
            asientos_filtrados = [a for a in asientos_filtrados if a.get_precio() <= filtro_precio]

        for asiento in asientos_filtrados:
            print(asiento)

    def buscar_asiento(self, numero, fila, dia_semana):
        """
        Busca un asiento en la sala de cine por su número, fila y día de la semana.
        Devuelve el asiento si es encontrado, o None si no lo es.

        Args:
            numero (int): El número del asiento.
            fila (int): La fila del asiento.
            dia_semana (str): El día de la semana en que el asiento está disponible.

        Returns:
            Asiento: El asiento encontrado, o None si no se encuentra.
        """
        for asiento in self.__asientos[dia_semana]:
            if asiento.get_numero() == numero and asiento.get_fila() == fila:
                return asiento
        return None

    def hay_asientos_en_dia(self, dia_semana):
        """
        Verifica si hay asientos agregados en un día específico.
        Devuelve True si hay asientos, o False si no los hay.

        Args:
            dia_semana (str): El día de la semana.

        Returns:
            bool: True si hay asientos, False en caso contrario.
        """
        return len(self.__asientos[dia_semana]) > 0

    def to_dict(self):
        """
        Convierte la lista de asientos de la sala de cine a una lista de diccionarios.

        Returns:
            dict: Un diccionario que representa los asientos por día.
        """
        return {dia: [asiento.to_dict() for asiento in asientos] for dia, asientos in self.__asientos.items()}

    def from_dict(self, data):
        """
        Carga la lista de asientos de la sala de cine desde una lista de diccionarios.

        Args:
            data (dict): Un diccionario que representa los asientos por día.
        """
        self.__asientos = {dia: [Asiento(a["numero"], a["fila"], a["dia_semana"]) for a in asientos] for dia, asientos in data.items()}
        for dia, asientos in data.items():
            for asiento, a in zip(self.__asientos[dia], asientos):
                asiento.set_precio(a["precio"])
                asiento.set_edad(a["edad"])
                asiento.set_descuentos(a["descuentos"])
                if a["reservado"]:
                    asiento.reservar()

    def calcular_precio(self, precio_base, dia_semana, edad):
        """
        Calcula el precio final de un asiento aplicando descuentos según el día de la semana y la edad del espectador.
        Devuelve el precio final y una lista de descuentos aplicados.

        Args:
            precio_base (float): El precio base del asiento.
            dia_semana (str): El día de la semana.
            edad (int): La edad del espectador.

        Returns:
            tuple: El precio final y una lista de descuentos aplicados.
        """
        descuento = 0.0
        descuentos_aplicados = []

        if dia_semana == "miércoles":
            descuento += 0.2
            descuentos_aplicados.append("20% de descuento los miércoles")
        if edad > 65:
            descuento += 0.3
            descuentos_aplicados.append("30% de descuento para mayores de 65 años")

        precio_final = precio_base * (1 - descuento)
        return precio_final, descuentos_aplicados

def guardar_estado(sala):
    """
    Guarda el estado actual de la sala de cine en un archivo JSON.

    Args:
        sala (SalaCine): La instancia de la sala de cine a guardar.
    """
    try:
        with open("estado_sala.json", "w") as file:
            json.dump(sala.to_dict(), file)
        print(Mensajes.estado_guardado())
    except Exception as e:
        print(f"Error al guardar el estado: {e}")

def cargar_estado():
    """
    Carga el estado de la sala de cine desde un archivo JSON.
    Si el archivo no existe o está corrupto, se inicia una nueva sala.

    Returns:
        SalaCine: La instancia de la sala de cine cargada.
    """
    if not os.path.exists("estado_sala.json"):
        print(Mensajes.estado_no_encontrado())
        return SalaCine()
    try:
        with open("estado_sala.json", "r") as file:
            data = json.load(file)
            sala = SalaCine()
            sala.from_dict(data)
            print(Mensajes.estado_cargado())
            return sala
    except (json.JSONDecodeError, KeyError) as e:
        print(Mensajes.estado_error_carga(e))
        return SalaCine()

def reset_estado():
    """
    Resetea el estado de la sala de cine eliminando el archivo JSON.
    """
    try:
        if os.path.exists("estado_sala.json"):
            os.remove("estado_sala.json")
        print(Mensajes.estado_reseteado())
    except Exception as e:
        print(f"Error al resetear el estado: {e}")