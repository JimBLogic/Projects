import unittest
from unittest.mock import patch
from utilidades import calcular_descuento, validar_entrada, validar_opcion, agregar_asientos_en_rango, simulador_precios, reporte_disponibilidad
from sala_cine import SalaCine
from tests.test_setup import reset_estado_sala

class TestUtilidades(unittest.TestCase):

    def setUp(self):
        reset_estado_sala()
        self.sala = SalaCine()

    def test_calcular_descuento(self):
        self.assertEqual(calcular_descuento(10.0, 70, "miércoles"), 0.5)
        self.assertEqual(calcular_descuento(10.0, 30, "miércoles"), 0.2)
        self.assertEqual(calcular_descuento(10.0, 70, "lunes"), 0.3)
        self.assertEqual(calcular_descuento(10.0, 30, "lunes"), 0.0)

    @patch('builtins.input', return_value='5')
    def test_validar_entrada(self, mock_input):
        self.assertEqual(validar_entrada("Ingrese un número: ", int, (1, 10)), 5)

    @patch('builtins.input', return_value='15')
    def test_validar_entrada_fuera_de_rango(self, mock_input):
        with self.assertRaises(ValueError):
            validar_entrada("Ingrese un número: ", int, (1, 10))

    @patch('builtins.input', return_value='si')
    def test_validar_opcion(self, mock_input):
        self.assertEqual(validar_opcion("Ingrese una opción: ", ['si', 'no']), 'si')

    @patch('builtins.input', return_value='quizás')
    def test_validar_opcion_invalida(self, mock_input):
        with self.assertRaises(ValueError):
            validar_opcion("Ingrese una opción: ", ['si', 'no'])

    @patch('builtins.print')
    def test_agregar_asientos_en_rango(self, mock_print):
        dias = ["lunes", "martes"]
        filas = [1, 2]
        numeros = [1, 2]
        agregar_asientos_en_rango(self.sala, dias, filas, numeros)
        self.assertEqual(len(self.sala.to_dict()["lunes"]), 4)
        self.assertEqual(len(self.sala.to_dict()["martes"]), 4)

    @patch('builtins.print')
    def test_simulador_precios(self, mock_print):
        precio_final, descuentos_aplicados = simulador_precios(10.0, "miércoles", 70)
        self.assertEqual(precio_final, 5.0)
        self.assertIn("20% de descuento los miércoles", descuentos_aplicados)
        self.assertIn("30% de descuento para mayores de 65 años", descuentos_aplicados)

    @patch('builtins.print')
    def test_reporte_disponibilidad(self, mock_print):
        self.sala.agregar_asiento(1, 1, "lunes")
        self.sala.agregar_asiento(2, 1, "lunes")
        self.sala.reservar_asiento(1, 1, "lunes", 30)
        reporte_disponibilidad(self.sala)
        mock_print.assert_any_call("Lunes: 1 asientos disponibles")

if __name__ == '__main__':
    unittest.main()