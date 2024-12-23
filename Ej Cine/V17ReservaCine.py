import json
import os

class Asiento:
    """
    Clase que representa un asiento en una sala de cine.
    """

    def __init__(self, numero, fila, dia_semana):
        """
        Inicializa un asiento con su número, fila y día de la semana.
        """
        self.__numero = numero
        self.__fila = fila
        self.__dia_semana = dia_semana
        self.__reservado = False
        self.__precio = 0.0
        self.__edad = 0
        self.__descuentos = []

    def get_numero(self):
        """
        Devuelve el número del asiento.
        """
        return self.__numero

    def get_fila(self):
        """
        Devuelve la fila del asiento.
        """
        return self.__fila

    def get_dia_semana(self):
        """
        Devuelve el día de la semana del asiento.
        """
        return self.__dia_semana

    def get_reservado(self):
        """
        Devuelve si el asiento está reservado.
        """
        return self.__reservado

    def get_precio(self):
        """
        Devuelve el precio del asiento.
        """
        return self.__precio

    def get_edad(self):
        """
        Devuelve la edad del espectador que reservó el asiento.
        """
        return self.__edad

    def get_descuentos(self):
        """
        Devuelve los descuentos aplicados al asiento.
        """
        return self.__descuentos

    def set_precio(self, precio):
        """
        Establece el precio del asiento.
        Lanza una excepción si el asiento ya está reservado.
        """
        if self.__reservado:
            raise ValueError("No se puede modificar el precio de un asiento reservado.")
        self.__precio = precio

    def set_edad(self, edad):
        """
        Establece la edad del espectador que reservó el asiento.
        Lanza una excepción si el asiento ya está reservado.
        """
        if self.__reservado:
            raise ValueError("No se puede modificar la edad de un asiento reservado.")
        self.__edad = edad

    def set_descuentos(self, descuentos):
        """
        Establece los descuentos aplicados al asiento.
        Lanza una excepción si el asiento ya está reservado.
        """
        if self.__reservado:
            raise ValueError("No se pueden modificar los descuentos de un asiento reservado.")
        self.__descuentos = descuentos

    def reservar(self):
        """
        Reserva el asiento.
        Lanza una excepción si el asiento ya está reservado.
        """
        if not self.__reservado:
            self.__reservado = True
            return f"Asiento {self.__numero} en fila {self.__fila} reservado."
        else:
            raise ValueError(f"Asiento {self.__numero} en fila {self.__fila} ya está reservado.")

    def cancelar_reserva(self, confirmacion):
        """
        Cancela la reserva del asiento si la confirmación es "si".
        Lanza una excepción si el asiento no está reservado.
        """
        if confirmacion == "si":
            if self.__reservado:
                self.__reservado = False
                return f"Asiento {self.__numero} en fila {self.__fila} ahora está disponible."
            else:
                raise ValueError(f"Asiento {self.__numero} en fila {self.__fila} no está reservado.")
        else:
            return "Cancelación de reserva abortada."

    def __str__(self):
        """
        Devuelve una representación en cadena del asiento.
        """
        estado = "Reservado" if self.__reservado else "Disponible"
        descuentos = ", ".join(self.__descuentos) if self.__descuentos else "Sin descuentos"
        return f"Día: {self.__dia_semana}, Estado: {estado}, Fila: {self.__fila}, Asiento: {self.__numero}, Precio: €{self.__precio:.2f}, Edad: {self.__edad}, Descuentos: {descuentos}"

    def to_dict(self):
        """
        Convierte el asiento a un diccionario.
        """
        return {
            "numero": self.__numero,
            "fila": self.__fila,
            "dia_semana": self.__dia_semana,
            "reservado": self.__reservado,
            "precio": self.__precio,
            "edad": self.__edad,
            "descuentos": self.__descuentos
        }
