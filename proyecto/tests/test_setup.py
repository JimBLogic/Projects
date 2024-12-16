import os
import json
import unittest
from unittest.mock import patch, mock_open
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from proyecto import verificar_sistema

def reset_estado_sala():
    """
    Resetea el estado de la sala de cine a su estado inicial.
    """
    estado_inicial = {dia: [] for dia in ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]}
    with open('estado_sala.json', 'w') as file:
        json.dump(estado_inicial, file, indent=4)

class TestSetup(unittest.TestCase):
    """
    Clase de pruebas para la configuración inicial del sistema.
    """

    @patch('proyecto.verificar_sistema.crear_archivo_estado')
    def test_crear_archivo_estado(self, mock_crear):
        """
        Prueba la creación del archivo de estado inicial.
        """
        verificar_sistema.crear_archivo_estado('estado_sala.json', {})
        mock_crear.assert_called_once_with('estado_sala.json', {})

    @patch('proyecto.verificar_sistema.cargar_archivo_estado', return_value={})
    def test_cargar_archivo_estado_existente(self, mock_cargar):
        """
        Prueba la carga de un archivo de estado existente.
        """
        estado = verificar_sistema.cargar_archivo_estado('estado_sala.json')
        self.assertEqual(estado, {})

    @patch('proyecto.verificar_sistema.cargar_archivo_estado', return_value={"lunes": [{"fila": "A", "numero": 1, "estado": "libre"}]})
    def test_cargar_archivo_estado_con_datos(self, mock_cargar):
        """
        Prueba la carga de un archivo de estado con datos.
        """
        estado = verificar_sistema.cargar_archivo_estado('estado_sala.json')
        self.assertEqual(estado, {"lunes": [{"fila": "A", "numero": 1, "estado": "libre"}]})

    @patch('proyecto.verificar_sistema.cargar_archivo_estado', return_value={})
    def test_cargar_archivo_estado_no_file(self, mock_cargar):
        """
        Prueba la carga de un archivo de estado cuando no existe el archivo.
        """
        estado = verificar_sistema.cargar_archivo_estado('estado_sala.json')
        self.assertEqual(estado, {})

    def test_reset_estado_sala(self):
        """
        Prueba la función reset_estado_sala.
        """
        reset_estado_sala()
        with open('estado_sala.json', 'r') as file:
            estado = json.load(file)
        self.assertEqual(estado, {dia: [] for dia in ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]})

if __name__ == '__main__':
    unittest.main()