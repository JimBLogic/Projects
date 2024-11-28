# Sistema de Reservas de Cine
# Este archivo implementa una clase `Asiento` que simula la reserva de asientos en un cine. Incluye lógica básica 
# para calcular precios con descuentos y manejar el estado de reserva. 

class Asiento:
    """
    Representa un asiento en la sala de cine.

    Atributos:
        numero (int): Número del asiento.
        fila (int): Fila del asiento.
        reservado (bool): Estado de la reserva (True si está reservado, False si no).
        precio (float): Precio del asiento.
    """

    def __init__(self, numero, fila):
        """
        Inicializa un nuevo asiento con sus datos básicos.

        Args:
            numero (int): Número del asiento.
            fila (int): Fila del asiento.
        """
        self.numero = numero
        self.fila = fila
        self.reservado = False  # Por defecto, el asiento no está reservado.
        self.precio = 0.0  # El precio será calculado según el día y la edad del cliente.

    def reservar(self):
        """
        Reserva el asiento si está disponible.
        """
        if not self.reservado:
            self.reservado = True
            print(f"Asiento {self.numero} en fila {self.fila} reservado.")
        else:
            print(f"Asiento {self.numero} en fila {self.fila} ya está reservado.")

    def calcular_precio(self, dia_semana, edad):
        """
        Calcula el precio del asiento considerando descuentos por día de la semana o edad.

        Args:
            dia_semana (str): Día de la semana.
            edad (int): Edad del cliente.
        """
        precio_base = 10.0  # Precio base de la entrada.

        if dia_semana.lower() == "miercoles":
            # Los miércoles hay un 20% de descuento.
            self.precio = precio_base * 0.8
        elif edad >= 65:
            # Los mayores de 65 años tienen un 10% de descuento.
            self.precio = precio_base * 0.9
        else:
            # Sin descuentos adicionales.
            self.precio = precio_base

    def __str__(self):
        """
        Representación en cadena del asiento.

        Returns:
            str: Detalles del asiento.
        """
        return f"Asiento {self.numero} en fila {self.fila}, Precio: {self.precio:.2f}, Reservado: {self.reservado}"


# ------------------- Ejemplo de Uso -------------------

# Creamos un asiento en la fila 5, número 10.
mi_asiento = Asiento(10, 5)

# Mostramos su estado inicial.
print(mi_asiento)

# Calculamos su precio para un miércoles y un cliente de 30 años.
mi_asiento.calcular_precio("miercoles", 30)
print(mi_asiento)

# Reservamos el asiento.
mi_asiento.reservar()
print(mi_asiento)

# Intentamos reservar el asiento nuevamente.
mi_asiento.reservar()
print(mi_asiento)

# ------------------- Fin del Ejemplo -------------------

# En este ejemplo, el código demuestra:
# 1. Cómo inicializar un asiento.
# 2. Cómo calcular su precio considerando descuentos.
# 3. Cómo manejar la lógica de reserva, evitando reservas duplicadas.
