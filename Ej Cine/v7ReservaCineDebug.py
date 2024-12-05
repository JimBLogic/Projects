import json
import logging

# Configuración del registro de depuración
logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# El estado de la sala de cine se guardará en un archivo .json solo si se selecciona la opción de guardar al salir.

# Sistema de Reservas para un Cine con Tarifas Especiales

class Asiento:
    """
    Clase para representar un asiento en la sala de cine.
    """

    def __init__(self, numero, fila):
        # Inicialización de los atributos del asiento
        self.__numero = numero
        self.__fila = fila
        self.__reservado = False
        self.__precio = 0.0
        self.__dia_semana = ""
        self.__edad = 0
        self.__descuentos = []

    # Getters para acceder a los atributos privados
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

    # Setters para modificar los atributos privados
    def set_precio(self, precio):
        self.__precio = precio

    def set_dia_semana(self, dia_semana):
        self.__dia_semana = dia_semana.lower()

    def set_edad(self, edad):
        self.__edad = edad

    def set_descuentos(self, descuentos):
        self.__descuentos = descuentos

    # Método para reservar un asiento
    def reservar(self):
        if not self.__reservado:
            self.__reservado = True
            logging.info(f"Asiento {self.__numero} en fila {self.__fila} reservado.")
        else:
            raise ValueError(f"Asiento {self.__numero} en fila {self.__fila} ya está reservado.")

    # Método para cancelar la reserva de un asiento
    def cancelar_reserva(self):
        if self.__reservado:
            self.__reservado = False
            logging.info(f"Asiento {self.__numero} en fila {self.__fila} ahora está disponible.")
        else:
            raise ValueError(f"Asiento {self.__numero} en fila {self.__fila} no está reservado.")

    # Método para representar el estado del asiento como cadena
    def __str__(self):
        estado = "Reservado" if self.__reservado else "Disponible"
        descuentos = ", ".join(self.__descuentos) if self.__descuentos else "Sin descuentos"
        return f"Asiento {self.__numero}, Fila {self.__fila}, Precio: ${self.__precio:.2f}, Estado: {estado}, Día: {self.__dia_semana}, Edad: {self.__edad}, Descuentos: {descuentos}"

    # Método para convertir el estado del asiento a un diccionario
    def to_dict(self):
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

    MAX_FILA = 10
    MAX_ASIENTO = 20

    def __init__(self):
        # Inicialización de la lista de asientos
        self.__asientos = []

    # Método para agregar un asiento a la sala
    def agregar_asiento(self, numero, fila):
        # Reflexión: Es importante validar que el número de fila y asiento estén dentro de los límites permitidos.
        if fila > self.MAX_FILA or fila < 1:
            raise ValueError(f"Error: La fila debe estar entre 1 y {self.MAX_FILA}.")
        if numero > self.MAX_ASIENTO or numero < 1:
            raise ValueError(f"Error: El número de asiento debe estar entre 1 y {self.MAX_ASIENTO}.")

        # Reflexión: Verificar si el asiento ya ha sido agregado para evitar duplicaciones.
        for a in self.__asientos:
            if a.get_numero() == numero and a.get_fila() == fila:
                logging.warning(f"Asiento {numero} en fila {fila} ya está agregado.")
                confirmar = input("¿Desea reemplazarlo? (si/no): ").strip().lower()
                if confirmar == "si":
                    self.__asientos.remove(a)
                    break
                else:
                    logging.info("Asignación cancelada. Puede agregar otro asiento.")
                    return

        asiento = Asiento(numero, fila)
        self.__asientos.append(asiento)
        logging.info(f"Asiento {numero} en fila {fila} agregado correctamente.")

    # Método para reservar un asiento en la sala
    def reservar_asiento(self, numero, fila, dia_semana, edad):
        dia_semana = dia_semana.lower()
        dias_validos = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        # Reflexión: Validar que el día de la semana sea correcto.
        if dia_semana not in dias_validos:
            raise ValueError("Error: El día de la semana debe ser uno de los siguientes: (lunes, martes, miércoles, jueves, viernes, sábado, domingo).")

        asiento = self.buscar_asiento(numero, fila)
        # Reflexión: No se puede reservar un asiento que no ha sido agregado.
        if asiento is None:
            raise ValueError(f"Asiento {numero} en fila {fila} no está agregado.")

        # Reflexión: No se puede reservar un asiento que ya está reservado.
        if asiento.get_reservado():
            raise ValueError(f"Asiento {numero} en fila {fila} ya está reservado.")

        precio_base = 10.0
        descuento = 0.0
        descuentos_aplicados = []

        # Reflexión: Aplicar descuento del 20% los miércoles a todos los espectadores.
        if dia_semana == "miércoles":
            descuento += 0.2
            descuentos_aplicados.append("20% de descuento los miércoles")

        # Reflexión: Aplicar descuento adicional del 30% a personas mayores de 65 años (edad mayor a 65).
        if edad > 65:
            descuento += 0.3
            descuentos_aplicados.append("30% de descuento para mayores de 65 años")

        # Aplicar los descuentos en el orden correcto
        precio_final = precio_base * (1 - 0.3) if edad > 65 else precio_base
        precio_final *= (1 - 0.2) if dia_semana == "miércoles" else 1

        asiento.set_precio(precio_final)
        asiento.set_dia_semana(dia_semana)
        asiento.set_edad(edad)
        asiento.set_descuentos(descuentos_aplicados)
        asiento.reservar()

        logging.info(f"Descuentos aplicados: {', '.join(descuentos_aplicados)}")
        logging.info(f"Precio final: ${precio_final:.2f}")

    # Método para cancelar la reserva de un asiento
    def cancelar_reserva(self, numero, fila):
        asiento = self.buscar_asiento(numero, fila)
        # Reflexión: Solo se puede cancelar la reserva de un asiento que está reservado.
        if asiento:
            if not asiento.get_reservado():
                raise ValueError(f"Asiento {numero} en fila {fila} no está reservado.")
            asiento.cancelar_reserva()
            logging.info(f"Reserva del asiento {numero} en fila {fila} cancelada correctamente.")
        else:
            raise ValueError(f"Asiento {numero} en fila {fila} no encontrado.")

    # Método para mostrar todos los asientos en la sala
    def mostrar_asientos(self):
        if len(self.__asientos) == 0:
            logging.info("No hay asientos disponibles aún.")
        for asiento in self.__asientos:
            logging.info(asiento)

    # Método para buscar un asiento en la sala
    def buscar_asiento(self, numero, fila):
        for asiento in self.__asientos:
            if asiento.get_numero() == numero and asiento.get_fila() == fila:
                return asiento
        return None

    # Método para convertir el estado de la sala a un diccionario
    def to_dict(self):
        return [asiento.to_dict() for asiento in self.__asientos]

    # Método para restaurar el estado de la sala desde un diccionario
    def from_dict(self, data):
        self.__asientos = [Asiento(a["numero"], a["fila"]) for a in data]
        for asiento, a in zip(self.__asientos, data):
            if a["reservado"]:
                asiento.reservar()
            asiento.set_precio(a["precio"])
            asiento.set_dia_semana(a["dia_semana"].lower())
            asiento.set_edad(a["edad"])
            asiento.set_descuentos(a["descuentos"])

