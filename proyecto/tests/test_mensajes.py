import unittest
from unittest.mock import patch
from mensajes import mostrar_menu, solicitar_datos_asiento, solicitar_datos_reserva, mostrar_mensaje, mostrar_error
from tests.test_setup import reset_estado_sala
import logging

# Configurar el logger
logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class TestMensajes(unittest.TestCase):

    def setUp(self):
        """
        Configuración inicial para los tests.
        """
        reset_estado_sala()

    @patch('builtins.print')
    def test_mostrar_menu(self, mock_print):
        """
        Prueba la función mostrar_menu.
        """
        mostrar_menu()
        mock_print.assert_any_call("\nOpciones:")
        mock_print.assert_any_call("1. Agregar asiento")
        mock_print.assert_any_call("2. Reservar asiento")
        mock_print.assert_any_call("3. Cancelar reserva")
        mock_print.assert_any_call("4. Mostrar todos los asientos")
        mock_print.assert_any_call("5. Generar reporte de disponibilidad")
        mock_print.assert_any_call("6. Resetear estado")
        mock_print.assert_any_call("7. Salir")

    @patch('builtins.input', side_effect=['1', '1'])
    def test_solicitar_datos_asiento(self, mock_input):
        """
        Prueba la función solicitar_datos_asiento.
        """
        numero, fila = solicitar_datos_asiento()
        self.assertEqual(numero, 1)
        self.assertEqual(fila, 1)

    @patch('builtins.input', side_effect=['1', '1', '70', '3'])
    def test_solicitar_datos_reserva(self, mock_input):
        """
        Prueba la función solicitar_datos_reserva.
        """
        numero, fila, edad, dia = solicitar_datos_reserva()
        self.assertEqual(numero, 1)
        self.assertEqual(fila, 1)
        self.assertEqual(edad, 70)
        self.assertEqual(dia, 3)

    @patch('builtins.print')
    def test_mostrar_mensaje(self, mock_print):
        """
        Prueba la función mostrar_mensaje.
        """
        mostrar_mensaje("Mensaje de prueba")
        mock_print.assert_called_with("Mensaje de prueba")

    @patch('builtins.print')
    def test_mostrar_error(self, mock_print):
        """
        Prueba la función mostrar_error.
        """
        mostrar_error("Error de prueba")
        mock_print.assert_called_with("Error: Error de prueba")

if __name__ == '__main__':
    unittest.main()