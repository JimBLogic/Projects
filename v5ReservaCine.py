import json

# Sistema de Reservas para un Cine con Tarifas Especiales

# Intención:
# Este programa crea un archivo .json en la misma carpeta que el archivo .py.
# El archivo .json se utiliza para guardar el estado de los asientos en la sala de cine.
# Esto permite que los datos se queden registrados, se puedan borrar, añadir o resetear.

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
        self.__dia_semana = ""
        self.__edad = 0
        self.__descuentos = []

    # Métodos getter para acceder a los atributos privados
    def get_numero(self):
        return self.__numero

    def get_fila(self):
        return self.__fila

    def get_reservado(self):
        return self.__reservado

    def get_precio(self):
        return self.__precio

    def get_dia_semana(self):
        return self.__dia_semana

    def get_edad(self):
        return self.__edad

    def get_descuentos(self):
        return self.__descuentos

    # Setter para actualizar el precio
    def set_precio(self, precio):
        self.__precio = precio

    def set_dia_semana(self, dia_semana):
        self.__dia_semana = dia_semana.lower()  # Normalizar a minúsculas

    def set_edad(self, edad):
        self.__edad = edad

    def set_descuentos(self, descuentos):
        self.__descuentos = descuentos

    def reservar(self):
        """
        Cambia el estado del asiento a reservado.
        """
        if not self.__reservado:
            self.__reservado = True
            print(f"Asiento {self.__numero} en fila {self.__fila} reservado.")
        else:
            raise ValueError(f"Asiento {self.__numero} en fila {self.__fila} ya está reservado.")

    def cancelar_reserva(self):
        """
        Cancela la reserva del asiento.
        """
        if self.__reservado:
            self.__reservado = False
            print(f"Asiento {self.__numero} en fila {self.__fila} ahora está disponible.")
        else:
            raise ValueError(f"Asiento {self.__numero} en fila {self.__fila} no está reservado.")

    def __str__(self):
        """
        Devuelve una representación en cadena del estado del asiento.
        """
        estado = "Reservado" if self.__reservado else "Disponible"
        descuentos = ", ".join(self.__descuentos) if self.__descuentos else "Sin descuentos"
        return f"Asiento {self.__numero}, Fila {self.__fila}, Precio: ${self.__precio:.2f}, Estado: {estado}, Día: {self.__dia_semana}, Edad: {self.__edad}, Descuentos: {descuentos}"

    def to_dict(self):
        """
        Convierte el estado del asiento en un diccionario para guardarlo en un archivo JSON.
        """
        return {
            "numero": self.__numero,
            "fila": self.__fila,
            "reservado": self.__reservado,
            "precio": self.__precio,
            "dia_semana": self.__dia_semana,
            "edad": self.__edad,
            "descuentos": self.__descuentos
        }

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

        # Verificar si el asiento ya existe
        for a in self.__asientos:
            if a.get_numero() == asiento.get_numero() and a.get_fila() == asiento.get_fila() and a.get_dia_semana() == asiento.get_dia_semana():
                print(f"Asiento {asiento.get_numero()} en fila {asiento.get_fila()} ya está agregado para el día {asiento.get_dia_semana()}.")
                confirmar = input("¿Desea reemplazarlo? (si/no): ").strip().lower()
                if confirmar == "si":
                    self.__asientos.remove(a)
                    self.__asientos.append(asiento)
                    print(f"Asiento {asiento.get_numero()} en fila {asiento.get_fila()} reemplazado correctamente.")
                    return
                else:
                    print("Asignación cancelada. Puede agregar otro asiento.")
                    return
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
        dia_semana = dia_semana.lower()  # Normalizar a minúsculas
        asiento = self.buscar_asiento(numero, fila, dia_semana)
        if asiento is None:
            raise ValueError(f"Asiento {numero} en fila {fila} no está agregado para el día {dia_semana}.")

        if asiento.get_reservado():
            raise ValueError(f"Asiento {numero} en fila {fila} ya está reservado para el día {dia_semana}.")

        precio_base = 10.0  # Precio base.
        descuento = 0.0
        descuentos_aplicados = []

        # Validación del día de la semana
        dias_validos = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        if dia_semana not in dias_validos:
            raise ValueError("Error: El día de la semana debe ser uno de los siguientes: (lunes, martes, miércoles, jueves, viernes, sábado, domingo).")

        # Aplicar descuentos según las condiciones
        if edad >= 65:
            descuento += 0.3  # 30% de descuento para mayores de 65 años.
            descuentos_aplicados.append("30% de descuento para mayores de 65 años")
        if dia_semana == "miércoles":
            descuento += 0.2  # 20% de descuento los miércoles.
            descuentos_aplicados.append("20% de descuento los miércoles")

        precio_final = precio_base * (1 - descuento)
        asiento.set_precio(precio_final)
        asiento.set_dia_semana(dia_semana)
        asiento.set_edad(edad)
        asiento.set_descuentos(descuentos_aplicados)
        asiento.reservar()

        # Mostrar los descuentos aplicados
        print(f"Descuentos aplicados: {', '.join(descuentos_aplicados)}")
        print(f"Precio final: ${precio_final:.2f}")

    def cancelar_reserva(self, numero, fila, dia_semana):
        """
        Cancela la reserva de un asiento.
        """
        dia_semana = dia_semana.lower()  # Normalizar a minúsculas
        asiento = self.buscar_asiento(numero, fila, dia_semana)
        if asiento:
            if not asiento.get_reservado():
                raise ValueError(f"Asiento {numero} en fila {fila} no está reservado.")
            asiento.cancelar_reserva()
        else:
            raise ValueError(f"Asiento {numero} en fila {fila} no encontrado para el día {dia_semana}.")

    def mostrar_asientos(self):
        """
        Lista todos los asientos con su estado actual.
        """
        if len(self.__asientos) == 0:
            print("No hay asientos disponibles aún.")
        for asiento in self.__asientos:
            print(asiento)

    def buscar_asiento(self, numero, fila, dia_semana=None):
        """
        Busca un asiento en la lista por su número, fila y opcionalmente día de la semana.

        Returns:
            Asiento o None si no se encuentra.
        """
        for asiento in self.__asientos:
            if asiento.get_numero() == numero and asiento.get_fila() == fila:
                if dia_semana is None or asiento.get_dia_semana() == dia_semana:
                    return asiento
        return None

    def to_dict(self):
        """
        Convierte el estado de la sala de cine en un diccionario para guardarlo en un archivo JSON.
        """
        return [asiento.to_dict() for asiento in self.__asientos]

    def from_dict(self, data):
        """
        Restaura el estado de la sala de cine desde un diccionario cargado desde un archivo JSON.
        """
        self.__asientos = [Asiento(a["numero"], a["fila"]) for a in data]
        for asiento, a in zip(self.__asientos, data):
            if a["reservado"]:
                asiento.reservar()
            asiento.set_precio(a["precio"])
            asiento.set_dia_semana(a["dia_semana"].lower())  # Normalizar a minúsculas
            asiento.set_edad(a["edad"])
            asiento.set_descuentos(a["descuentos"])

