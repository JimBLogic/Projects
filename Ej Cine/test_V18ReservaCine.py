import unittest
from unittest.mock import patch
from io import StringIO
import os
from V18ReservaCine import main, reset_estado, guardar_estado

class TestMainFunction(unittest.TestCase):

    def setUp(self):
        """
        Runs before each test, resets the system state.
        """
        self.sala = reset_estado()

    def tearDown(self):
        """
        Runs after each test, removes any saved state.
        """
        if os.path.exists("estado_sala.json"):
            os.remove("estado_sala.json")

    @patch('builtins.input', side_effect=[
        '1', '1', 'lunes', '1', '1',  # Add individual seat
        '2', 'lunes', '1', '1', '30',  # Reserve seat
        '4', '1',  # Show all seats
        '7', 'no'  # Exit without saving
    ])
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_and_reserve_seat(self, mock_stdout, mock_input):
        """
        Test the flow of adding a seat, reserving it, and displaying seats.
        """
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Asiento 1 en fila 1 para el día lunes agregado correctamente.", output)
        self.assertIn("Precio final: €10.00", output)
        self.assertIn("Día: lunes, Estado: Reservado, Fila: 1, Asiento: 1", output)

    @patch('builtins.input', side_effect=[
        '8', 'si',  # Reset state
        '4', '1',  # Show all seats
        '7', 'no'  # Exit without saving
    ])
    @patch('sys.stdout', new_callable=StringIO)
    def test_reset_estado(self, mock_stdout, mock_input):
        """
        Test resetting the state of the system.
        """
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Estado reseteado correctamente.", output)
        self.assertIn("No hay asientos disponibles aún.", output)

    @patch('builtins.input', side_effect=[
        '1', '4',  # Add all seats for the entire week
        '7', 'no'  # Exit without saving
    ])
    @patch('sys.stdout', new_callable=StringIO)
    def test_agregar_todos_asientos_semana(self, mock_stdout, mock_input):
        """
        Test adding all seats for the entire week.
        """
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Asiento 1 en fila 1 para el día lunes agregado correctamente.", output)
        self.assertIn("Asiento 20 en fila 10 para el día domingo agregado correctamente.", output)

    @patch('builtins.input', side_effect=[
        '1', '1', 'lunes', '1', '1',  # Add seat
        '2', 'lunes', '1', '1', '30',  # Reserve seat
        '3', 'lunes', '1', '1', 'si',  # Cancel reservation
        '7', 'no'  # Exit without saving
    ])
    @patch('sys.stdout', new_callable=StringIO)
    def test_cancelar_reserva(self, mock_stdout, mock_input):
        """
        Test canceling a reservation.
        """
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Asiento 1 en fila 1 ahora está disponible.", output)

    @patch('builtins.input', side_effect=[
        '1', '1', 'lunes', '1', '1',  # Add seat
        '2', 'lunes', '1', '1', '30',  # Reserve seat
        '5', 'si',  # Save and exit
        '4', '1',  # Show all seats after loading
        '7', 'no'  # Exit without saving
    ])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_save_and_load(self, mock_stdout, mock_input):
        """
        Test saving and loading the system state.
        """
        main()
        output_save = mock_stdout.getvalue()
        self.assertIn("Estado guardado correctamente.", output_save)

        with patch('builtins.input', side_effect=['4', '1']):
            mock_stdout.seek(0)
            mock_stdout.truncate(0)
            main()
            output_load = mock_stdout.getvalue()
            self.assertIn("Día: lunes, Estado: Reservado, Fila: 1, Asiento: 1, Precio: €10.00", output_load)

if __name__ == "__main__":
    unittest.main()
