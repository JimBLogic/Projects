import json
import os

class Asiento:
    def __init__(self, numero, fila, dia_semana):
        self.__numero = numero
        self.__fila = fila
        self.__dia_semana = dia_semana
        self.__reservado = False
        self.__precio = 0.0
        self.__edad = 0
        self.__descuentos = []

    def get_numero(self):
        return self.__numero

    def get_fila(self):
        return self.__fila

    def get_dia_semana(self):
        return self.__dia_semana

    def get_reservado(self):
        return self.__reservado

    def get_precio(self):
        return self.__precio

    def get_edad(self):
        return self.__edad

    def get_descuentos(self):
        return self.__descuentos

    def set_precio(self, precio):
        if self.__reservado:
            raise ValueError("No se puede modificar el precio de un asiento reservado.")
        self.__precio = precio

    def set_edad(self, edad):
        if self.__reservado:
            raise ValueError("No se puede modificar la edad de un asiento reservado.")
        self.__edad = edad

    def set_descuentos(self, descuentos):
        if self.__reservado:
            raise ValueError("No se pueden modificar los descuentos de un asiento reservado.")
        self.__descuentos = descuentos

    def reservar(self):
        if not self.__reservado:
            self.__reservado = True
            print(f"Asiento {self.__numero} en fila {self.__fila} reservado.")
        else:
            raise ValueError(f"Asiento {self.__numero} en fila {self.__fila} ya está reservado.")

    def cancelar_reserva(self, confirmacion):
        if confirmacion == "si":
            if self.__reservado:
                self.__reservado = False
                print(f"Asiento {self.__numero} en fila {self.__fila} ahora está disponible.")
            else:
                raise ValueError(f"Asiento {self.__numero} en fila {self.__fila} no está reservado.")
        else:
            print("Cancelación de reserva abortada.")

    def __str__(self):
        estado = "Reservado" if self.__reservado else "Disponible"
        descuentos = ", ".join(self.__descuentos) if self.__descuentos else "Sin descuentos"
        return f"Día: {self.__dia_semana}, Estado: {estado}, Fila: {self.__fila}, Asiento: {self.__numero}, Precio: €{self.__precio:.2f}, Edad: {self.__edad}, Descuentos: {descuentos}"

    def to_dict(self):
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
    MAX_FILA = 10
    MAX_ASIENTO = 20

    def __init__(self, precio_base=10.0):
        self.__asientos = []
        self.__precio_base = precio_base

    def agregar_asiento(self, numero, fila, dia_semana):
        if fila > self.MAX_FILA or fila < 1:
            raise ValueError(f"Error: La fila debe estar entre 1 y {self.MAX_FILA}.")
        if numero > self.MAX_ASIENTO or numero < 1:
            raise ValueError(f"Error: El número de asiento debe estar entre 1 y {self.MAX_ASIENTO}.")

        for a in self.__asientos:
            if a.get_numero() == numero and a.get_fila() == fila and a.get_dia_semana() == dia_semana:
                raise ValueError(f"Asiento {numero} en fila {fila} para el día {dia_semana} ya está agregado.")

        asiento = Asiento(numero, fila, dia_semana)
        self.__asientos.append(asiento)
        print(f"Asiento {numero} en fila {fila} para el día {dia_semana} agregado correctamente.")

    def reservar_asiento(self, numero, fila, dia_semana, edad):
        asiento = self.buscar_asiento(numero, fila, dia_semana)
        if asiento is None:
            raise ValueError(f"Asiento {numero} en fila {fila} para el día {dia_semana} no está agregado.")

        if asiento.get_reservado():
            raise ValueError(f"Asiento {numero} en fila {fila} para el día {dia_semana} ya está reservado.")

        descuento = 0.0
        descuentos_aplicados = []

        if dia_semana == "miércoles":
            descuento += 0.2
            descuentos_aplicados.append("20% de descuento los miércoles")

        if edad > 65:
            descuento += 0.3
            descuentos_aplicados.append("30% de descuento para mayores de 65 años")

        precio_final = self.__precio_base * (1 - descuento)

        asiento.set_precio(precio_final)
        asiento.set_edad(edad)
        asiento.set_descuentos(descuentos_aplicados)
        asiento.reservar()

        if descuentos_aplicados:
            print(f"Descuentos aplicados: {', '.join(descuentos_aplicados)}")
        print(f"Precio final: €{precio_final:.2f}")

    def cancelar_reserva(self, numero, fila, dia_semana, confirmacion):
        asiento = self.buscar_asiento(numero, fila, dia_semana)
        if asiento:
            asiento.cancelar_reserva(confirmacion)
        else:
            raise ValueError(f"Asiento {numero} en fila {fila} para el día {dia_semana} no encontrado.")

    def mostrar_asientos(self, filtro_dia=None, filtro_estado=None):
        if len(self.__asientos) == 0:
            print("No hay asientos disponibles aún.")
        else:
            dias_ordenados = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
            asientos_ordenados = sorted(self.__asientos, key=lambda x: (dias_ordenados.index(x.get_dia_semana()), x.get_fila(), x.get_numero()))
            for asiento in asientos_ordenados:
                if (filtro_dia is None or asiento.get_dia_semana() == filtro_dia) and (filtro_estado is None or (filtro_estado == "reservado" and asiento.get_reservado()) or (filtro_estado == "disponible" and not asiento.get_reservado())):
                    print(asiento)

    def buscar_asiento(self, numero, fila, dia_semana):
        for asiento in self.__asientos:
            if asiento.get_numero() == numero and asiento.get_fila() == fila and asiento.get_dia_semana() == dia_semana:
                return asiento
        return None

    def hay_asientos_en_dia(self, dia_semana):
        for asiento in self.__asientos:
            if asiento.get_dia_semana() == dia_semana:
                return True
        return False

    def to_dict(self):
        return [asiento.to_dict() for asiento in self.__asientos]

    def from_dict(self, data):
        self.__asientos = [Asiento(a["numero"], a["fila"], a["dia_semana"]) for a in data]
        for asiento, a in zip(self.__asientos, data):
            asiento.set_precio(a["precio"])
            asiento.set_edad(a["edad"])
            asiento.set_descuentos(a["descuentos"])
            if a["reservado"]:
                asiento.reservar()