class SalaCine:
    """
    Clase que representa una sala de cine con múltiples asientos.
    """
    MAX_FILA = 10  # Número máximo de filas en la sala
    MAX_ASIENTO = 20  # Número máximo de asientos por fila

    def __init__(self, precio_base=10.0):
        """
        Inicializa una sala de cine con un precio base para los asientos.
        """
        self.__asientos = []  # Lista de asientos en la sala
        self.__precio_base = precio_base  # Precio base de los asientos

    def agregar_asiento(self, numero, fila, dia_semana):
        """
        Agrega un asiento a la sala de cine.
        Lanza una excepción si el número de fila o asiento está fuera de los límites permitidos,
        o si el asiento ya ha sido agregado para el mismo día.
        """
        if fila > self.MAX_FILA or fila < 1:
            raise ValueError(f"Error: La fila debe estar entre 1 y {self.MAX_FILA}.")
        if numero > self.MAX_ASIENTO or numero < 1:
            raise ValueError(f"Error: El número de asiento debe estar entre 1 y {self.MAX_ASIENTO}.")

        # Verifica si el asiento ya ha sido agregado para el mismo día
        for a in self.__asientos:
            if a.get_numero() == numero and a.get_fila() == fila and a.get_dia_semana() == dia_semana:
                raise ValueError(f"Asiento {numero} en fila {fila} para el día {dia_semana} ya está agregado.")

        # Agrega el nuevo asiento a la lista de asientos
        asiento = Asiento(numero, fila, dia_semana)
        self.__asientos.append(asiento)
        return Mensajes.asiento_agregado(numero, fila, dia_semana)

    def reservar_asiento(self, numero, fila, dia_semana, edad):
        """
        Reserva un asiento en la sala de cine.
        Lanza una excepción si el asiento no ha sido agregado o ya está reservado.
        Calcula el precio final del asiento aplicando descuentos según el día de la semana y la edad del espectador.
        """
        asiento = self.buscar_asiento(numero, fila, dia_semana)
        if asiento is None:
            raise ValueError(Mensajes.error_asiento_no_encontrado(numero, fila, dia_semana))

        if asiento.get_reservado():
            raise ValueError(f"Asiento {numero} en fila {fila} para el día {dia_semana} ya está reservado.")

        # Calcula el precio final y los descuentos aplicados
        precio_final, descuentos_aplicados = self.calcular_precio(self.__precio_base, dia_semana, edad)

        # Establece el precio, la edad y los descuentos del asiento
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
        """
        asiento = self.buscar_asiento(numero, fila, dia_semana)
        if asiento:
            return asiento.cancelar_reserva(confirmacion)
        else:
            raise ValueError(Mensajes.error_asiento_no_encontrado(numero, fila, dia_semana))

    def mostrar_asientos(self, filtro_dia=None, filtro_estado=None, filtro_precio=None):
        """
        Muestra los asientos de la sala de cine, aplicando filtros opcionales por día, estado y precio.
        """
        asientos_filtrados = self.__asientos
        if filtro_dia:
            asientos_filtrados = [a for a in asientos_filtrados if a.get_dia_semana() == filtro_dia]
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
        """
        for asiento in self.__asientos:
            if asiento.get_numero() == numero and asiento.get_fila() == fila and asiento.get_dia_semana() == dia_semana:
                return asiento
        return None

    def hay_asientos_en_dia(self, dia_semana):
        """
        Verifica si hay asientos agregados en un día específico.
        Devuelve True si hay asientos, o False si no los hay.
        """
        for asiento in self.__asientos:
            if asiento.get_dia_semana() == dia_semana:
                return True
        return False

    def to_dict(self):
        """
        Convierte la lista de asientos de la sala de cine a una lista de diccionarios.
        """
        return [asiento.to_dict() for asiento in self.__asientos]

    def from_dict(self, data):
        """
        Carga la lista de asientos de la sala de cine desde una lista de diccionarios.
        """
        self.__asientos = [Asiento(a["numero"], a["fila"], a["dia_semana"]) for a in data]
        for asiento, a in zip(self.__asientos, data):
            asiento.set_precio(a["precio"])
            asiento.set_edad(a["edad"])
            asiento.set_descuentos(a["descuentos"])
            if a["reservado"]:
                asiento.reservar()

    def calcular_precio(self, precio_base, dia_semana, edad):
        """
        Calcula el precio final de un asiento aplicando descuentos según el día de la semana y la edad del espectador.
        Devuelve el precio final y una lista de descuentos aplicados.
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
    """
    with open("estado_sala.json", "w") as file:
        json.dump(sala.to_dict(), file)
    print(Mensajes.estado_guardado())

