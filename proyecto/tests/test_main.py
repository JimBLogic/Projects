import unittest
from unittest.mock import patch
from main import main
from tests.test_setup import reset_estado_sala
import logging

# Configurar el logger
logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class TestMain(unittest.TestCase):

    def setUp(self):
        """
        Configuración inicial para los tests.
        """
        reset_estado_sala()

    @patch('builtins.input', side_effect=['1', '1', '1', '1', '7'])
    @patch('builtins.print')
    def test_agregar_asiento(self, mock_print, mock_input):
        """
        Prueba la opción de agregar asiento en el menú principal.
        """
        main()
        mock_print.assert_any_call("Asiento agregado correctamente.")

    @patch('builtins.input', side_effect=['2', '1', '1', '1', '30', '7'])
    @patch('builtins.print')
    def test_reservar_asiento(self, mock_print, mock_input):
        """
        Prueba la opción de reservar asiento en el menú principal.
        """
        main()
        mock_print.assert_any_call("Asiento reservado correctamente.")

    @patch('builtins.input', side_effect=['3', '1', '1', '1', '7'])
    @patch('builtins.print')
    def test_cancelar_reserva(self, mock_print, mock_input):
        """
        Prueba la opción de cancelar reserva en el menú principal.
        """
        main()
        mock_print.assert_any_call("Reserva cancelada correctamente.")

    @patch('builtins.input', side_effect=['4', '1', '1', '7'])
    @patch('builtins.print')
    def test_mostrar_asientos(self, mock_print, mock_input):
        """
        Prueba la opción de mostrar asientos en el menú principal.
        """
        main()
        mock_print.assert_any_call("Asiento 1 en fila 1 para el día lunes agregado correctamente.")

    @patch('builtins.input', side_effect=['5', '7'])
    @patch('builtins.print')
    def test_reporte_disponibilidad(self, mock_print, mock_input):
        """
        Prueba la opción de generar reporte de disponibilidad en el menú principal.
        """
        main()
        mock_print.assert_any_call("Lunes: 0 asientos sin agregar, 0 asientos disponibles para reservar")

    @patch('builtins.input', side_effect=['6', '7'])
    @patch('builtins.print')
    def test_reset_estado(self, mock_print, mock_input):
        """
        Prueba la opción de resetear estado en el menú principal.
        """
        main()
        mock_print.assert_any_call("Estado reseteado correctamente. Todos los asientos han sido eliminados.")

    @patch('builtins.input', side_effect=['7', 'si'])
    @patch('builtins.print')
    def test_salir(self, mock_print, mock_input):
        """
        Prueba la opción de salir del sistema en el menú principal.
        """
        main()
        mock_print.assert_any_call("Saliendo del sistema...")

if __name__ == '__main__':
    unittest.main()