def guardar_estado(sala):
    with open("estado_sala.json", "w") as file:
        json.dump(sala.to_dict(), file)
    print("Estado guardado correctamente.")

def cargar_estado():
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
    except json.JSONDecodeError:
        print("Error al cargar el estado: el archivo JSON está corrupto.")
        return SalaCine()

def reset_estado():
    if os.path.exists("estado_sala.json"):
        os.remove("estado_sala.json")
    print("Estado reseteado correctamente.")
    return SalaCine()

def validar_entrada(mensaje, tipo=int, rango=None):
    while True:
        try:
            entrada = tipo(input(mensaje))
            if rango and (entrada < rango[0] or entrada > rango[1]):
                raise ValueError
            return entrada
        except ValueError:
            print(f"Entrada inválida. Por favor, ingrese un {tipo.__name__} válido.")

def validar_dia_semana(mensaje):
    dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    while True:
        dia = input(mensaje).strip().lower()
        if dia in dias_semana:
            return dia
        else:
            print("Día de la semana inválido. Por favor, ingrese un día válido (lunes, martes, miércoles, jueves, viernes, sábado, domingo).")

def agregar_varios_asientos(sala, dias, filas, numeros):
    errores = 0
    for dia in dias:
        for fila in filas:
            for numero in numeros:
                try:
                    sala.agregar_asiento(numero, fila, dia)
                except ValueError as e:
                    print(f"Error: {e}.")
                    errores += 1
    if errores > 0:
        print(f"Se encontraron {errores} errores al agregar los asientos.")