def cargar_estado():
    """
    Carga el estado de la sala de cine desde un archivo JSON.
    Si el archivo no existe o está corrupto, se inicia una nueva sala.
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
    if os.path.exists("estado_sala.json"):
        os.remove("estado_sala.json")
    print(Mensajes.estado_reseteado())

def validar_entrada(mensaje, tipo=int, rango=None):
    """
    Valida la entrada del usuario asegurándose de que sea del tipo y rango especificados.
    """
    while True:
        try:
            entrada = tipo(input(mensaje))
            if rango and (entrada < rango[0] or entrada > rango[1]):
                raise ValueError
            return entrada
        except ValueError:
            print(f"Entrada inválida. Por favor, ingrese un {tipo.__name__} válido.")

def validar_opcion(mensaje, opciones_validas):
    """
    Valida que la opción ingresada por el usuario esté dentro de las opciones válidas.
    """
    while True:
        entrada = input(mensaje).strip().lower()
        if entrada in opciones_validas:
            return entrada
        print(f"Opción inválida. Las opciones válidas son: {', '.join(opciones_validas)}.")

def agregar_asientos_en_rango(sala, dias, filas, numeros):
    """
    Agrega múltiples asientos a la sala de cine en los días, filas y números especificados.
    """
    for dia in dias:
        for fila in filas:
            for numero in numeros:
                try:
                    mensaje = sala.agregar_asiento(numero, fila, dia)
                    print(mensaje)
                except ValueError as e:
                    print(f"Error: {e}")

def simulador_precios(precio_base, dia_semana, edad):
    """
    Simula el precio de un asiento aplicando descuentos según el día de la semana y la edad del espectador.
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

def reporte_disponibilidad(sala):
    """
    Genera un reporte de la disponibilidad de asientos por día.
    """
    dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    reporte = {dia: 0 for dia in dias_semana}

    for asiento in sala.to_dict():
        if not asiento["reservado"]:
            reporte[asiento["dia_semana"]] += 1

    for dia, disponibles in reporte.items():
        print(f"{dia.capitalize()}: {disponibles} asientos disponibles")

class Mensajes:
    """
    Clase para centralizar los mensajes al usuario.
    """
    @staticmethod
    def error_asiento_no_encontrado(numero, fila, dia):
        return f"Error: El asiento {numero} en fila {fila} para el día {dia} no existe."

    @staticmethod
    def asiento_reservado(numero, fila):
        return f"Asiento {numero} en fila {fila} reservado correctamente."

    @staticmethod
    def asiento_agregado(numero, fila, dia):
        return f"Asiento {numero} en fila {fila} para el día {dia} agregado correctamente."

    @staticmethod
    def no_hay_asientos(dia):
        return f"Error: No hay asientos agregados para el día {dia}."

    @staticmethod
    def estado_guardado():
        return "Estado guardado correctamente."

    @staticmethod
    def estado_cargado():
        return "Estado cargado correctamente."

    @staticmethod
    def estado_no_encontrado():
        return "No se encontró un estado guardado. Se iniciará una nueva sala."

    @staticmethod
    def estado_error_carga(e):
        return f"Error al cargar el estado: {e}. Se iniciará una nueva sala."

    @staticmethod
    def estado_reseteado():
        return "Estado reseteado correctamente."

    @staticmethod
    def cancelacion_reserva_abortada():
        return "Cancelación de reserva abortada."

    @staticmethod
    def precio_final(precio):
        return f"Precio final: €{precio:.2f}"

    @staticmethod
    def descuentos_aplicados(descuentos):
        return f"Descuentos aplicados: {', '.join(descuentos)}"
