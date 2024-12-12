import unittest
from asiento import Asiento
from tests.test_setup import reset_estado_sala

class TestAsiento(unittest.TestCase):

    def setUp(self):
        """
        Configuración inicial para los tests.
        """
        reset_estado_sala()
        self.asiento = Asiento(1, 1, "lunes")

    def test_get_numero(self):
        """
        Prueba el método get_numero.
        """
        self.assertEqual(self.asiento.get_numero(), 1)

    def test_get_fila(self):
        """
        Prueba el método get_fila.
        """
        self.assertEqual(self.asiento.get_fila(), 1)

    def test_get_dia_semana(self):
        """
        Prueba el método get_dia_semana.
        """
        self.assertEqual(self.asiento.get_dia_semana(), "lunes")

    def test_get_reservado(self):
        """
        Prueba el método get_reservado.
        """
        self.assertFalse(self.asiento.get_reservado())

    def test_get_precio(self):
        """
        Prueba el método get_precio.
        """
        self.assertEqual(self.asiento.get_precio(), 0.0)

    def test_get_edad(self):
        """
        Prueba el método get_edad.
        """
        self.assertEqual(self.asiento.get_edad(), 0)

    def test_get_descuentos(self):
        """
        Prueba el método get_descuentos.
        """
        self.assertEqual(self.asiento.get_descuentos(), [])

    def test_set_precio(self):
        """
        Prueba el método set_precio.
        """
        self.asiento.set_precio(15.0)
        self.assertEqual(self.asiento.get_precio(), 15.0)
        with self.assertRaises(ValueError):
            self.asiento.reservar()
            self.asiento.set_precio(20.0)

    def test_set_edad(self):
        """
        Prueba el método set_edad.
        """
        self.asiento.set_edad(30)
        self.assertEqual(self.asiento.get_edad(), 30)
        with self.assertRaises(ValueError):
            self.asiento.reservar()
            self.asiento.set_edad(40)

    def test_set_descuentos(self):
        """
        Prueba el método set_descuentos.
        """
        self.asiento.set_descuentos(["20%"])
        self.assertEqual(self.asiento.get_descuentos(), ["20%"])
        with self.assertRaises(ValueError):
            self.asiento.reservar()
            self.asiento.set_descuentos(["30%"])

    def test_reservar(self):
        """
        Prueba el método reservar.
        """
        self.assertEqual(self.asiento.reservar(), "Asiento 1 en fila 1 reservado.")
        with self.assertRaises(ValueError):
            self.asiento.reservar()

    def test_cancelar_reserva(self):
        """
        Prueba el método cancelar_reserva.
        """
        self.asiento.reservar()
        self.assertEqual(self.asiento.cancelar_reserva("si"), "Asiento 1 en fila 1 ahora está disponible.")
        with self.assertRaises(ValueError):
            self.asiento.cancelar_reserva("si")

    def test_to_dict(self):
        """
        Prueba el método to_dict.
        """
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

    def test_from_dict(self):
        """
        Prueba el método from_dict.
        """
        data = {
            "numero": 1,
            "fila": 1,
            "dia_semana": "lunes",
            "reservado": False,
            "precio": 15.0,
            "edad": 30,
            "descuentos": ["20%"]
        }
        asiento = Asiento.from_dict(data)
        self.assertEqual(asiento.get_numero(), 1)
        self.assertEqual(asiento.get_fila(), 1)
        self.assertEqual(asiento.get_dia_semana(), "lunes")
        self.assertFalse(asiento.get_reservado())
        self.assertEqual(asiento.get_precio(), 15.0)
        self.assertEqual(asiento.get_edad(), 30)
        self.assertEqual(asiento.get_descuentos(), ["20%"])

if __name__ == '__main__':
    unittest.main()