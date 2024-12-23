class Asiento:
    def __init__(self, numero, fila, precio_base):
        self.__numero = numero
        self.__fila = fila
        self.__reservado = False
        self.__precio_base = precio_base
        self.__precio_actual = precio_base

    @property
    def numero(self):
        return self.__numero

    @property
    def fila(self):
        return self.__fila

    @property
    def reservado(self):
        return self.__reservado

    @property
    def precio(self):
        return self.__precio_actual

    def reservar(self, descuento=0):
        if self.__reservado:
            raise Exception("Este asiento ya está reservado.")
        self.__precio_actual = self.__precio_base * (1 - descuento)
        self.__reservado = True

    def cancelar_reserva(self):
        if not self.__reservado:
            raise Exception("Este asiento no está reservado.")
        self.__reservado = False
        self.__precio_actual = self.__precio_base

    def __str__(self):
        estado = "Reservado" if self.__reservado else "Disponible"
        return f"Asiento {self.__numero} en fila {self.__fila}: {estado} - Precio: {self.__precio_actual:.2f}€"
