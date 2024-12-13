import unittest
from unittest.mock import patch, mock_open
import verificar_sistema
import os

class TestVerificarSistema(unittest.TestCase):
    """
    Clase de pruebas para las funciones del módulo verificar_sistema.
    """

    @patch('subprocess.run')
    def test_ejecutar_tests(self, mock_run):
        """
        Prueba la función ejecutar_tests.
        """
        mock_run.return_value.returncode = 0
        mock_run.return_value.stdout = "Todos los tests pasaron correctamente."
        result = verificar_sistema.ejecutar_tests()
        mock_run.assert_called_with(['python', '-m', 'unittest', 'discover', '-s', 'tests'], capture_output=True, text=True)
        self.assertEqual(result, "Todos los tests pasaron correctamente.")

    @patch('os.path.exists', return_value=True)
    @patch('builtins.open', new_callable=mock_open, read_data="INFO: No errors found.")
    def test_revisar_debug_log(self, mock_open, mock_exists):
        """
        Prueba la función revisar_debug_log.
        """
        result = verificar_sistema.revisar_debug_log()
        mock_open.assert_called_with('debug.log', 'r')
        self.assertEqual(result, "INFO: No errors found.")

    @patch('os.path.exists', return_value=False)
    def test_revisar_debug_log_no_file(self, mock_exists):
        """
        Prueba la función revisar_debug_log cuando no existe el archivo.
        """
        result = verificar_sistema.revisar_debug_log()
        self.assertEqual(result, "El archivo debug.log no existe.")

    @patch('subprocess.run')
    def test_probar_programa(self, mock_run):
        """
        Prueba la función probar_programa.
        """
        mock_run.return_value.returncode = 0
        mock_run.return_value.stdout = "El programa se ejecutó correctamente."
        result = verificar_sistema.probar_programa()
        mock_run.assert_called_with(['python', 'main.py'], capture_output=True, text=True)
        self.assertEqual(result, "El programa se ejecutó correctamente.")

if __name__ == '__main__':
    unittest.main()