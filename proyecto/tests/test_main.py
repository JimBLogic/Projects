import unittest
from unittest.mock import patch
from main import add_seat, reserve_seat, cancel_reservation, update_seat_info as update_seat, manage_seats
from proyecto.sala_cine import SalaCine

class TestMain(unittest.TestCase):
    def setUp(self):
        global cinema
        cinema = SalaCine()

    @patch('builtins.input', side_effect=['1', 'A', '1'])
    def test_add_seat(self, mock_input):
        add_seat()
        self.assertIn({"numero": 1, "fila": "A", "reservado": False, "precio": 10.0}, cinema.get_estado()["lunes"])

    @patch('builtins.input', side_effect=['1', 'A', '1', '30'])
    def test_reserve_seat(self, mock_input):
        add_seat()
        reserve_seat()
        self.assertTrue(cinema.get_estado()["lunes"][0]["reservado"])

    @patch('builtins.input', side_effect=['1', 'A', '1', '30'])
    def test_cancel_reservation(self, mock_input):
        add_seat()
        reserve_seat()
        cancel_reservation()
        self.assertFalse(cinema.get_estado()["lunes"][0]["reservado"])

    @patch('builtins.input', side_effect=['1', 'A', '1', 'B', '2'])
    def test_update_seat(self, mock_input):
        add_seat()
        update_seat()
        self.assertIn({"numero": 2, "fila": "B", "reservado": False, "precio": 10.0}, cinema.get_estado()["lunes"])

    @patch('builtins.input', side_effect=['1'])
    @patch('builtins.print')
    def test_manage_seats_option(self, mock_print, mock_input):
        manage_seats()
        mock_print.assert_any_call("Seleccione una opción de gestión de asientos:")

if __name__ == '__main__':
    unittest.main()