import unittest
from unittest.mock import patch
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from proyecto.utilidades import calcular_descuento, validar_entrada, validar_opcion, calcular_precio_final

class TestUtilidades(unittest.TestCase):
    """
    Clase de pruebas para las funciones del módulo utilidades.
    """

    def test_calcular_descuento(self):
        """
        Prueba la función calcular_descuento.
        """
        self.assertEqual(calcular_descuento(10.0, 70, "miércoles"), 0.5)
        self.assertEqual(calcular_descuento(10.0, 30, "miércoles"), 0.0)
        self.assertEqual(calcular_descuento(10.0, 70, "lunes"), 0.3)
        self.assertEqual(calcular_descuento(10.0, 30, "lunes"), 0.0)
        # Edge cases
        self.assertEqual(calcular_descuento(0.0, 70, "miércoles"), 0.5)
        self.assertEqual(calcular_descuento(100.0, 70, "miércoles"), 0.5)
        self.assertEqual(calcular_descuento(10.0, 0, "miércoles"), 0.2)
        self.assertEqual(calcular_descuento(10.0, 70, "domingo"), 0.3)

    @patch('builtins.input', return_value='5')
    def test_validar_entrada(self, mock_input):
        """
        Prueba la función validar_entrada con una entrada válida.
        """
        self.assertEqual(validar_entrada("Ingrese un número: ", int, (1, 10)), 5)

    @patch('builtins.input', return_value='15')
    def test_validar_entrada_fuera_de_rango(self, mock_input):
        """
        Prueba la función validar_entrada con una entrada fuera de rango.
        """
        with self.assertRaises(ValueError):
            validar_entrada("Ingrese un número: ", int, (1, 10))

    @patch('builtins.input', side_effect=['abc', '5'])
    def test_validar_entrada_invalida(self, mock_input):
        """
        Prueba la función validar_entrada con una entrada no válida.
        """
        self.assertEqual(validar_entrada("Ingrese un número: ", int, (1, 10)), 5)

    @patch('builtins.input', return_value='si')
    def test_validar_opcion(self, mock_input):
        """
        Prueba la función validar_opcion con una opción válida.
        """
        self.assertEqual(validar_opcion("Ingrese una opción: ", ['si', 'no']), 'si')

    @patch('builtins.input', return_value='quizás')
    def test_validar_opcion_invalida(self, mock_input):
        """
        Prueba la función validar_opcion con una opción inválida.
        """
        with self.assertRaises(ValueError):
            validar_opcion("Ingrese una opción: ", ['si', 'no'])

    def test_calcular_precio_final(self):
        """
        Prueba la función calcular_precio_final.
        """
        self.assertEqual(calcular_precio_final(10.0, 70, "miércoles"), 5.0)
        self.assertEqual(calcular_precio_final(10.0, 30, "miércoles"), 10.0)
        self.assertEqual(calcular_precio_final(10.0, 70, "lunes"), 7.0)
        self.assertEqual(calcular_precio_final(10.0, 30, "lunes"), 10.0)
        # Edge cases
        self.assertEqual(calcular_precio_final(0.0, 70, "miércoles"), 0.0)
        self.assertEqual(calcular_precio_final(10.0, 0, "miércoles"), 8.0)
        self.assertEqual(calcular_precio_final(10.0, 10, "lunes"), 10.0)
        self.assertEqual(calcular_precio_final(10.0, 70, "domingo"), 7.0)

if __name__ == '__main__':
    unittest.main()