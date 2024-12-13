import unittest
from unittest.mock import patch
from main import main
from mensajes import Mensajes
from tests.test_setup import reset_estado_sala
import logging

# Configurar el logger
logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class TestMain(unittest.TestCase):
    """
    Clase de pruebas para la función principal del programa.
    """

    def setUp(self):
        """
        Configuración inicial para los tests.
        """
        reset_estado_sala()

    @patch('builtins.input', side_effect=['1', 'lunes', 'A', '1', '7'])
    @patch('builtins.print')
    def test_agregar_asiento(self, mock_print, mock_input):
        """
        Prueba la opción de agregar asiento en el menú principal.
        """
        main()
        mock_print.assert_any_call(Mensajes.asiento_agregado())
        mock_print.assert_any_call("Estado actual: {'fila': 'A', 'numero': 1, 'estado': 'libre'}")

    @patch('builtins.input', side_effect=['2', 'lunes', 'A', '1', '7'])
    @patch('builtins.print')
    def test_reservar_asiento(self, mock_print, mock_input):
        """
        Prueba la opción de reservar asiento en el menú principal.
        """
        main()
        mock_print.assert_any_call(Mensajes.asiento_reservado())
        mock_print.assert_any_call("Estado actual: {'fila': 'A', 'numero': 1, 'estado': 'reservado'}")

    @patch('builtins.input', side_effect=['3', 'lunes', 'A', '1', '7'])
    @patch('builtins.print')
    def test_cancelar_reserva(self, mock_print, mock_input):
        """
        Prueba la opción de cancelar reserva en el menú principal.
        """
        main()
        mock_print.assert_any_call(Mensajes.reserva_cancelada())
        mock_print.assert_any_call("Estado actual: {'fila': 'A', 'numero': 1, 'estado': 'libre'}")

    @patch('builtins.input', side_effect=['4', 'lunes', '7'])
    @patch('builtins.print')
    def test_mostrar_asientos(self, mock_print, mock_input):
        """
        Prueba la opción de mostrar asientos en el menú principal.
        """
        main()
        mock_print.assert_any_call({'fila': 'A', 'numero': 1, 'estado': 'libre'})

    @patch('builtins.input', side_effect=['5', '7'])
    @patch('builtins.print')
    def test_reporte_disponibilidad(self, mock_print, mock_input):
        """
        Prueba la opción de generar reporte de disponibilidad en el menú principal.
        """
        main()
        mock_print.assert_any_call(Mensajes.reporte_disponibilidad("lunes", 1, 0))

    @patch('builtins.input', side_effect=['6', '7'])
    @patch('builtins.print')
    def test_reset_estado(self, mock_print, mock_input):
        """
        Prueba la opción de resetear estado en el menú principal.
        """
        main()
        mock_print.assert_any_call(Mensajes.estado_reseteado())
        mock_print.assert_any_call("Estado actual: {}")

    @patch('builtins.input', side_effect=['7'])
    @patch('builtins.print')
    def test_salir(self, mock_print, mock_input):
        """
        Prueba la opción de salir del sistema en el menú principal.
        """
        main()
        mock_print.assert_any_call(Mensajes.saliendo_sistema())

    @patch('builtins.input', side_effect=['8'])
    @patch('builtins.print')
    def test_opcion_invalida(self, mock_print, mock_input):
        """
        Prueba la opción inválida en el menú principal.
        """
        main()
        mock_print.assert_any_call(Mensajes.opcion_invalida())

if __name__ == '__main__':
    unittest.main()