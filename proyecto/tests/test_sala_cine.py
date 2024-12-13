import unittest
from sala_cine import SalaCine
from asiento import Asiento
from mensajes import Mensajes
import os
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
    Clase de pruebas para la clase SalaCine.
    """

    def setUp(self):
        """
        Configuración inicial para los tests.
        """
        reset_estado_sala()
        self.sala = SalaCine()

    def tearDown(self):
        """
        Limpieza después de cada test.
        """
        if os.path.exists('estado_sala.json'):
            os.remove('estado_sala.json')

    def test_agregar_asiento(self):
        """
        Prueba la función agregar_asiento.
        """
        mensaje = self.sala.agregar_asiento("lunes", "A", 1)
        self.assertEqual(mensaje, Mensajes.asiento_agregado())
        self.assertEqual(len(self.sala.estado["lunes"]), 1)
        self.assertEqual(self.sala.estado["lunes"][0].to_dict(), {"fila": "A", "numero": 1, "estado": "libre"})

    def test_reservar_asiento(self):
        """
        Prueba la función reservar_asiento.
        """
        self.sala.agregar_asiento("lunes", "A", 1)
        mensaje = self.sala.reservar_asiento("lunes", "A", 1)
        self.assertEqual(mensaje, Mensajes.asiento_reservado())
        self.assertEqual(self.sala.estado["lunes"][0].estado, "reservado")

    def test_cancelar_reserva(self):
        """
        Prueba la función cancelar_reserva.
        """
        self.sala.agregar_asiento("lunes", "A", 1)
        self.sala.reservar_asiento("lunes", "A", 1)
        mensaje = self.sala.cancelar_reserva("lunes", "A", 1)
        self.assertEqual(mensaje, Mensajes.reserva_cancelada())
        self.assertEqual(self.sala.estado["lunes"][0].estado, "libre")

    def test_reporte_disponibilidad(self):
        """
        Prueba la función reporte_disponibilidad.
        """
        self.sala.agregar_asiento("lunes", "A", 1)
        self.sala.reservar_asiento("lunes", "A", 1)
        reporte = self.sala.reporte_disponibilidad()
        self.assertEqual(reporte["lunes"]["libres"], 0)
        self.assertEqual(reporte["lunes"]["reservados"], 1)
        self.assertEqual(reporte["lunes"]["no_agregados"], 99)

    def test_agregar_asiento_existente(self):
        """
        Prueba agregar un asiento que ya existe.
        """
        self.sala.agregar_asiento("lunes", "A", 1)
        with self.assertRaises(ValueError):
            self.sala.agregar_asiento("lunes", "A", 1)

    def test_reservar_asiento_inexistente(self):
        """
        Prueba reservar un asiento que no existe.
        """
        mensaje = self.sala.reservar_asiento("lunes", "A", 1)
        self.assertEqual(mensaje, Mensajes.asiento_no_encontrado())

    def test_cancelar_reserva_asiento_inexistente(self):
        """
        Prueba cancelar la reserva de un asiento que no existe.
        """
        mensaje = self.sala.cancelar_reserva("lunes", "A", 1)
        self.assertEqual(mensaje, Mensajes.asiento_no_encontrado())

    def test_reporte_disponibilidad_sin_asientos(self):
        """
        Prueba la función reporte_disponibilidad sin asientos.
        """
        reporte = self.sala.reporte_disponibilidad()
        self.assertEqual(reporte["lunes"]["libres"], 0)
        self.assertEqual(reporte["lunes"]["reservados"], 0)
        self.assertEqual(reporte["lunes"]["no_agregados"], 100)

if __name__ == '__main__':
    unittest.main()