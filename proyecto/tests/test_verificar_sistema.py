import unittest
import os
import json
import sys
import logging

# Asegurar que la ruta es correcta
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Verificar la ruta
print(sys.path)

# Importar el módulo
from proyecto.verificar_sistema import load_state_file, create_state_file, delete_state_file
from proyecto.utilidades import save_state_file, reset_state_file

class TestVerificarSistema(unittest.TestCase):
    def setUp(self):
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

    def test_load_state_file(self):
        create_state_file(self.test_file, self.initial_state)
        state = load_state_file(self.test_file)
        self.assertEqual(state, self.initial_state)
        logging.debug('test_load_state_file passed')

    def test_create_state_file(self):
        create_state_file(self.test_file, self.initial_state)
        self.assertTrue(os.path.exists(self.test_file))
        with open(self.test_file, 'r') as f:
            state = json.load(f)
        self.assertEqual(state, self.initial_state)
        logging.debug('test_create_state_file passed')

    def test_save_state_file(self):
        create_state_file(self.test_file, self.initial_state)
        new_state = self.initial_state.copy()
        new_state["lunes"].append({"numero": 1, "fila": "A", "reservado": False, "precio": 10.0})
        save_state_file(self.test_file, new_state)
        with open(self.test_file, 'r') as f:
            state = json.load(f)
        self.assertEqual(state, new_state)
        logging.debug('test_save_state_file passed')

    def test_delete_state_file(self):
        create_state_file(self.test_file, self.initial_state)
        delete_state_file(self.test_file)
        self.assertFalse(os.path.exists(self.test_file))
        logging.debug('test_delete_state_file passed')

    def test_reset_state_file(self):
        create_state_file(self.test_file, self.initial_state)
        new_state = self.initial_state.copy()
        new_state["lunes"].append({"numero": 1, "fila": "A", "reservado": False, "precio": 10.0})
        save_state_file(self.test_file, new_state)
        reset_state_file(self.test_file, self.initial_state)
        with open(self.test_file, 'r') as f:
            state = json.load(f)
        self.assertEqual(state, self.initial_state)
        logging.debug('test_reset_state_file passed')

if __name__ == '__main__':
    unittest.main()