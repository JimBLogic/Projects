import unittest
from sala_cine import SalaCine
from tests.test_setup import reset_estado_sala

class TestSalaCine(unittest.TestCase):

    def setUp(self):
        reset_estado_sala()
        self.sala = SalaCine()

    def test_agregar_asiento(self):
        mensaje = self.sala.agregar_asiento(1, 1, "lunes")
        self.assertEqual(mensaje, "Asiento 1 en fila 1 para el día lunes agregado.")
        with self.assertRaises(ValueError):
            self.sala.agregar_asiento(1, 1, "lunes")

    def test_reservar_asiento(self):
        self.sala.agregar_asiento(1, 1, "lunes")
        mensaje = self.sala.reservar_asiento(1, 1, "lunes", 70)
        self.assertEqual(mensaje, "Asiento 1 en fila 1 reservado.")
        with self.assertRaises(ValueError):
            self.sala.reservar_asiento(1, 1, "lunes", 70)

    def test_cancelar_reserva(self):
        self.sala.agregar_asiento(1, 1, "lunes")
        self.sala.reservar_asiento(1, 1, "lunes", 70)
        mensaje = self.sala.cancelar_reserva(1, 1, "lunes", "si")
        self.assertEqual(mensaje, "Asiento 1 en fila 1 ahora está disponible.")
        with self.assertRaises(ValueError):
            self.sala.cancelar_reserva(1, 1, "lunes", "si")

    def test_mostrar_asientos(self):
        self.sala.agregar_asiento(1, 1, "lunes")
        self.sala.mostrar_asientos()

    def test_buscar_asiento(self):
        self.sala.agregar_asiento(1, 1, "lunes")
        asiento = self.sala.buscar_asiento(1, 1, "lunes")
        self.assertIsNotNone(asiento)
        asiento = self.sala.buscar_asiento(2, 1, "lunes")
        self.assertIsNone(asiento)

    def test_hay_asientos_en_dia(self):
        self.sala.agregar_asiento(1, 1, "lunes")
        self.assertTrue(self.sala.hay_asientos_en_dia("lunes"))
        self.assertFalse(self.sala.hay_asientos_en_dia("martes"))

    def test_to_dict(self):
        self.sala.agregar_asiento(1, 1, "lunes")
        asientos_dict = self.sala.to_dict()
        self.assertEqual(len(asientos_dict["lunes"]), 1)

    def test_from_dict(self):
        data = {
            "lunes": [{"numero": 1, "fila": 1, "dia_semana": "lunes", "reservado": False, "precio": 0.0, "edad": 0, "descuentos": []}]
        }
        self.sala.from_dict(data)
        self.assertEqual(len(self.sala.to_dict()["lunes"]), 1)

if __name__ == '__main__':
    unittest.main()