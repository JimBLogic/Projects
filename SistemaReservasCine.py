# Sistema de Reservas para un Cine con Tarifas Especiales

class Asiento:
    """
    Representa un asiento en la sala de cine.
    """

    def __init__(self, numero, fila):
        """
        Inicializa un nuevo asiento.

        Args:
            numero (int): Número del asiento.
            fila (int): Fila del asiento.
        """
        self.__numero = numero
        self.__fila = fila
        self.__reservado = False
        self.__precio = 0.0

    # Getters
    def get_numero(self):
        return self.__numero

    def get_fila(self):
        return self.__fila

    def get_reservado(self):
        return self.__reservado

    def get_precio(self):
        return self.__precio

    # Setters
    def set_precio(self, precio):
        self.__precio = precio

    def reservar(self):
        """
        Reserva el asiento si no está reservado.
        """
        if not self.__reservado:
            self.__reservado = True
            print(f"Asiento {self.__numero} en fila {self.__fila} reservado.")
        else:
            raise ValueError(f"Asiento {self.__numero} en fila {self.__fila} ya está reservado.")

    def cancelar_reserva(self):
        """
        Cancela la reserva del asiento si está reservado.
        """
        if self.__reservado:
            self.__reservado = False
            print(f"Asiento {self.__numero} en fila {self.__fila} ahora está disponible.")
        else:
            raise ValueError(f"Asiento {self.__numero} en fila {self.__fila} no está reservado.")

    def __str__(self):
        """
        Representación del asiento.
        """
        estado = "Reservado" if self.__reservado else "Disponible"
        return f"Asiento {self.__numero}, Fila {self.__fila}, Precio: ${self.__precio:.2f}, Estado: {estado}"


class SalaCine:
    """
    Administra los asientos en una sala de cine.
    """

    def __init__(self):
        self.__asientos = []  # Lista de asientos

    def agregar_asiento(self, asiento):
        """
        Añade un asiento a la sala si no está ya registrado.

        Args:
            asiento (Asiento): El asiento a agregar.
        """
        for a in self.__asientos:
            if a.get_numero() == asiento.get_numero() and a.get_fila() == asiento.get_fila():
                raise ValueError(f"Asiento {asiento.get_numero()} en fila {asiento.get_fila()} ya existe.")
        self.__asientos.append(asiento)

    def reservar_asiento(self, numero, fila, dia_semana, edad):
        """
        Reserva un asiento y calcula su precio según el día y la edad.

        Args:
            numero (int): Número del asiento.
            fila (int): Fila del asiento.
            dia_semana (str): Día de la semana.
            edad (int): Edad del espectador.
        """
        asiento = self.buscar_asiento(numero, fila)
        if asiento:
            precio_base = 10.0
            descuento = 0.0

            # Aplicar descuentos
            if dia_semana.lower() == "miercoles":
                descuento += 0.2  # 20% descuento
            if edad >= 65:
                descuento += 0.3  # 30% descuento

            precio_final = precio_base * (1 - descuento)
            asiento.set_precio(precio_final)
            asiento.reservar()
        else:
            raise ValueError(f"Asiento {numero} en fila {fila} no encontrado.")

    def cancelar_reserva(self, numero, fila):
        """
        Cancela la reserva de un asiento.

        Args:
            numero (int): Número del asiento.
            fila (int): Fila del asiento.
        """
        asiento = self.buscar_asiento(numero, fila)
        if asiento:
            asiento.cancelar_reserva()
        else:
            raise ValueError(f"Asiento {numero} en fila {fila} no encontrado.")

    def mostrar_asientos(self):
        """
        Muestra todos los asientos en la sala.
        """
        for asiento in self.__asientos:
            print(asiento)

    def buscar_asiento(self, numero, fila):
        """
        Busca un asiento por número y fila.

        Args:
            numero (int): Número del asiento.
            fila (int): Fila del asiento.

        Returns:
            Asiento: El asiento encontrado o None.
        """
        for asiento in self.__asientos:
            if asiento.get_numero() == numero and asiento.get_fila() == fila:
                return asiento
        return None


# ------------------- Ejemplo de Uso -------------------

# Crear la sala de cine
sala = SalaCine()

# Agregar asientos
try:
    sala.agregar_asiento(Asiento(1, 1))
    sala.agregar_asiento(Asiento(2, 1))
    sala.agregar_asiento(Asiento(3, 1))
except ValueError as e:
    print(e)

# Mostrar los asientos
print("\n--- Asientos en la sala ---")
sala.mostrar_asientos()

# Reservar un asiento
try:
    sala.reservar_asiento(1, 1, "miercoles", 70)
except ValueError as e:
    print(e)

# Mostrar los asientos después de la reserva
print("\n--- Asientos después de reservar ---")
sala.mostrar_asientos()

# Cancelar una reserva
try:
    sala.cancelar_reserva(1, 1)
except ValueError as e:
    print(e)

# Mostrar los asientos después de cancelar la reserva
print("\n--- Asientos después de cancelar la reserva ---")
sala.mostrar_asientos()

# Ejercicio completado.
