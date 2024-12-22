import unittest
from unittest.mock import patch
import sys
import os
import logging

# Asegurar que la ruta es correcta
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Verificar la ruta
print(sys.path)

# Importar el módulo
from proyecto.utilidades import calculate_discount, calculate_final_price, validate_input, validate_option

class TestUtilidades(unittest.TestCase):
    """
    Clase de pruebas para las funciones del módulo utilidades.
    """

    def setUp(self):
        """
        Configuración inicial para las pruebas.
        """
        logging.basicConfig(filename='debug.log', level=logging.DEBUG)

    def test_calculate_discount(self):
        """
        Prueba la función calculate_discount.
        """
        self.assertEqual(calculate_discount(100, 25, "lunes"), 0.0)
        self.assertEqual(calculate_discount(100, 65, "miércoles"), 0.5)
        self.assertEqual(calculate_discount(100, 30, "domingo"), 0.0)
        logging.debug('test_calculate_discount passed')

    def test_calculate_final_price(self):
        """
        Prueba la función calculate_final_price.
        """
        self.assertEqual(calculate_final_price(100, 25, "lunes"), 100.0)
        self.assertEqual(calculate_final_price(100, 65, "miércoles"), 50.0)
        self.assertEqual(calculate_final_price(100, 30, "domingo"), 100.0)
        logging.debug('test_calculate_final_price passed')

    @patch('builtins.input', side_effect=['5'])
    def test_validate_input(self, mock_input):
        """
        Prueba la función validate_input.
        """
        self.assertEqual(validate_input("Ingrese un número: ", int, range(1, 6)), 5)
        logging.debug('test_validate_input passed')

    @patch('builtins.input', side_effect=['A', 'B', 'C'])
    def test_validate_input_invalid(self, mock_input):
        """
        Prueba la función validate_input para manejar entradas inválidas.
        """
        with self.assertRaises(ValueError):
            validate_input("Ingrese un número: ", int, range(1, 6))
        logging.debug('test_validate_input_invalid passed')

    @patch('builtins.input', side_effect=StopIteration)
    def test_validate_input_stop_iteration(self, mock_input):
        """
        Prueba la función validate_input para manejar StopIteration.
        """
        with self.assertRaises(ValueError):
            validate_input("Ingrese un número: ", int, range(1, 6))
        logging.debug('test_validate_input_stop_iteration passed')

    @patch('builtins.input', side_effect=['opcion1'])
    def test_validate_option(self, mock_input):
        """
        Prueba la función validate_option.
        """
        self.assertEqual(validate_option("Seleccione una opción: ", ['opcion1', 'opcion2']), 'opcion1')
        logging.debug('test_validate_option passed')

if __name__ == '__main__':
    unittest.main()