def main():
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
        print("5. Salir")
        print("6. Reset")

        opcion = validar_entrada("Seleccione una opción (1-6): ", int, (1, 6))

        try:
            if opcion == 1:
                print("Opciones para agregar asiento:")
                print("1. Agregar asiento individual")
                print("2. Agregar fila completa")
                print("3. Agregar todos los asientos de un día")
                print("4. Agregar todos los asientos de toda la semana")
                sub_opcion = validar_entrada("Seleccione una opción (1-4): ", int, (1, 4))

                if sub_opcion == 1:
                    dia_semana = validar_dia_semana("Ingrese el día de la semana: ")
                    fila = validar_entrada("Fila del asiento (1-10): ", int, (1, 10))
                    numero = validar_entrada("Número del asiento (1-20): ", int, (1, 20))
                    try:
                        sala.agregar_asiento(numero, fila, dia_semana)
                    except ValueError as e:
                        print(f"Error: {e}. Por favor, intente nuevamente.")

                elif sub_opcion == 2:
                    dia_semana = validar_dia_semana("Ingrese el día de la semana: ")
                    fila = validar_entrada("Fila del asiento (1-10): ", int, (1, 10))
                    agregar_varios_asientos(sala, [dia_semana], range(1, 11), range(1, 21))

                elif sub_opcion == 3:
                    dia_semana = validar_dia_semana("Ingrese el día de la semana: ")
                    agregar_varios_asientos(sala, [dia_semana], range(1, 11), range(1, 21))

                elif sub_opcion == 4:
                    agregar_varios_asientos(sala, ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"], range(1, 11), range(1, 21))

            elif opcion == 2:
                dia_semana = validar_dia_semana("Ingrese el día de la semana: ")

                if not sala.hay_asientos_en_dia(dia_semana):
                    print(f"Error: No hay asientos agregados para el día {dia_semana}.")
                    continue

                fila = validar_entrada("Fila del asiento (1-10): ", int, (1, 10))
                numero = validar_entrada("Número del asiento (1-20): ", int, (1, 20))
                edad = validar_entrada("Edad del espectador (1-120): ", int, (1, 120))

                if sala.buscar_asiento(numero, fila, dia_semana) is None:
                    print(f"Error: El asiento {numero} en la fila {fila} para el día {dia_semana} no está agregado.")
                else:
                    sala.reservar_asiento(numero, fila, dia_semana, edad)

            elif opcion == 3:
                dia_semana = validar_dia_semana("Ingrese el día de la semana: ")

                if not sala.hay_asientos_en_dia(dia_semana):
                    print(f"Error: No hay asientos agregados para el día {dia_semana}.")
                    continue

                fila = validar_entrada("Fila del asiento (1-10): ", int, (1, 10))
                numero = validar_entrada("Número del asiento (1-20): ", int, (1, 20))
                confirmacion = input(f"¿Está seguro de que desea cancelar la reserva del asiento {numero} en fila {fila} para el día {dia_semana}? (si/no): ").strip().lower()

                if sala.buscar_asiento(numero, fila, dia_semana) is None:
                    print(f"Error: El asiento {numero} en la fila {fila} para el día {dia_semana} no está agregado.")
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
                    dia_semana = validar_dia_semana("Ingrese el día de la semana: ")
                    sala.mostrar_asientos(filtro_dia=dia_semana)
                elif sub_opcion == 3:
                    estado = input("Ingrese el estado (reservado/disponible): ").strip().lower()
                    if estado in ["reservado", "disponible"]:
                        sala.mostrar_asientos(filtro_estado=estado)
                    else:
                        print("Estado inválido. Por favor, ingrese 'reservado' o 'disponible'.")

            elif opcion == 5:
                guardar = input("¿Desea guardar el estado actual del programa? (si/no): ").strip().lower()
                if guardar == "si":
                    guardar_estado(sala)
                else:
                    print("Estado no guardado. Volviendo al menú principal.")
                print("¡Gracias por usar el sistema! Hasta luego.")
                break

            elif opcion == 6:
                reset = input("¿Desea resetear el estado actual del programa? (si/no): ").strip().lower()
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