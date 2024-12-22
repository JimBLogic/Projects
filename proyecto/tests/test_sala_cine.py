import unittest
import sys
import os
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from proyecto.sala_cine import SalaCine
from proyecto.asiento import Asiento

class TestSalaCine(unittest.TestCase):

    def setUp(self):
        self.test_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../estado_sala.json'))
        self.cinema = SalaCine(archivo_estado=self.test_file)
        initial_state = {day: [] for day in ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]}
        with open(self.test_file, 'w') as file:
            json.dump(initial_state, file, indent=4)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_seat(self):
        """
        Prueba agregar un asiento a la sala de cine.
        """
        seat = Asiento(1, 'A', False, 10.0)
        message = self.cinema.agregar_asiento('lunes', 'A', 1)
        self.assertEqual(message, "Asiento agregado correctamente.")
        state = self.cinema.get_estado()
        self.assertIn(seat.to_dict(), [asiento.to_dict() for asiento in state['lunes']])

    def test_add_seat_exceeds_limit(self):
        """
        Prueba agregar un asiento que excede el límite de filas.
        """
        for i in range(1, 11):
            self.cinema.agregar_asiento('lunes', chr(64 + i), 1)
        message = self.cinema.agregar_asiento('lunes', 'J', 2)
        self.assertEqual(message, "Número máximo de filas alcanzado.")

    def test_reserve_seat(self):
        """
        Prueba reservar un asiento en la sala de cine.
        """
        self.cinema.agregar_asiento('lunes', 'A', 1)
        message = self.cinema.reservar_asiento('lunes', 'A', 1, 30)
        state = self.cinema.get_estado()
        self.assertTrue(state['lunes'][0].is_reservado())
        self.assertEqual(message, "Asiento reservado correctamente.")

    def test_cancel_reservation(self):
        """
        Prueba cancelar la reserva de un asiento en la sala de cine.
        """
        self.cinema.agregar_asiento('lunes', 'A', 1)
        self.cinema.reservar_asiento('lunes', 'A', 1, 30)
        message = self.cinema.cancelar_reserva('lunes', 'A', 1)
        state = self.cinema.get_estado()
        self.assertFalse(state['lunes'][0].is_reservado())
        self.assertEqual(message, "Reserva cancelada correctamente.")

    def test_update_seat(self):
        """
        Prueba actualizar la información de un asiento en la sala de cine.
        """
        self.cinema.agregar_asiento('lunes', 'A', 1)
        message = self.cinema.actualizar_asiento('lunes', 'A', 1, 'B', 2)
        state = self.cinema.get_estado()
        self.assertEqual(state['lunes'][0].get_fila(), 'B')
        self.assertEqual(state['lunes'][0].get_numero(), 2)
        self.assertEqual(message, "Asiento actualizado correctamente.")

    def test_delete_seat(self):
        """
        Prueba eliminar un asiento de la sala de cine.
        """
        self.cinema.agregar_asiento('lunes', 'A', 1)
        message = self.cinema.eliminar_asiento('lunes', 'A', 1)
        state = self.cinema.get_estado()
        self.assertEqual(len(state['lunes']), 0)
        self.assertEqual(message, "Asiento eliminado correctamente.")

if __name__ == '__main__':
    unittest.main()