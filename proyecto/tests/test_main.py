import unittest
from unittest.mock import patch
from main import main
from tests.test_setup import reset_estado_sala

class TestMain(unittest.TestCase):

    def setUp(self):
        reset_estado_sala()

    @patch('builtins.input', side_effect=['1', '1', '1', '1', 'lunes', '5'])
    @patch('builtins.print')
    def test_agregar_asiento(self, mock_print, mock_input):
        main()
        mock_print.assert_any_call("Asiento agregado correctamente.")

    @patch('builtins.input', side_effect=['2', '1', '1', '70', '1', 'lunes', '5'])
    @patch('builtins.print')
    def test_reservar_asiento(self, mock_print, mock_input):
        main()
        mock_print.assert_any_call("Asiento reservado correctamente.")

    @patch('builtins.input', side_effect=['3', '1', '1', '1', 'lunes', '5'])
    @patch('builtins.print')
    def test_cancelar_reserva(self, mock_print, mock_input):
        main()
        mock_print.assert_any_call("Reserva cancelada correctamente.")

    @patch('builtins.input', side_effect=['4', '5'])
    @patch('builtins.print')
    def test_mostrar_asientos(self, mock_print, mock_input):
        main()
        mock_print.assert_any_call("Asiento 1 en fila 1 para el día lunes agregado.")

    @patch('builtins.input', side_effect=['5', '5'])
    @patch('builtins.print')
    def test_salir(self, mock_print, mock_input):
        main()
        mock_print.assert_any_call("Saliendo del sistema...")

    @patch('builtins.input', side_effect=['6', '1', '1', '70', '1', 'lunes', '5', '5', '5'])
    @patch('builtins.print')
    def test_simular_precio(self, mock_print, mock_input):
        main()
        mock_print.assert_any_call("Precio final: €7.00")

    @patch('builtins.input', side_effect=['7', '5'])
    @patch('builtins.print')
    def test_reporte_disponibilidad(self, mock_print, mock_input):
        main()
        mock_print.assert_any_call("lunes: 1 asientos disponibles")

    @patch('builtins.input', side_effect=['8', '5'])
    @patch('builtins.print')
    def test_reset_estado(self, mock_print, mock_input):
        main()
        mock_print.assert_any_call("Estado reseteado correctamente.")

if __name__ == '__main__':
    unittest.main()