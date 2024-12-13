import unittest
from asiento import Asiento
from mensajes import Mensajes

class TestAsiento(unittest.TestCase):
    """
    Clase de pruebas para la clase Asiento.
    """

    def test_reservar_asiento_libre(self):
        """
        Prueba la reserva de un asiento libre.
        """
        asiento = Asiento("A", 1)
        mensaje = asiento.reservar()
        self.assertEqual(mensaje, Mensajes.asiento_reservado())
        self.assertEqual(asiento.estado, "reservado")

    def test_reservar_asiento_reservado(self):
        """
        Prueba la reserva de un asiento ya reservado.
        """
        asiento = Asiento("A", 1, "reservado")
        mensaje = asiento.reservar()
        self.assertEqual(mensaje, Mensajes.asiento_ya_reservado())
        self.assertEqual(asiento.estado, "reservado")

    def test_cancelar_reserva_asiento_reservado(self):
        """
        Prueba la cancelación de la reserva de un asiento reservado.
        """
        asiento = Asiento("A", 1, "reservado")
        mensaje = asiento.cancelar()
        self.assertEqual(mensaje, Mensajes.reserva_cancelada())
        self.assertEqual(asiento.estado, "libre")

    def test_cancelar_reserva_asiento_libre(self):
        """
        Prueba la cancelación de la reserva de un asiento libre.
        """
        asiento = Asiento("A", 1)
        mensaje = asiento.cancelar()
        self.assertEqual(mensaje, Mensajes.asiento_no_encontrado())
        self.assertEqual(asiento.estado, "libre")

    def test_to_dict(self):
        """
        Prueba la conversión de un asiento a diccionario.
        """
        asiento = Asiento("A", 1)
        self.assertEqual(asiento.to_dict(), {"fila": "A", "numero": 1, "estado": "libre"})

    def test_from_dict(self):
        """
        Prueba la creación de un asiento desde un diccionario.
        """
        data = {"fila": "A", "numero": 1, "estado": "libre"}
        asiento = Asiento.from_dict(data)
        self.assertEqual(asiento.fila, "A")
        self.assertEqual(asiento.numero, 1)
        self.assertEqual(asiento.estado, "libre")

if __name__ == '__main__':
    unittest.main()