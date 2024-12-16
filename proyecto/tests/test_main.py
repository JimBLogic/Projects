import unittest
from unittest.mock import patch, MagicMock
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from proyecto.main import main
from proyecto.mensajes import Mensajes as Messages
from tests.test_setup import reset_estado_sala
import logging

# Configurar el logger
logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s - %(message)s')

class TestMain(unittest.TestCase):
    """
    Clase de pruebas para la función principal del programa.
    """

    def setUp(self):
        """
        Configuración inicial para los tests.
        """
        reset_estado_sala()

    @patch('builtins.input', side_effect=['1', '2', '3', '4', '5', '6', '7'])
    def test_agregar_asiento(self, mock_input):
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_any_call(Messages.asiento_agregado())

    @patch('builtins.input', side_effect=['1', '2', '3', '4', '5', '6', '7'])
    def test_reservar_asiento(self, mock_input):
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_any_call(Messages.asiento_reservado())

    @patch('builtins.input', side_effect=['1', '2', '3', '4', '5', '6'])
    def test_cancelar_reserva(self, mock_input):
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_any_call(Messages.reserva_cancelada())

    @patch('builtins.input', side_effect=['1', '2', '3', '4', '5', '6'])
    def test_mostrar_asientos(self, mock_input):
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_any_call({'fila': 'A', 'numero': 1, 'estado': 'libre', 'precio': 10.0})

    @patch('builtins.input', side_effect=['1', '2', '3', '4', '5', '6', '7'])
    def test_actualizar_asiento(self, mock_input):
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_any_call(Messages.asiento_actualizado())

    @patch('builtins.input', side_effect=['1', '2', '3', '4', '5', '6', '7'])
    def test_eliminar_asiento(self, mock_input):
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_any_call(Messages.asiento_eliminado())

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['1', '2', '3', '4', '5', '6', '7'])
    def test_reporte_disponibilidad(self, mock_input, mock_print):
        main()
        mock_print.assert_any_call(Messages.reporte_disponibilidad("lunes", 1, 0, 99))

    @patch('builtins.input', side_effect=['1', '2', '3', '4', '5', '6', '7'])
    def test_reset_estado(self, mock_input):
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_any_call(Messages.estado_reseteado())

if __name__ == '__main__':
    unittest.main()