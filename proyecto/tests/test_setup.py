import os
import json
import unittest
from unittest.mock import patch, mock_open
import sys
import logging
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from proyecto.verificar_sistema import create_state_file as create_cinema_state, load_state_file as load_cinema_state, delete_state_file

# Configurar el logger
log_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../debug.log'))
logging.basicConfig(filename=log_file_path, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def reset_cinema_state():
    """
    Resetea el estado de la sala de cine a su estado inicial.
    """
    initial_state = {day: [] for day in ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]}
    with open(os.path.join(os.path.dirname(__file__), '../estado_sala.json'), 'w') as file:
        json.dump(initial_state, file, indent=4)

class TestSetup(unittest.TestCase):
    """
    Clase de pruebas para la configuración inicial del sistema.
    """

    def setUp(self):
        """
        Configuración inicial para las pruebas.
        """
        self.test_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../estado_sala.json'))
        self.initial_state = {
            "lunes": [],
            "martes": [],
            "miércoles": [],
            "jueves": [],
            "viernes": [],
            "sábado": [],
            "domingo": []
        }
        logging.basicConfig(filename='debug.log', level=logging.DEBUG)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    @patch('proyecto.verificar_sistema.create_state_file')
    def test_create_cinema_state(self, mock_create):
        """
        Prueba la creación del archivo de estado inicial.
        """
        create_cinema_state(self.test_file, self.initial_state)
        mock_create.assert_called_once_with(self.test_file, self.initial_state)
        logging.debug('test_create_cinema_state passed')

    @patch('builtins.open', new_callable=mock_open, read_data='{"lunes": [], "martes": [], "miércoles": [], "jueves": [], "viernes": [], "sábado": [], "domingo": []}')
    def test_load_cinema_state_existing(self, mock_open):
        """
        Prueba la carga de un archivo de estado existente.
        """
        state = load_cinema_state(os.path.join(os.path.dirname(__file__), '../estado_sala.json'))
        self.assertEqual(state, {day: [] for day in ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]})
        mock_open.assert_called_once_with(os.path.join(os.path.dirname(__file__), '../estado_sala.json'), 'r')

    @patch('builtins.open', new_callable=mock_open, read_data='{"lunes": [{"fila": "A", "numero": 1, "estado": "libre"}]}')
    def test_load_cinema_state_with_data(self, mock_open):
        """
        Prueba la carga de un archivo de estado con datos.
        """
        state = load_cinema_state(os.path.join(os.path.dirname(__file__), '../estado_sala.json'))
        self.assertEqual(state, {"lunes": [{"fila": "A", "numero": 1, "estado": "libre"}]})
        mock_open.assert_called_once_with(os.path.join(os.path.dirname(__file__), '../estado_sala.json'), 'r')

    @patch('proyecto.verificar_sistema.load_state_file', return_value={day: [] for day in ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]})
    def test_load_cinema_state_no_file(self, mock_load):
        """
        Prueba la carga de un archivo de estado cuando no existe el archivo.
        """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        state = load_cinema_state(self.test_file)
        self.assertEqual(state, self.initial_state)
        mock_load.assert_called_once()

    def test_reset_cinema_state(self):
        """
        Prueba la función reset_cinema_state.
        """
        reset_cinema_state()
        with open(os.path.join(os.path.dirname(__file__), '../estado_sala.json'), 'r') as file:
            state = json.load(file)
        self.assertEqual(state, {day: [] for day in ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]})

    def test_delete_state_file(self):
        """
        Prueba la función delete_state_file.
        """
        create_cinema_state(self.test_file, self.initial_state)
        delete_state_file(self.test_file)
        self.assertFalse(os.path.exists(self.test_file))
        logging.debug('test_delete_state_file passed')

if __name__ == '__main__':
    unittest.main()