def main():
    """
    Función principal que maneja la interacción con el usuario.
    """
    sala = cargar_estado()
    print("¡Bienvenido al Sistema de Reservas para un Cine!")
    print("Las filas van del 1 al 10 y los asientos de cada fila van del 1 al 20.")
    print("Recuerda que los miércoles hay un 20% de descuento y los mayores de 65 años tienen un 30% de descuento adicional.")

    while True:
        print("\nOpciones:")
        print("1. Agregar asiento")
        print("2. Reservar asiento")
        print("3. Cancelar reserva")
        print("4. Mostrar todos los asientos")
        print("5. Simular precio de un asiento")
        print("6. Generar reporte de disponibilidad")
        print("7. Salir")
        print("8. Reset")

        opcion = validar_entrada("Seleccione una opción (1-8): ", int, (1, 8))

        try:
            if opcion == 1:
                print("Opciones para agregar asiento:")
                print("1. Agregar asiento individual")
                print("2. Agregar fila completa")
                print("3. Agregar todos los asientos de un día")
                print("4. Agregar todos los asientos de toda la semana")
                sub_opcion = validar_entrada("Seleccione una opción (1-4): ", int, (1, 4))

                dia_semana = validar_opcion("Ingrese el día de la semana: ", ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"])
                fila = validar_entrada("Fila del asiento (1-10): ", int, (1, 10))
                numero = validar_entrada("Número del asiento (1-20): ", int, (1, 20))

                opciones_agregar = {
                    1: ([dia_semana], [fila], [numero]),
                    2: ([dia_semana], [fila], range(1, 21)),
                    3: ([dia_semana], range(1, 11), range(1, 21)),
                    4: (["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"], range(1, 11), range(1, 21)),
                }
                dias, filas, numeros = opciones_agregar[sub_opcion]
                agregar_asientos_en_rango(sala, dias, filas, numeros)

            elif opcion == 2:
                dia_semana = validar_opcion("Ingrese el día de la semana: ", ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"])

                if not sala.hay_asientos_en_dia(dia_semana):
                    print(f"Error: No hay asientos agregados para el día {dia_semana}.")
                    continue

                fila = validar_entrada("Fila del asiento (1-10): ", int, (1, 10))
                numero = validar_entrada("Número del asiento (1-20): ", int, (1, 20))
                edad = validar_entrada("Edad del espectador (1-120): ", int, (1, 120))

                if sala.buscar_asiento(numero, fila, dia_semana) is None:
                    print(Mensajes.error_asiento_no_encontrado(numero, fila, dia_semana))
                else:
                    sala.reservar_asiento(numero, fila, dia_semana, edad)

            elif opcion == 3:
                dia_semana = validar_opcion("Ingrese el día de la semana: ", ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"])

                if not sala.hay_asientos_en_dia(dia_semana):
                    print(f"Error: No hay asientos agregados para el día {dia_semana}.")
                    continue

                fila = validar_entrada("Fila del asiento (1-10): ", int, (1, 10))
                numero = validar_entrada("Número del asiento (1-20): ", int, (1, 20))
                confirmacion = validar_opcion(f"¿Está seguro de que desea cancelar la reserva del asiento {numero} en fila {fila} para el día {dia_semana}? (si/no): ", ["si", "no"])

                if sala.buscar_asiento(numero, fila, dia_semana) is None:
                    print(Mensajes.error_asiento_no_encontrado(numero, fila, dia_semana))
                else:
                    sala.cancelar_reserva(numero, fila, dia_semana, confirmacion)

            elif opcion == 4:
                print("Opciones para mostrar asientos:")
                print("1. Mostrar todos los asientos")
                print("2. Mostrar asientos por día de la semana")
                print("3. Mostrar asientos por estado (reservado/disponible)")
                sub_opcion = validar_entrada("Seleccione una opción (1-3): ", int, (1, 3))

                if sub_opcion == 1:
                    sala.mostrar_asientos()
                elif sub_opcion == 2:
                    dia_semana = validar_opcion("Ingrese el día de la semana: ", ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"])
                    sala.mostrar_asientos(filtro_dia=dia_semana)
                elif sub_opcion == 3:
                    estado = validar_opcion("Ingrese el estado (reservado/disponible): ", ["reservado", "disponible"])
                    sala.mostrar_asientos(filtro_estado=estado)

            elif opcion == 5:
                dia_semana = validar_opcion("Ingrese el día de la semana: ", ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"])
                edad = validar_entrada("Edad del espectador (1-120): ", int, (1, 120))
                precio_final, descuentos_aplicados = simulador_precios(sala.__precio_base, dia_semana, edad)
                print(Mensajes.precio_final(precio_final))
                if descuentos_aplicados:
                    print(Mensajes.descuentos_aplicados(descuentos_aplicados))

            elif opcion == 6:
                reporte_disponibilidad(sala)

            elif opcion == 7:
                guardar = validar_opcion("¿Desea guardar el estado actual del programa? (si/no): ", ["si", "no"])
                if guardar == "si":
                    guardar_estado(sala)
                else:
                    print("Estado no guardado. Volviendo al menú principal.")
                print("¡Gracias por usar el sistema! Hasta luego.")
                break

            elif opcion == 8:
                reset = validar_opcion("¿Desea resetear el estado actual del programa? (si/no): ", ["si", "no"])
                if reset == "si":
                    sala = reset_estado()
                else:
                    print("Estado no reseteado. Volviendo al menú principal.")

        except ValueError as e:
            print(f"Error: {e}")

        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()