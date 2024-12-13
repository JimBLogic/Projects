import os
import json

def reset_estado_sala():
    """
    Resetea el estado de la sala de cine a su estado inicial.
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
        json.dump(estado_inicial, file, indent=4)

import unittest
from unittest.mock import patch, mock_open
import verificar_sistema

class TestSetup(unittest.TestCase):
    """
    Clase de pruebas para la configuración inicial del sistema.
    """

    @patch('os.path.exists', return_value=False)
    @patch('builtins.open', new_callable=mock_open)
    def test_crear_archivo_estado(self, mock_open, mock_exists):
        """
        Prueba la creación del archivo de estado inicial.
        """
        verificar_sistema.crear_archivo_estado()
        mock_open.assert_called_with('estado_sala.json', 'w')

    @patch('os.path.exists', return_value=True)
    @patch('builtins.open', new_callable=mock_open, read_data='{}')
    def test_cargar_archivo_estado_existente(self, mock_open, mock_exists):
        """
        Prueba la carga de un archivo de estado existente.
        """
        estado = verificar_sistema.cargar_archivo_estado()
        self.assertEqual(estado, {})

    @patch('os.path.exists', return_value=True)
    @patch('builtins.open', new_callable=mock_open, read_data='{"lunes": [{"fila": "A", "numero": 1, "estado": "libre"}]}')
    def test_cargar_archivo_estado_con_datos(self, mock_open, mock_exists):
        """
        Prueba la carga de un archivo de estado con datos.
        """
        estado = verificar_sistema.cargar_archivo_estado()
        self.assertEqual(estado, {"lunes": [{"fila": "A", "numero": 1, "estado": "libre"}]})

    @patch('os.path.exists', return_value=False)
    def test_cargar_archivo_estado_no_file(self, mock_exists):
        """
        Prueba la carga de un archivo de estado cuando no existe el archivo.
        """
        estado = verificar_sistema.cargar_archivo_estado()
        self.assertEqual(estado, None)

if __name__ == '__main__':
    unittest.main()