# Función para guardar el estado de la sala en un archivo JSON
def guardar_estado(sala):
    with open("estado_sala.json", "w") as file:
        json.dump(sala.to_dict(), file)
    logging.info("Estado guardado correctamente.")

# Función para cargar el estado de la sala desde un archivo JSON
def cargar_estado():
    try:
        with open("estado_sala.json", "r") as file:
            data = json.load(file)
            sala = SalaCine()
            sala.from_dict(data)
            logging.info("Estado cargado correctamente.")
            return sala
    except FileNotFoundError:
        logging.warning("No se encontró un estado guardado previamente.")
        return SalaCine()

# Función para resetear el estado de la sala
def reset_estado():
    logging.info("Estado reseteado correctamente.")
    return SalaCine()

# Interfaz de usuario para interactuar con el sistema de reservas
def main():
    sala = cargar_estado()
    print("¡Bienvenido al Sistema de Reservas para un Cine!")
    print("Las filas van del 1 al 10 y los asientos de cada fila van del 1 al 20.")
    print("Recuerda que los miércoles hay un 20% de descuento y los mayores de 65 años tienen un 30% de descuento adicional.")
    print("Por favor, seleccione el día de la semana utilizando los números del 1 al 7.")

    dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

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
                while True:
                    try:
                        print("\nSeleccione el día de la semana:")
                        for i, dia in enumerate(dias_semana, 1):
                            print(f"{i}. {dia.capitalize()}")
                        dia_opcion = int(input("Ingrese el número del día de la semana (1-7): "))
                        if dia_opcion < 1 or dia_opcion > 7:
                            raise ValueError("Error: Selección inválida. Debe ser un número entre 1 y 7.")
                        dia_semana = dias_semana[dia_opcion - 1]
                        break
                    except ValueError as e:
                        print(f"Error: {e}. Por favor, intente nuevamente.")

                while True:
                    try:
                        edad = int(input("Edad del espectador (1-100): "))
                        if edad < 1 or edad > 100:
                            raise ValueError("Error: La edad debe estar entre 1 y 100.")
                        break
                    except ValueError as e:
                        print(f"Error: {e}. Por favor, intente nuevamente.")

                while True:
                    try:
                        filas_disponibles = [f"Fila {j}" for j in range(1, 11) if any(not sala.buscar_asiento(i, j) for i in range(1, 21))]
                        if not filas_disponibles:
                            print(f"No hay filas disponibles para el día {dia_semana}. Volviendo al menú principal.")
                            break

                        print(f"Filas disponibles para el día {dia_semana}: {', '.join(filas_disponibles)}")
                        fila = int(input("Fila del asiento (1-10): "))
                        if fila < 1 or fila > 10:
                            raise ValueError(f"Error: La fila debe estar entre 1 y 10.")
                        asientos_disponibles = [f"Asiento {i}" for i in range(1, 21) if not sala.buscar_asiento(i, fila)]
                        if not asientos_disponibles:
                            print(f"No hay asientos disponibles en la fila {fila} para el día {dia_semana}.")
                            continue
                        print(f"Asientos disponibles en la fila {fila} para el día {dia_semana}: {', '.join(asientos_disponibles)}")
                        numero = int(input("Número del asiento (1-20): "))
                        if numero < 1 or numero > 20:
                            raise ValueError(f"Error: El número de asiento debe estar entre 1 y 20.")
                        if sala.buscar_asiento(numero, fila):
                            print(f"Error: Asiento {numero} en fila {fila} ya está ocupado.")
                            continue
                        break
                    except ValueError as e:
                        print(f"Error: {e}. Por favor, intente nuevamente.")

                try:
                    if opcion == "1":
                        sala.agregar_asiento(numero, fila)
                    elif opcion == "2":
                        sala.reservar_asiento(numero, fila, dia_semana, edad)
                    print(f"Operación realizada correctamente.")
                except ValueError as e:
                    print(f"Error: {e}. Por favor, intente nuevamente.")

            elif opcion == "3":
                if len(sala._SalaCine__asientos) == 0:
                    print("No hay reservas para cancelar. Volviendo al menú principal.")
                    continue
                while True:
                    try:
                        print("\nSeleccione el día de la semana:")
                        for i, dia in enumerate(dias_semana, 1):
                            print(f"{i}. {dia.capitalize()}")
                        dia_opcion = int(input("Ingrese el número del día de la semana (1-7): "))
                        if dia_opcion < 1 or dia_opcion > 7:
                            raise ValueError("Error: Selección inválida. Debe ser un número entre 1 y 7.")
                        dia_semana = dias_semana[dia_opcion - 1]
                        break
                    except ValueError as e:
                        print(f"Error: {e}. Por favor, intente nuevamente.")

                while True:
                    try:
                        numero = int(input("Número del asiento (1-20): "))
                        if numero < 1 or numero > 20:
                            raise ValueError(f"Error: El número de asiento debe estar entre 1 y 20.")
                        fila = int(input("Fila del asiento (1-10): "))
                        if fila < 1 or fila > 10:
                            raise ValueError(f"Error: La fila debe estar entre 1 y 10.")
                        sala.cancelar_reserva(numero, fila)
                        print(f"Reserva del asiento {numero} en fila {fila} cancelada correctamente.")
                        break
                    except ValueError as e:
                        print(f"Error: {e}. Por favor, intente nuevamente.")
                    except Exception as e:
                        print(f"Error: No se encontró la reserva para cancelar. Volviendo al menú principal.")
                        break

            elif opcion == "4":
                print("\n--- Estado de los asientos ---")
                sala.mostrar_asientos()

            elif opcion == "5":
                guardar = input("¿Desea guardar el estado actual del programa? (si/no): ").strip().lower()
                if guardar == "si":
                    guardar_estado(sala)
                else:
                    print("Estado no guardado. Volviendo al estado inicial.")
                print("¡Gracias por usar el sistema! Hasta luego.")
                break

            elif opcion == "6":
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
            logging.error(f"Error: {e}")

if __name__ == "__main__":
    main()