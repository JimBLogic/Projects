import unittest
from unittest.mock import patch
import v7ReservaCineDebug

class TestReservaCine(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '3', '66', '10', '20'])
    @patch('builtins.print')
    def test_agregar_asiento_valido(self, mock_print, mock_input):
        v7ReservaCineDebug.main()
        mock_print.assert_any_call("Operación realizada correctamente.")

    @patch('builtins.input', side_effect=['1', '3', '66', '10', '20', '1', '3', '66', '10', '20'])
    @patch('builtins.print')
    def test_agregar_asiento_existente(self, mock_print, mock_input):
        v7ReservaCineDebug.main()
        mock_print.assert_any_call("Error: Asiento 20 en fila 10 ya está ocupado.")

    @patch('builtins.input', side_effect=['1', '3', '66', '11', '20'])
    @patch('builtins.print')
    def test_agregar_asiento_fila_invalida(self, mock_print, mock_input):
        v7ReservaCineDebug.main()
        mock_print.assert_any_call("Error: La fila debe estar entre 1 y 10.")

    @patch('builtins.input', side_effect=['2', '3', '66', '10', '20'])
    @patch('builtins.print')
    def test_reservar_asiento_valido(self, mock_print, mock_input):
        v7ReservaCineDebug.main()
        mock_print.assert_any_call("Operación realizada correctamente.")

    @patch('builtins.input', side_effect=['2', '3', '66', '10', '20'])
    @patch('builtins.print')
    def test_reservar_asiento_no_agregado(self, mock_print, mock_input):
        v7ReservaCineDebug.main()
        mock_print.assert_any_call("Error: Asiento 20 en fila 10 no está agregado.")

    @patch('builtins.input', side_effect=['1', '3', '66', '10', '20', '2', '3', '66', '10', '20'])
    @patch('builtins.print')
    def test_reservar_asiento_ya_reservado(self, mock_print, mock_input):
        v7ReservaCineDebug.main()
        mock_print.assert_any_call("Error: Asiento 20 en fila 10 ya está reservado.")

    @patch('builtins.input', side_effect=['3', '3', '10', '20'])
    @patch('builtins.print')
    def test_cancelar_reserva_asiento_reservado(self, mock_print, mock_input):
        v7ReservaCineDebug.main()
        mock_print.assert_any_call("Reserva del asiento 20 en fila 10 cancelada correctamente.")

    @patch('builtins.input', side_effect=['3', '3', '10', '20'])
    @patch('builtins.print')
    def test_cancelar_reserva_asiento_no_reservado(self, mock_print, mock_input):
        v7ReservaCineDebug.main()
        mock_print.assert_any_call("Error: Asiento 20 en fila 10 no está reservado.")

    @patch('builtins.input', side_effect=['3', '3', '10', '20'])
    @patch('builtins.print')
    def test_cancelar_reserva_asiento_no_agregado(self, mock_print, mock_input):
        v7ReservaCineDebug.main()
        mock_print.assert_any_call("Error: Asiento 20 en fila 10 no encontrado.")

    @patch('builtins.input', side_effect=['4'])
    @patch('builtins.print')
    def test_mostrar_asientos_no_agregados(self, mock_print, mock_input):
        v7ReservaCineDebug.main()
        mock_print.assert_any_call("No hay asientos disponibles aún.")

    @patch('builtins.input', side_effect=['1', '3', '66', '10', '20', '4'])
    @patch('builtins.print')
    def test_mostrar_asientos_agregados(self, mock_print, mock_input):
        v7ReservaCineDebug.main()
        mock_print.assert_any_call("Asiento 20, Fila 10, Precio: $0.00, Estado: Disponible, Día: , Edad: 0, Descuentos: Sin descuentos")

    @patch('builtins.input', side_effect=['5', 'si'])
    @patch('builtins.print')
    def test_guardar_estado(self, mock_print, mock_input):
        v7ReservaCineDebug.main()
        mock_print.assert_any_call("Estado guardado correctamente.")

    @patch('builtins.input', side_effect=['6', 'si'])
    @patch('builtins.print')
    def test_resetear_estado(self, mock_print, mock_input):
        v7ReservaCineDebug.main()
        mock_print.assert_any_call("Estado reseteado correctamente.")

if __name__ == '__main__':
    unittest.main()