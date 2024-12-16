import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from proyecto.asiento import Asiento

import unittest

class TestAsiento(unittest.TestCase):
    """
    Clase de prueba para la clase Asiento.
    """

    def test_crear_asiento(self):
        """
        Prueba la creación de un asiento.
        """
        asiento = Asiento(1, "A", False, 10.0)
        self.assertEqual(asiento.get_numero(), 1)
        self.assertEqual(asiento.get_fila(), "A")
        self.assertFalse(asiento.is_reservado())
        self.assertEqual(asiento.get_precio(), 10.0)

    def test_reservar_asiento(self):
        """
        Prueba la reserva de un asiento.
        """
        asiento = Asiento(1, "A", False, 10.0)
        mensaje = asiento.reservar()
        self.assertTrue(asiento.is_reservado())
        self.assertEqual(mensaje, "Asiento reservado correctamente.")

    def test_cancelar_reserva(self):
        """
        Prueba la cancelación de una reserva de asiento.
        """
        asiento = Asiento(1, "A", True, 10.0)
        mensaje = asiento.cancelar()
        self.assertFalse(asiento.is_reservado())
        self.assertEqual(mensaje, "Reserva cancelada correctamente.")

    def test_actualizar_asiento(self):
        """
        Prueba la actualización de un asiento.
        """
        asiento = Asiento(1, "A", False, 10.0)
        mensaje = asiento.actualizar("B", 2)
        self.assertEqual(asiento.get_fila(), "B")
        self.assertEqual(asiento.get_numero(), 2)
        self.assertEqual(mensaje, "Asiento actualizado correctamente.")

    def test_asiento_to_dict(self):
        """
        Prueba la conversión de un asiento a un diccionario.
        """
        asiento = Asiento(1, "A", False, 10.0)
        asiento_dict = asiento.to_dict()
        self.assertEqual(asiento_dict, {
            "numero": 1,
            "fila": "A",
            "reservado": False,
            "precio": 10.0
        })

    def test_asiento_from_dict(self):
        """
        Prueba la creación de un asiento a partir de un diccionario.
        """
        data = {
            "numero": 1,
            "fila": "A",
            "reservado": False,
            "precio": 10.0
        }
        asiento = Asiento.from_dict(data)
        self.assertEqual(asiento.get_numero(), 1)
        self.assertEqual(asiento.get_fila(), "A")
        self.assertFalse(asiento.is_reservado())
        self.assertEqual(asiento.get_precio(), 10.0)

if __name__ == "__main__":
    unittest.main()