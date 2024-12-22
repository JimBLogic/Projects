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
from proyecto.sala_cine import SalaCine
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

class TestSalaCine(unittest.TestCase):

    def setUp(self):
        self.test_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'estado_cine.json'))
        self.cinema = SalaCine(archivo_estado=self.test_file)
        initial_state = {day: [] for day in ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]}
        with open(self.test_file, 'w') as file:
            json.dump(initial_state, file, indent=4)
        logging.debug('TestSalaCine setUp executed')

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        logging.debug('TestSalaCine tearDown executed')

    def test_add_seat(self):
        """
        Prueba agregar un asiento a la sala de cine.
        """
        seat = Asiento(1, 'A', False, 10.0)
        message = self.cinema.agregar_asiento('lunes', 'A', 1)
        self.assertEqual(message, "Asiento agregado correctamente.")
        state = self.cinema.get_estado()
        self.assertIn(seat.to_dict(), [asiento.to_dict() for asiento in state['lunes']])
        logging.debug('test_add_seat passed')

    def test_add_seat_exceeds_limit(self):
        """
        Prueba agregar un asiento que excede el límite de filas.
        """
        for i in range(1, 7):
            self.cinema.agregar_asiento('lunes', chr(64 + i), 1)
        with self.assertRaises(ValueError) as context:
            self.cinema.agregar_asiento('lunes', 'G', 1)
        self.assertTrue("Fila inválida. Debe ser una letra entre A y F." in str(context.exception))
        logging.debug('test_add_seat_exceeds_limit passed')

    def test_reserve_seat(self):
        """
        Prueba reservar un asiento en la sala de cine.
        """
        self.cinema.agregar_asiento('lunes', 'A', 1)
        message = self.cinema.reservar_asiento('lunes', 'A', 1, 30)
        state = self.cinema.get_estado()
        self.assertTrue(state['lunes'][0].is_reservado())
        self.assertEqual(message, "Asiento reservado correctamente.")
        logging.debug('test_reserve_seat passed')

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
        logging.debug('test_cancel_reservation passed')

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
        logging.debug('test_update_seat passed')

    def test_delete_seat(self):
        """
        Prueba eliminar un asiento de la sala de cine.
        """
        self.cinema.agregar_asiento('lunes', 'A', 1)
        message = self.cinema.eliminar_asiento('lunes', 'A', 1)
        state = self.cinema.get_estado()
        self.assertEqual(len(state['lunes']), 0)
        self.assertEqual(message, "Asiento eliminado correctamente.")
        logging.debug('test_delete_seat passed')

