from asiento import Asiento
from utilidades import calcular_descuento

class SalaCine:
    def __init__(self, precio_base):
        self.__asientos = []
        self.__precio_base = precio_base

    def agregar_asiento(self, numero, fila):
        if any(asiento.numero == numero and asiento.fila == fila for asiento in self.__asientos):
            raise Exception("Este asiento ya está registrado.")
        self.__asientos.append(Asiento(numero, fila, self.__precio_base))

    def reservar_asiento(self, numero, fila, edad, dia):
        asiento = self.buscar_asiento(numero, fila)
        if asiento is None:
            raise Exception("Asiento no encontrado.")
        descuento = calcular_descuento(self.__precio_base, edad, dia)
        asiento.reservar(descuento)

    def cancelar_reserva(self, numero, fila):
        asiento = self.buscar_asiento(numero, fila)
        if asiento is None:
            raise Exception("Asiento no encontrado.")
        asiento.cancelar_reserva()

    def mostrar_asientos(self):
        for asiento in self.__asientos:
            print(asiento)

    def buscar_asiento(self, numero, fila):
        for asiento in self.__asientos:
            if asiento.numero == numero and asiento.fila == fila:
                return asiento
        return None
