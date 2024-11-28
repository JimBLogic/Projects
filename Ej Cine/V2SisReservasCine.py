# Sistema de Reservas para un Cine con Tarifas Especiales

class Asiento:
    """
    Clase para representar un asiento en la sala de cine.
    """

    def __init__(self, numero, fila):
        """
        Inicializa un asiento con su número y fila.

        Args:
            numero (int): Número del asiento.
            fila (int): Fila del asiento.
        """
        self.__numero = numero
        self.__fila = fila
        self.__reservado = False
        self.__precio = 0.0

    # Métodos getter para acceder a los atributos privados
    def get_numero(self):
        return self.__numero

    def get_fila(self):
        return self.__fila

    def get_reservado(self):
        return self.__reservado

    def get_precio(self):
        return self.__precio

    # Setter para actualizar el precio
    def set_precio(self, precio):
        self.__precio = precio

    def reservar(self):
        if not self.__reservado:
            self.__reservado = True
            print(f"Asiento {self.__numero} en fila {self.__fila} reservado.")
        else:
            raise ValueError(f"Asiento {self.__numero} en fila {self.__fila} ya está reservado.")

    def cancelar_reserva(self):
        if self.__reservado:
            self.__reservado = False
            print(f"Asiento {self.__numero} en fila {self.__fila} ahora está disponible.")
        else:
            raise ValueError(f"Asiento {self.__numero} en fila {self.__fila} no está reservado.")

    def __str__(self):
        estado = "Reservado" if self.__reservado else "Disponible"
        return f"Asiento {self.__numero}, Fila {self.__fila}, Precio: ${self.__precio:.2f}, Estado: {estado}"


class SalaCine:
    """
    Clase para administrar una sala de cine con múltiples asientos.
    """

    MAX_FILA = 10  # Limite de filas
    MAX_ASIENTO = 20  # Limite de asientos por fila

    def __init__(self):
        self.__asientos = []  # Lista para almacenar los objetos Asiento.

    def agregar_asiento(self, asiento):
        """
        Añade un asiento si no existe ya en la sala.

        Args:
            asiento (Asiento): El asiento a agregar.
        """
        # Validación de que el asiento y fila estén dentro de los límites
        if asiento.get_fila() > self.MAX_FILA or asiento.get_fila() < 1:
            raise ValueError(f"Error: La fila debe estar entre 1 y {self.MAX_FILA}.")
        if asiento.get_numero() > self.MAX_ASIENTO or asiento.get_numero() < 1:
            raise ValueError(f"Error: El número de asiento debe estar entre 1 y {self.MAX_ASIENTO}.")

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
            edad (int): Edad del cliente.
        """
        asiento = self.buscar_asiento(numero, fila)
        if asiento:
            precio_base = 10.0  # Precio base.
            descuento = 0.0

            # Validación del día de la semana
            dias_validos = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
            if dia_semana.lower() not in dias_validos:
                raise ValueError("Error: El día de la semana debe ser uno de los siguientes: (lunes, martes, miércoles, jueves, viernes, sábado, domingo).")

            # Aplicar descuentos según las condiciones
            if dia_semana.lower() == "miercoles":
                descuento += 0.2  # 20% de descuento los miércoles.
            if edad >= 65:
                descuento += 0.3  # 30% de descuento para mayores de 65 años.

            precio_final = precio_base * (1 - descuento)
            asiento.set_precio(precio_final)
            asiento.reservar()
        else:
            raise ValueError(f"Asiento {numero} en fila {fila} no encontrado.")

    def cancelar_reserva(self, numero, fila):
        """
        Cancela la reserva de un asiento.
        """
        asiento = self.buscar_asiento(numero, fila)
        if asiento:
            asiento.cancelar_reserva()
        else:
            raise ValueError(f"Asiento {numero} en fila {fila} no encontrado.")

    def mostrar_asientos(self):
        """
        Lista todos los asientos con su estado actual.
        """
        if len(self.__asientos) == 0:
            print("No hay asientos disponibles aún.")
        for asiento in self.__asientos:
            print(asiento)

    def buscar_asiento(self, numero, fila):
        """
        Busca un asiento en la lista por su número y fila.

        Returns:
            Asiento o None si no se encuentra.
        """
        for asiento in self.__asientos:
            if asiento.get_numero() == numero and asiento.get_fila() == fila:
                return asiento
        return None


# Interfaz de usuario para probar todas las funcionalidades
def main():
    sala = SalaCine()
    print("¡Bienvenido al Sistema de Reservas para un Cine!")
    print("Las filas van del 1 al 10 y los asientos de cada fila van del 1 al 20.")
    print("Recuerda que los miércoles hay un 20% de descuento y los mayores de 65 años tienen un 30% de descuento adicional.")

    while True:
        print("\nOpciones:")
        print("1. Agregar asiento")
        print("2. Reservar asiento")
        print("3. Cancelar reserva")
        print("4. Mostrar todos los asientos")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        try:
            if opcion == "1":
                try:
                    numero = int(input("Número del asiento (1-20): "))
                    fila = int(input("Fila del asiento (1-10): "))
                    asiento = Asiento(numero, fila)
                    sala.agregar_asiento(asiento)
                    print(f"Asiento {numero} en fila {fila} agregado correctamente.")
                except ValueError:
                    print("Error: Entrada inválida. Asegúrese de ingresar números válidos para el asiento y la fila.")

            elif opcion == "2":
                try:
                    numero = int(input("Número del asiento (1-20): "))
                    fila = int(input("Fila del asiento (1-10): "))
                    dia_semana = input("Día de la semana (lunes, martes, miércoles, jueves, viernes, sábado, domingo): ").strip()
                    edad = int(input("Edad del espectador: "))
                    sala.reservar_asiento(numero, fila, dia_semana, edad)
                except ValueError:
                    print("Error: Entrada inválida. Asegúrese de ingresar datos correctos.")

            elif opcion == "3":
                try:
                    numero = int(input("Número del asiento (1-20): "))
                    fila = int(input("Fila del asiento (1-10): "))
                    sala.cancelar_reserva(numero, fila)
                except ValueError:
                    print("Error: Entrada inválida. Asegúrese de ingresar números válidos para el asiento y la fila.")

            elif opcion == "4":
                print("\n--- Estado de los asientos ---")
                sala.mostrar_asientos()

            elif opcion == "5":
                print("¡Gracias por usar el sistema! Hasta luego.")
                break

            else:
                print("Opción no válida, intente nuevamente.")

        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()