def guardar_estado(sala):
    """
    Guarda el estado actual de la sala de cine en un archivo JSON.
    """
    with open("estado_sala.json", "w") as file:
        json.dump(sala.to_dict(), file)
    print("Estado guardado correctamente.")

def cargar_estado():
    """
    Carga el estado de la sala de cine desde un archivo JSON si existe.
    """
    try:
        with open("estado_sala.json", "r") as file:
            data = json.load(file)
            sala = SalaCine()
            sala.from_dict(data)
            print("Estado cargado correctamente.")
            return sala
    except FileNotFoundError:
        print("No se encontró un estado guardado previamente.")
        return SalaCine()

def reset_estado():
    """
    Resetea el estado de la sala de cine.
    """
    return SalaCine()

# Aquí comienza el código de la interfaz de usuario para interactuar con el sistema de reservas.

def main():
    sala = cargar_estado()
    print("¡Bienvenido al Sistema de Reservas para un Cine!")
    print("Las filas van del 1 al 10 y los asientos de cada fila van del 1 al 20.")
    print("Recuerda que los miércoles hay un 20% de descuento y los mayores de 65 años tienen un 30% de descuento adicional.")
    print("Por favor, escriba los días de la semana en minúsculas y sin errores gramaticales.")

    while True:
        print("\nOpciones:")
        print("1. Agregar asiento")
        print("2. Reservar asiento")
        print("3. Cancelar reserva")
        print("4. Mostrar todos los asientos")
        print("5. Salir")
        print("6. Reset")

        opcion = input("Seleccione una opción (1-6): ")

        try:
            if opcion == "1" or opcion == "2":
                # Primero se elige el día de la semana
                while True:
                    try:
                        dia_semana = input("Día de la semana (lunes, martes, miércoles, jueves, viernes, sábado, domingo): ").strip().lower()
                        dias_validos = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
                        if dia_semana not in dias_validos:
                            raise ValueError("Error: El día de la semana debe ser uno de los siguientes: (lunes, martes, miércoles, jueves, viernes, sábado, domingo).")
                        break
                    except ValueError as e:
                        print(f"Error: {e}. Por favor, intente nuevamente. Recuerde escribir los días en minúsculas y sin errores gramaticales.")

                # Verificar si hay filas disponibles para el día elegido
                filas_disponibles = [f"Fila {j}" for j in range(1, 11) if any(not sala.buscar_asiento(i, j, dia_semana) for i in range(1, 21))]
                if not filas_disponibles:
                    print(f"No hay filas disponibles para el día {dia_semana}. Volviendo al menú principal.")
                    continue

                print(f"Filas disponibles para el día {dia_semana}: {', '.join(filas_disponibles)}")

                while True:
                    try:
                        fila = int(input("Fila del asiento (1-10): "))
                        if fila < 1 or fila > 10:
                            raise ValueError(f"Error: La fila debe estar entre 1 y 10.")
                        asientos_disponibles = [f"Asiento {i}" for i in range(1, 21) if not sala.buscar_asiento(i, fila, dia_semana)]
                        if not asientos_disponibles:
                            print(f"No hay asientos disponibles en la fila {fila} para el día {dia_semana}.")
                            continue
                        print(f"Asientos disponibles en la fila {fila} para el día {dia_semana}: {', '.join(asientos_disponibles)}")
                        numero = int(input("Número del asiento (1-20): "))
                        if numero < 1 or numero > 20:
                            raise ValueError(f"Error: El número de asiento debe estar entre 1 y 20.")
                        if sala.buscar_asiento(numero, fila, dia_semana):
                            print(f"Error: Asiento {numero} en fila {fila} ya está ocupado para el día {dia_semana}.")
                            continue
                        edad = int(input("Edad del espectador (1-100): "))
                        if edad < 1 or edad > 100:
                            raise ValueError("Error: La edad debe estar entre 1 y 100.")
                        break
                    except ValueError as e:
                        print(f"Error: {e}. Por favor, intente nuevamente.")

                try:
                    if opcion == "1":
                        # Agregar asiento
                        asiento = Asiento(numero, fila)
                        asiento.set_dia_semana(dia_semana)
                        asiento.set_edad(edad)
                        sala.agregar_asiento(asiento)
                    elif opcion == "2":
                        # Reservar asiento
                        sala.reservar_asiento(numero, fila, dia_semana, edad)
                    print(f"Operación realizada correctamente.")
                except ValueError as e:
                    print(f"Error: {e}. Por favor, intente nuevamente.")

            elif opcion == "3":
                # Cancelar reserva: Cancela la reserva de un asiento.
                if len(sala._SalaCine__asientos) == 0:
                    print("No hay reservas para cancelar. Volviendo al menú principal.")
                    continue
                while True:
                    try:
                        dia_semana = input("Día de la semana (lunes, martes, miércoles, jueves, viernes, sábado, domingo): ").strip().lower()
                        dias_validos = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
                        if dia_semana not in dias_validos:
                            raise ValueError("Error: El día de la semana debe ser uno de los siguientes: (lunes, martes, miércoles, jueves, viernes, sábado, domingo).")
                        break
                    except ValueError as e:
                        print(f"Error: {e}. Por favor, intente nuevamente. Recuerde escribir los días en minúsculas y sin errores gramaticales.")

                while True:
                    try:
                        numero = int(input("Número del asiento (1-20): "))
                        if numero < 1 or numero > 20:
                            raise ValueError(f"Error: El número de asiento debe estar entre 1 y 20.")
                        fila = int(input("Fila del asiento (1-10): "))
                        if fila < 1 or fila > 10:
                            raise ValueError(f"Error: La fila debe estar entre 1 y 10.")
                        sala.cancelar_reserva(numero, fila, dia_semana)
                        print(f"Reserva del asiento {numero} en fila {fila} para el día {dia_semana} cancelada correctamente.")
                        break
                    except ValueError as e:
                        print(f"Error: {e}. Por favor, intente nuevamente.")
                    except Exception as e:
                        print(f"Error: No se encontró la reserva para cancelar. Volviendo al menú principal.")
                        break

            elif opcion == "4":
                # Mostrar todos los asientos: Lista todos los asientos con su estado actual.
                print("\n--- Estado de los asientos ---")
                sala.mostrar_asientos()

            elif opcion == "5":
                # Salir: Pregunta si desea guardar el estado actual del programa.
                guardar = input("¿Desea guardar el estado actual del programa? (si/no): ").strip().lower()
                if guardar == "si":
                    guardar_estado(sala)
                else:
                    print("Estado no guardado. Volviendo al estado inicial.")
                print("¡Gracias por usar el sistema! Hasta luego.")
                break

            elif opcion == "6":
                # Reset: Pregunta si desea resetear el estado actual del programa.
                reset = input("¿Desea resetear el estado actual del programa? (si/no): ").strip().lower()
                if reset == "si":
                    sala = reset_estado()
                    print("Estado reseteado correctamente.")
                else:
                    print("Estado no reseteado. Volviendo al menú principal.")

            else:
                print("Opción no válida, intente nuevamente.")

        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()