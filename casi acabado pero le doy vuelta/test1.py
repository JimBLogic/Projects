import unittest
import sys
import os
import json
import logging
from unittest.mock import patch, mock_open

# Ensure the correct path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import modules
from proyecto.verificar_sistema import load_state_file, create_state_file, delete_state_file
from proyecto.utilidades import save_state_file, reset_state_file, calculate_discount, calculate_final_price, validate_input, validate_option
from proyecto.asiento import Asiento
from proyecto.mensajes import Mensajes

# Configure logger
log_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'debug.log'))
logging.basicConfig(filename=log_file_path, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class TestVerificarSistema(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'estado_cine.json'))
        cls.initial_state = {
            "lunes": [],
            "martes": [],
            "miércoles": [],
            "jueves": [],
            "viernes": [],
            "sábado": [],
            "domingo": []
        }
        logging.debug('TestVerificarSistema setUpClass executed')

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.test_file):
            os.remove(cls.test_file)
        logging.debug('TestVerificarSistema tearDownClass executed')

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

class TestUtilidades(unittest.TestCase):
    """
    Clase de pruebas para las funciones del módulo utilidades.
    """

    def setUp(self):
        """
        Configuración inicial para las pruebas.
        """
        logging.debug('TestUtilidades setUp ejecutado')

    def test_calculate_discount(self):
        """
        Prueba la función calculate_discount.
        """
        self.assertEqual(calculate_discount(100, 25, "lunes"), 0.0)
        self.assertEqual(calculate_discount(100, 65, "miércoles"), 0.5)
        self.assertEqual(calculate_discount(100, 30, "domingo"), 0.0)
        logging.debug('test_calculate_discount passed')

    def test_calculate_final_price(self):
        """
        Prueba la función calculate_final_price.
        """
        self.assertEqual(calculate_final_price(100, 25, "lunes"), 100.0)
        self.assertEqual(calculate_final_price(100, 65, "miércoles"), 50.0)
        self.assertEqual(calculate_final_price(100, 30, "domingo"), 100.0)
        logging.debug('test_calculate_final_price passed')

    @patch('builtins.input', side_effect=['5'])
    def test_validate_input(self, mock_input):
        """
        Prueba la función validate_input.
        """
        self.assertEqual(validate_input("Ingrese un número: ", int, range(1, 6)), 5)
        logging.debug('test_validate_input passed')

    @patch('builtins.input', side_effect=['A', 'B', 'C'])
    def test_validate_input_invalid(self, mock_input):
        """
        Prueba la función validate_input para manejar entradas inválidas.
        """
        with self.assertRaises(StopIteration):
            validate_input("Ingrese un número: ", int, range(1, 6))
        logging.debug('test_validate_input_invalid passed')

    @patch('builtins.input', side_effect=StopIteration)
    def test_validate_input_stop_iteration(self, mock_input):
        """
        Prueba la función validate_input para manejar StopIteration.
        """
        with self.assertRaises(StopIteration):
            validate_input("Ingrese un número: ", int, range(1, 6))
        logging.debug('test_validate_input_stop_iteration passed')

    @patch('builtins.input', side_effect=['opcion1'])
    def test_validate_option(self, mock_input):
        """
        Prueba la función validate_option.
        """
        self.assertEqual(validate_option("Seleccione una opción: ", ['opcion1', 'opcion2']), 'opcion1')
        logging.debug('test_validate_option passed')

class TestAsiento(unittest.TestCase):

    def setUp(self):
        self.asiento = Asiento(1, 'A', False, 10.0)

    def test_reservar(self):
        self.assertFalse(self.asiento.is_reservado())
        self.asiento.reservar()
        self.assertTrue(self.asiento.is_reservado())

    def test_cancelar(self):
        self.asiento.reservar()
        self.assertTrue(self.asiento.is_reservado())
        self.asiento.cancelar()
        self.assertFalse(self.asiento.is_reservado())

    def test_actualizar(self):
        self.asiento.actualizar('B', 2)
        self.assertEqual(self.asiento.get_fila(), 'B')
        self.assertEqual(self.asiento.get_numero(), 2)

    def test_to_dict(self):
        asiento_dict = self.asiento.to_dict()
        self.assertEqual(asiento_dict['numero'], 1)
        self.assertEqual(asiento_dict['fila'], 'A')
        self.assertEqual(asiento_dict['reservado'], False)
        self.assertEqual(asiento_dict['precio'], 10.0)

    def test_from_dict(self):
        data = {"numero": 2, "fila": "B", "reservado": True, "precio": 15.0}
        nuevo_asiento = Asiento.from_dict(data)
        self.assertEqual(nuevo_asiento.get_numero(), 2)
        self.assertEqual(nuevo_asiento.get_fila(), 'B')
        self.assertTrue(nuevo_asiento.is_reservado())
        self.assertEqual(nuevo_asiento.get_precio(), 15.0)

