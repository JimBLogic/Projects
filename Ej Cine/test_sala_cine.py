import unittest
from V17ReservaCine import Asiento, SalaCine

class TestAsiento(unittest.TestCase):
    def setUp(self):
        self.asiento = Asiento(1, 1, "lunes")

    def test_getters(self):
        self.assertEqual(self.asiento.get_numero(), 1)
        self.assertEqual(self.asiento.get_fila(), 1)
        self.assertEqual(self.asiento.get_dia_semana(), "lunes")
        self.assertFalse(self.asiento.get_reservado())
        self.assertEqual(self.asiento.get_precio(), 0.0)
        self.assertEqual(self.asiento.get_edad(), 0)
        self.assertEqual(self.asiento.get_descuentos(), [])

    def test_set_precio(self):
        self.asiento.set_precio(15.0)
        self.assertEqual(self.asiento.get_precio(), 15.0)
        self.asiento.reservar()
        with self.assertRaises(ValueError):
            self.asiento.set_precio(20.0)

    def test_set_edad(self):
        self.asiento.set_edad(30)
        self.assertEqual(self.asiento.get_edad(), 30)
        self.asiento.reservar()
        with self.assertRaises(ValueError):
            self.asiento.set_edad(40)

    def test_set_descuentos(self):
        self.asiento.set_descuentos(["10%"])
        self.assertEqual(self.asiento.get_descuentos(), ["10%"])
        self.asiento.reservar()
        with self.assertRaises(ValueError):
            self.asiento.set_descuentos(["20%"])

    def test_reservar(self):
        self.asiento.reservar()
        self.assertTrue(self.asiento.get_reservado())
        with self.assertRaises(ValueError):
            self.asiento.reservar()

    def test_cancelar_reserva(self):
        self.asiento.reservar()
        self.asiento.cancelar_reserva("si")
        self.assertFalse(self.asiento.get_reservado())
        with self.assertRaises(ValueError):
            self.asiento.cancelar_reserva("si")

    def test_to_dict(self):
        self.asiento.set_precio(15.0)
        self.asiento.set_edad(30)
        self.asiento.set_descuentos(["10%"])
        self.asiento.reservar()
        expected_dict = {
            "numero": 1,
            "fila": 1,
            "dia_semana": "lunes",
            "reservado": True,
            "precio": 15.0,
            "edad": 30,
            "descuentos": ["10%"]
        }
        self.assertEqual(self.asiento.to_dict(), expected_dict)

class TestSalaCine(unittest.TestCase):
    def setUp(self):
        self.sala = SalaCine()

    def test_agregar_asiento(self):
        self.sala.agregar_asiento(1, 1, "lunes")
        self.assertEqual(len(self.sala._SalaCine__asientos), 1)
        with self.assertRaises(ValueError):
            self.sala.agregar_asiento(1, 1, "lunes")

    def test_reservar_asiento(self):
        self.sala.agregar_asiento(1, 1, "lunes")
        self.sala.reservar_asiento(1, 1, "lunes", 30)
        asiento = self.sala.buscar_asiento(1, 1, "lunes")
        self.assertTrue(asiento.get_reservado())
        with self.assertRaises(ValueError):
            self.sala.reservar_asiento(1, 1, "lunes", 30)

    def test_cancelar_reserva(self):
        self.sala.agregar_asiento(1, 1, "lunes")
        self.sala.reservar_asiento(1, 1, "lunes", 30)
        self.sala.cancelar_reserva(1, 1, "lunes", "si")
        asiento = self.sala.buscar_asiento(1, 1, "lunes")
        self.assertFalse(asiento.get_reservado())
        with self.assertRaises(ValueError):
            self.sala.cancelar_reserva(1, 1, "lunes", "si")

    def test_mostrar_asientos(self):
        self.sala.agregar_asiento(1, 1, "lunes")
        self.sala.agregar_asiento(2, 1, "lunes")
        self.sala.reservar_asiento(1, 1, "lunes", 30)
        self.sala.mostrar_asientos(filtro_dia="lunes")
        self.sala.mostrar_asientos(filtro_estado="reservado")
        self.sala.mostrar_asientos(filtro_precio=10.0)

    def test_calcular_precio(self):
        precio, descuentos = self.sala.calcular_precio(10.0, "miércoles", 70)
        self.assertEqual(precio, 5.0)
        self.assertEqual(descuentos, ["20% de descuento los miércoles", "30% de descuento para mayores de 65 años"])

if __name__ == "__main__":
    unittest.main()