import unittest
from asiento import Asiento
from tests.test_setup import reset_estado_sala

class TestAsiento(unittest.TestCase):

    def setUp(self):
        reset_estado_sala()
        self.asiento = Asiento(1, 1, "lunes")

    def test_get_numero(self):
        self.assertEqual(self.asiento.get_numero(), 1)

    def test_get_fila(self):
        self.assertEqual(self.asiento.get_fila(), 1)

    def test_get_dia_semana(self):
        self.assertEqual(self.asiento.get_dia_semana(), "lunes")

    def test_get_reservado(self):
        self.assertFalse(self.asiento.get_reservado())

    def test_get_precio(self):
        self.assertEqual(self.asiento.get_precio(), 0.0)

    def test_get_edad(self):
        self.assertEqual(self.asiento.get_edad(), 0)

    def test_get_descuentos(self):
        self.assertEqual(self.asiento.get_descuentos(), [])

    def test_set_precio(self):
        self.asiento.set_precio(15.0)
        self.assertEqual(self.asiento.get_precio(), 15.0)
        with self.assertRaises(ValueError):
            self.asiento.reservar()
            self.asiento.set_precio(20.0)

    def test_set_edad(self):
        self.asiento.set_edad(30)
        self.assertEqual(self.asiento.get_edad(), 30)
        with self.assertRaises(ValueError):
            self.asiento.reservar()
            self.asiento.set_edad(40)

    def test_set_descuentos(self):
        self.asiento.set_descuentos(["20%"])
        self.assertEqual(self.asiento.get_descuentos(), ["20%"])
        with self.assertRaises(ValueError):
            self.asiento.reservar()
            self.asiento.set_descuentos(["30%"])

    def test_reservar(self):
        self.assertEqual(self.asiento.reservar(), "Asiento 1 en fila 1 reservado.")
        with self.assertRaises(ValueError):
            self.asiento.reservar()

    def test_cancelar_reserva(self):
        self.asiento.reservar()
        self.assertEqual(self.asiento.cancelar_reserva("si"), "Asiento 1 en fila 1 ahora está disponible.")
        with self.assertRaises(ValueError):
            self.asiento.cancelar_reserva("si")

    def test_to_dict(self):
        self.asiento.set_precio(15.0)
        self.asiento.set_edad(30)
        self.asiento.set_descuentos(["20%"])
        expected_dict = {
            "numero": 1,
            "fila": 1,
            "dia_semana": "lunes",
            "reservado": False,
            "precio": 15.0,
            "edad": 30,
            "descuentos": ["20%"]
        }
        self.assertEqual(self.asiento.to_dict(), expected_dict)

if __name__ == '__main__':
    unittest.main()