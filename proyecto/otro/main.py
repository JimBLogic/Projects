from sala_cine import SalaCine

def main():
    precio_base = 10.0  # Precio base de una entrada
    sala = SalaCine(precio_base)

    # Agregar algunos asientos
    sala.agregar_asiento(1, "A")
    sala.agregar_asiento(2, "A")
    sala.agregar_asiento(3, "B")

    # Reservar un asiento
    try:
        sala.reservar_asiento(1, "A", 70, "miércoles")  # Asiento con descuento para mayor y día de espectador
    except Exception as e:
        print(e)

    # Mostrar todos los asientos
    sala.mostrar_asientos()

    # Cancelar una reserva
    try:
        sala.cancelar_reserva(1, "A")
    except Exception as e:
        print(e)

    # Mostrar todos los asientos después de cancelar
    sala.mostrar_asientos()

if __name__ == "__main__":
    main()