class TestMensajes(unittest.TestCase):
    """
    Clase de pruebas para la clase Mensajes.
    """

    def setUp(self):
        """
        Configuración inicial para las pruebas.
        """
        initial_state = {dia: [] for dia in ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]}
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'estado_cine.json')), 'w') as file:
            json.dump(initial_state, file, indent=4)
        logging.debug('TestMensajes setUp executed')

    def test_bienvenida(self):
        """
        Prueba el mensaje de bienvenida.
        """
        self.assertEqual(Mensajes.bienvenida(), "Bienvenido al sistema de gestión de asientos del cine.")
        logging.debug('test_bienvenida passed')

    def test_opcion_invalida(self):
        """
        Prueba el mensaje de opción inválida.
        """
        self.assertEqual(Mensajes.opcion_invalida(), "Opción inválida. Por favor, intente de nuevo.")
        logging.debug('test_opcion_invalida passed')

    def test_asiento_agregado(self):
        """
        Prueba el mensaje de asiento agregado.
        """
        self.assertEqual(Mensajes.asiento_agregado(), "Asiento agregado correctamente.")
        logging.debug('test_asiento_agregado passed')

    def test_asiento_reservado(self):
        """
        Prueba el mensaje de asiento reservado.
        """
        self.assertEqual(Mensajes.asiento_reservado(), "Asiento reservado correctamente.")
        logging.debug('test_asiento_reservado passed')

    def test_reserva_cancelada(self):
        """
        Prueba el mensaje de reserva cancelada.
        """
        self.assertEqual(Mensajes.reserva_cancelada(), "Reserva cancelada correctamente.")
        logging.debug('test_reserva_cancelada passed')

    def test_reporte_disponibilidad(self):
        """
        Prueba el mensaje de reporte de disponibilidad.
        """
        self.assertEqual(Mensajes.reporte_disponibilidad("lunes", 10, 5, 85), "Lunes: 10 asientos libres, 5 asientos reservados, 85 asientos no agregados.")
        logging.debug('test_reporte_disponibilidad passed')

    def test_max_intentos(self):
        """
        Prueba el mensaje de número máximo de intentos alcanzado.
        """
        self.assertEqual(Mensajes.max_intentos(), "Número máximo de intentos alcanzado. Por favor, intente de nuevo más tarde.")
        logging.debug('test_max_intentos passed')

    def test_confirmar_reseteo(self):
        """
        Prueba el mensaje de confirmación de reseteo.
        """
        self.assertEqual(Mensajes.confirmar_reseteo(), "¿Está seguro de que desea resetear el estado? Esto borrará todos los datos. (si/no):")
        logging.debug('test_confirmar_reseteo passed')

    def test_reseteo_cancelado(self):
        """
        Prueba el mensaje de reseteo cancelado.
        """
        self.assertEqual(Mensajes.reseteo_cancelado(), "Reseteo de estado cancelado.")
        logging.debug('test_reseteo_cancelado passed')

    def test_confirmar_guardado(self):
        """
        Prueba el mensaje de confirmación de guardado.
        """
        self.assertEqual(Mensajes.confirmar_guardado(), "¿Desea guardar el estado actual antes de salir? (si/no):")
        logging.debug('test_confirmar_guardado passed')

    def test_estado_guardado(self):
        """
        Prueba el mensaje de estado guardado.
        """
        self.assertEqual(Mensajes.estado_guardado(), "Estado guardado correctamente.")
        logging.debug('test_estado_guardado passed')

    def test_estado_reseteado(self):
        """
        Prueba el mensaje de estado reseteado.
        """
        self.assertEqual(Mensajes.estado_reseteado(), "Estado reseteado correctamente.")
        logging.debug('test_estado_reseteado passed')

    def test_saliendo_sistema(self):
        """
        Prueba el mensaje de salida del sistema.
        """
        self.assertEqual(Mensajes.saliendo_sistema(), "Saliendo del sistema...")
        logging.debug('test_saliendo_sistema passed')

    def test_ingrese_dia(self):
        """
        Prueba el mensaje para ingresar el día.
        """
        self.assertEqual(Mensajes.ingrese_dia(), "Ingrese el día (1: lunes, 2: martes, 3: miércoles, 4: jueves, 5: viernes, 6: sábado, 7: domingo): ")
        logging.debug('test_ingrese_dia passed')

    def test_ingrese_fila(self):
        """
        Prueba el mensaje para ingresar la fila.
        """
        self.assertEqual(Mensajes.ingrese_fila(), "Ingrese la fila (A-F): ")
        logging.debug('test_ingrese_fila passed')

    def test_ingrese_numero_asiento(self):
        """
        Prueba el mensaje para ingresar el número de asiento.
        """
        self.assertEqual(Mensajes.ingrese_numero_asiento(), "Ingrese el número de asiento (1-10): ")
        logging.debug('test_ingrese_numero_asiento passed')

    def test_dia_invalido(self):
        """
        Prueba el mensaje de día inválido.
        """
        self.assertEqual(Mensajes.dia_invalido(), "Día inválido. Por favor, intente de nuevo.")
        logging.debug('test_dia_invalido passed')

    def test_asiento_no_encontrado(self):
        """
        Prueba el mensaje de asiento no encontrado.
        """
        self.assertEqual(Mensajes.asiento_no_encontrado(), "El asiento no se encuentra en el sistema.")
        logging.debug('test_asiento_no_encontrado passed')

    def test_asiento_ya_reservado(self):
        """
        Prueba el mensaje de asiento ya reservado.
        """
        self.assertEqual(Mensajes.asiento_ya_reservado(), "El asiento ya está reservado.")
        logging.debug('test_asiento_ya_reservado passed')

    def test_asiento_ya_existe(self):
        """
        Prueba el mensaje de asiento ya existente.
        """
        self.assertEqual(Mensajes.asiento_ya_existe(), "El asiento ya existe en el sistema.")
        logging.debug('test_asiento_ya_existe passed')

    def test_ingrese_edad(self):
        """
        Prueba el mensaje para ingresar la edad del espectador.
        """
        self.assertEqual(Mensajes.ingrese_edad(), "Ingrese la edad del espectador: ")
        logging.debug('test_ingrese_edad passed')

    def test_ingrese_nueva_fila(self):
        """
        Prueba el mensaje para ingresar la nueva fila.
        """
        self.assertEqual(Mensajes.ingrese_nueva_fila(), "Ingrese la nueva fila (A-F): ")
        logging.debug('test_ingrese_nueva_fila passed')

    def test_ingrese_nuevo_numero_asiento(self):
        """
        Prueba el mensaje para ingresar el nuevo número de asiento.
        """
        self.assertEqual(Mensajes.ingrese_nuevo_numero_asiento(), "Ingrese el nuevo número de asiento (1-10): ")
        logging.debug('test_ingrese_nuevo_numero_asiento passed')

    def test_asiento_eliminado(self):
        """
        Prueba el mensaje de asiento eliminado.
        """
        self.assertEqual(Mensajes.asiento_eliminado(), "Asiento eliminado correctamente.")
        logging.debug('test_asiento_eliminado passed')

    def test_asiento_actualizado(self):
        """
        Prueba el mensaje de asiento actualizado.
        """
        self.assertEqual(Mensajes.asiento_actualizado(), "Asiento actualizado correctamente.")
        logging.debug('test_asiento_actualizado passed')

if __name__ == '__main__':
    unittest.main()
