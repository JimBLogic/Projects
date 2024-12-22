import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from proyecto.asiento import Asiento
import json
import logging

# Configurar el logger
log_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../debug.log'))
logging.basicConfig(filename=log_file_path, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class TestAsiento(unittest.TestCase):
    """
    Clase de prueba para la clase Asiento.
    """
    
    def setUp(self):
        """
        Configuración inicial para las pruebas.
        """
        self.asiento = Asiento(1, 'A', False, 10.0)
        estado_inicial = {dia: [] for dia in ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]}
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../estado_sala.json')), 'w') as file:
            json.dump(estado_inicial, file, indent=4)

    def test_reservar_asiento_libre(self):
        """
        Prueba reservar un asiento que está libre.
        """
        mensaje = self.asiento.reservar()
        self.assertTrue(self.asiento.is_reservado())
        self.assertEqual(mensaje, "Asiento reservado correctamente.")
        logging.info("Asiento reservado correctamente.")

    def test_reservar_asiento_reservado(self):
        """
        Prueba reservar un asiento que ya está reservado.
        """
        self.asiento.set_reservado(True)
        with self.assertRaises(Exception) as context:
            self.asiento.reservar()
        self.assertTrue("El asiento ya está reservado." in str(context.exception))
        logging.error("Error al reservar asiento: El asiento ya está reservado.")

    def test_cancelar_reserva_asiento_reservado(self):
        """
        Prueba cancelar la reserva de un asiento que está reservado.
        """
        self.asiento.set_reservado(True)
        mensaje = self.asiento.cancelar()
        self.assertFalse(self.asiento.is_reservado())
        self.assertEqual(mensaje, "Reserva cancelada correctamente.")
        logging.info("Reserva cancelada correctamente.")

    def test_cancelar_reserva_asiento_no_reservado(self):
        """
        Prueba cancelar la reserva de un asiento que no está reservado.
        """
        with self.assertRaises(Exception) as context:
            self.asiento.cancelar()
        self.assertTrue("El asiento no está reservado." in str(context.exception))
        logging.error("Error al cancelar reserva: El asiento no está reservado.")

    def test_actualizar_asiento(self):
        """
        Prueba actualizar la fila y el número de un asiento.
        """
        mensaje = self.asiento.actualizar('B', 2)
        self.assertEqual(self.asiento.get_fila(), 'B')
        self.assertEqual(self.asiento.get_numero(), 2)
        self.assertEqual(mensaje, "Asiento actualizado correctamente.")
        logging.info("Asiento actualizado correctamente.")

    def test_to_dict(self):
        """
        Prueba convertir un objeto Asiento a un diccionario.
        """
        asiento_dict = self.asiento.to_dict()
        self.assertEqual(asiento_dict, {
            "numero": 1,
            "fila": 'A',
            "reservado": False,
            "precio": 10.0
        })
        logging.info("Asiento convertido a diccionario correctamente.")

    def test_from_dict(self):
        """
        Prueba crear un objeto Asiento a partir de un diccionario.
        """
        data = {
            "numero": 1,
            "fila": 'A',
            "reservado": False,
            "precio": 10.0
        }
        asiento = Asiento.from_dict(data)
        self.assertEqual(asiento.get_numero(), 1)
        self.assertEqual(asiento.get_fila(), 'A')
        self.assertFalse(asiento.is_reservado())
        self.assertEqual(asiento.get_precio(), 10.0)
        logging.info("Asiento creado a partir de diccionario correctamente.")

if __name__ == '__main__':
    unittest.main()