class TestMensajes(unittest.TestCase):

    def test_bienvenida(self):
        self.assertEqual(Mensajes.bienvenida(), "Bienvenido al sistema de gestión de asientos del cine.")

    def test_opcion_invalida(self):
        self.assertEqual(Mensajes.opcion_invalida(), "Opción inválida. Por favor, intente de nuevo.")

    def test_asiento_agregado(self):
        self.assertEqual(Mensajes.asiento_agregado(), "Asiento agregado correctamente.")

    def test_asiento_reservado(self):
        self.assertEqual(Mensajes.asiento_reservado(), "Asiento reservado correctamente.")

    def test_reserva_cancelada(self):
        self.assertEqual(Mensajes.reserva_cancelada(), "Reserva cancelada correctamente.")

    def test_reporte_disponibilidad(self):
        self.assertEqual(Mensajes.reporte_disponibilidad("lunes", 10, 5, 45), "Lunes: 10 asientos libres, 5 asientos reservados, 45 asientos no agregados.")

    def test_max_intentos(self):
        self.assertEqual(Mensajes.max_intentos(), "Número máximo de intentos alcanzado. Por favor, intente de nuevo más tarde.")

    def test_confirmar_reseteo(self):
        self.assertEqual(Mensajes.confirmar_reseteo(), "¿Está seguro de que desea resetear el estado? Esto borrará todos los datos. (si/no):")

    def test_reseteo_cancelado(self):
        self.assertEqual(Mensajes.reseteo_cancelado(), "Reseteo de estado cancelado.")

    def test_confirmar_guardado(self):
        self.assertEqual(Mensajes.confirmar_guardado(), "¿Desea guardar el estado actual antes de salir? (si/no):")

    def test_estado_guardado(self):
        self.assertEqual(Mensajes.estado_guardado(), "Estado guardado correctamente.")

    def test_estado_reseteado(self):
        self.assertEqual(Mensajes.estado_reseteado(), "Estado reseteado correctamente.")

    def test_saliendo_sistema(self):
        self.assertEqual(Mensajes.saliendo_sistema(), "Saliendo del sistema...")

    def test_ingrese_dia(self):
        self.assertEqual(Mensajes.ingrese_dia(), "Ingrese el día (1: lunes, 2: martes, 3: miércoles, 4: jueves, 5: viernes, 6: sábado, 7: domingo): ")

    def test_ingrese_fila(self):
        self.assertEqual(Mensajes.ingrese_fila(), "Ingrese la fila (A-F): ")

    def test_ingrese_numero_asiento(self):
        self.assertEqual(Mensajes.ingrese_numero_asiento(), "Ingrese el número de asiento (1-10): ")

    def test_dia_invalido(self):
        self.assertEqual(Mensajes.dia_invalido(), "Día inválido. Por favor, intente de nuevo.")

    def test_asiento_no_encontrado(self):
        self.assertEqual(Mensajes.asiento_no_encontrado(), "El asiento no se encuentra en el sistema.")

    def test_asiento_ya_reservado(self):
        self.assertEqual(Mensajes.asiento_ya_reservado(), "El asiento ya está reservado.")

    def test_asiento_ya_existe(self):
        self.assertEqual(Mensajes.asiento_ya_existe(), "El asiento ya existe en el sistema.")

    def test_ingrese_edad(self):
        self.assertEqual(Mensajes.ingrese_edad(), "Ingrese la edad del espectador: ")

    def test_asiento_actualizado(self):
        self.assertEqual(Mensajes.asiento_actualizado(), "Asiento actualizado correctamente.")

    def test_ingrese_nueva_fila(self):
        self.assertEqual(Mensajes.ingrese_nueva_fila(), "Ingrese la nueva fila (A-F): ")

    def test_ingrese_nuevo_numero_asiento(self):
        self.assertEqual(Mensajes.ingrese_nuevo_numero_asiento(), "Ingrese el nuevo número de asiento (1-10): ")

    def test_asiento_eliminado(self):
        self.assertEqual(Mensajes.asiento_eliminado(), "Asiento eliminado correctamente.")

if __name__ == '__main__':
    unittest.main()
