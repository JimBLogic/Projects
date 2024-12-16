import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from proyecto.sala_cine import SalaCine
from proyecto.asiento import Asiento
import json

def reset_estado_sala():
    """
    Resetea el archivo de estado de la sala para las pruebas.
    """
    estado_inicial = {
        "lunes": [],
        "martes": [],
        "miércoles": [],
        "jueves": [],
        "viernes": [],
        "sábado": [],
        "domingo": []
    }
    with open('estado_sala.json', 'w') as file:
        json.dump(estado_inicial, file)

class TestSalaCine(unittest.TestCase):
    """
    Clase de prueba para la clase SalaCine.
    """

    def setUp(self):
        """
        Configuración inicial para las pruebas.
        """
        self.sala = SalaCine()
        self.sala.set_estado({
            "lunes": [Asiento(1, "A", False, 10.0)],
            "martes": [],
            "miércoles": [],
            "jueves": [],
            "viernes": [],
            "sábado": [],
            "domingo": []
        })

    def tearDown(self):
        """
        Limpieza después de cada test.
        """
        if os.path.exists('estado_sala.json'):
            os.remove('estado_sala.json')

    def test_agregar_asiento(self):
        """
        Prueba la adición de un asiento.
        """
        mensaje = self.sala.agregar_asiento("lunes", "B", 2)
        self.assertEqual(mensaje, "Asiento agregado correctamente.")
        self.assertEqual(len(self.sala.get_estado()["lunes"]), 2)

    def test_reservar_asiento(self):
        """
        Prueba la reserva de un asiento.
        """
        mensaje = self.sala.reservar_asiento("lunes", "A", 1, 30)
        self.assertEqual(mensaje, "Asiento reservado correctamente.")
        self.assertTrue(self.sala.get_estado()["lunes"][0].is_reservado())

    def test_cancelar_reserva(self):
        """
        Prueba la cancelación de una reserva de asiento.
        """
        self.sala.reservar_asiento("lunes", "A", 1, 30)
        mensaje = self.sala.cancelar_reserva("lunes", "A", 1)
        self.assertEqual(mensaje, "Reserva cancelada correctamente.")
        self.assertFalse(self.sala.get_estado()["lunes"][0].is_reservado())

    def test_mostrar_asientos(self):
        """
        Prueba la visualización de los asientos.
        """
        asientos_info = self.sala.mostrar_asientos()
        self.assertIn("lunes", asientos_info)
        self.assertEqual(len(asientos_info["lunes"]), 1)

    def test_buscar_asiento(self):
        """
        Prueba la búsqueda de un asiento.
        """
        asiento_info = self.sala.buscar_asiento("lunes", "A", 1)
        self.assertEqual(asiento_info["numero"], 1)
        self.assertEqual(asiento_info["fila"], "A")

    def test_actualizar_asiento(self):
        """
        Prueba la actualización de un asiento.
        """
        mensaje = self.sala.actualizar_asiento("lunes", "A", 1, "B", 2)
        self.assertEqual(mensaje, "Asiento actualizado correctamente.")
        asiento_info = self.sala.buscar_asiento("lunes", "B", 2)
        self.assertEqual(asiento_info["numero"], 2)
        self.assertEqual(asiento_info["fila"], "B")

    def test_eliminar_asiento(self):
        """
        Prueba la eliminación de un asiento.
        """
        mensaje = self.sala.eliminar_asiento("lunes", "A", 1)
        self.assertEqual(mensaje, "Asiento eliminado correctamente.")
        self.assertEqual(len(self.sala.get_estado()["lunes"]), 0)

if __name__ == "__main__":
    unittest.main()