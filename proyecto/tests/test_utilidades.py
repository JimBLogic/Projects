import unittest
from unittest.mock import patch
from utilidades import calcular_descuento, validar_entrada, validar_opcion, agregar_asientos_en_rango, reporte_disponibilidad
from sala_cine import SalaCine
from tests.test_setup import reset_estado_sala
import logging

# Configurar el logger
logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class TestUtilidades(unittest.TestCase):

    def setUp(self):
        """
        Configuración inicial para los tests.
        """
        reset_estado_sala()
        self.sala = SalaCine()

    def test_calcular_descuento(self):
        """
        Prueba la función calcular_descuento.
        """
        try:
            self.assertEqual(calcular_descuento(10.0, 70, "miércoles"), 0.5)
            self.assertEqual(calcular_descuento(10.0, 30, "miércoles"), 0.2)
            self.assertEqual(calcular_descuento(10.0, 70, "lunes"), 0.3)
            self.assertEqual(calcular_descuento(10.0, 30, "lunes"), 0.0)
        except AssertionError as e:
            logging.debug(f"Error en test_calcular_descuento: {e}")
            raise

    @patch('builtins.input', return_value='5')
    def test_validar_entrada(self, mock_input):
        """
        Prueba la función validar_entrada con una entrada válida.
        """
        try:
            self.assertEqual(validar_entrada("Ingrese un número: ", int, (1, 10)), 5)
        except AssertionError as e:
            logging.debug(f"Error en test_validar_entrada: {e}")
            raise

    @patch('builtins.input', return_value='15')
    def test_validar_entrada_fuera_de_rango(self, mock_input):
        """
        Prueba la función validar_entrada con una entrada fuera de rango.
        """
        with self.assertRaises(ValueError):
            try:
                validar_entrada("Ingrese un número: ", int, (1, 10))
            except ValueError as e:
                logging.debug(f"Error en test_validar_entrada_fuera_de_rango: {e}")
                raise

    @patch('builtins.input', return_value='si')
    def test_validar_opcion(self, mock_input):
        """
        Prueba la función validar_opcion con una opción válida.
        """
        try:
            self.assertEqual(validar_opcion("Ingrese una opción: ", ['si', 'no']), 'si')
        except AssertionError as e:
            logging.debug(f"Error en test_validar_opcion: {e}")
            raise

    @patch('builtins.input', return_value='quizás')
    def test_validar_opcion_invalida(self, mock_input):
        """
        Prueba la función validar_opcion con una opción inválida.
        """
        with self.assertRaises(ValueError):
            try:
                validar_opcion("Ingrese una opción: ", ['si', 'no'])
            except ValueError as e:
                logging.debug(f"Error en test_validar_opcion_invalida: {e}")
                raise

    @patch('builtins.print')
    def test_agregar_asientos_en_rango(self, mock_print):
        """
        Prueba la función agregar_asientos_en_rango.
        """
        try:
            dias = ["lunes", "martes"]
            filas = [1, 2]
            numeros = [1, 2]
            agregar_asientos_en_rango(self.sala, dias, filas, numeros)
            self.assertEqual(len(self.sala.to_dict()["lunes"]), 4)
            self.assertEqual(len(self.sala.to_dict()["martes"]), 4)
        except AssertionError as e:
            logging.debug(f"Error en test_agregar_asientos_en_rango: {e}")
            raise

    @patch('builtins.print')
    def test_reporte_disponibilidad(self, mock_print):
        """
        Prueba la función reporte_disponibilidad.
        """
        try:
            self.sala.agregar_asiento(1, 1, "lunes")
            self.sala.agregar_asiento(2, 1, "lunes")
            self.sala.reservar_asiento(1, 1, "lunes", 30)
            reporte_disponibilidad(self.sala)
            mock_print.assert_any_call("Lunes: 1 asientos sin agregar, 1 asientos disponibles para reservar")
        except AssertionError as e:
            logging.debug(f"Error en test_reporte_disponibilidad: {e}")
            raise

if __name__ == '__main__':
    unittest.main()