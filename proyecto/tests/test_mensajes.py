import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from proyecto.mensajes import Mensajes

class TestMensajes(unittest.TestCase):
    """
    Clase de pruebas para la clase Mensajes.
    """

    def test_bienvenida(self):
        """
        Prueba el mensaje de bienvenida.
        """
        self.assertEqual(Mensajes.bienvenida(), "Bienvenido al sistema de gestión de asientos del cine.")

    def test_opcion_invalida(self):
        """
        Prueba el mensaje de opción inválida.
        """
        self.assertEqual(Mensajes.opcion_invalida(), "Opción inválida. Por favor, intente de nuevo.")

    def test_asiento_agregado(self):
        """
        Prueba el mensaje de asiento agregado.
        """
        self.assertEqual(Mensajes.asiento_agregado(), "Asiento agregado correctamente.")

    def test_asiento_reservado(self):
        """
        Prueba el mensaje de asiento reservado.
        """
        self.assertEqual(Mensajes.asiento_reservado(), "Asiento reservado correctamente.")

    def test_reserva_cancelada(self):
        """
        Prueba el mensaje de reserva cancelada.
        """
        self.assertEqual(Mensajes.reserva_cancelada(), "Reserva cancelada correctamente.")

    def test_reporte_disponibilidad(self):
        """
        Prueba el mensaje de reporte de disponibilidad.
        """
        self.assertEqual(Mensajes.reporte_disponibilidad("lunes", 10, 5, 85), "Lunes: 10 asientos libres, 5 asientos reservados, 85 asientos no agregados.")

    def test_max_intentos(self):
        """
        Prueba el mensaje de número máximo de intentos alcanzado.
        """
        self.assertEqual(Mensajes.max_intentos(), "Número máximo de intentos alcanzado. Por favor, intente de nuevo más tarde.")

    def test_confirmar_reseteo(self):
        """
        Prueba el mensaje de confirmación de reseteo.
        """
        self.assertEqual(Mensajes.confirmar_reseteo(), "¿Está seguro de que desea resetear el estado? Esto borrará todos los datos. (si/no):")

    def test_reseteo_cancelado(self):
        """
        Prueba el mensaje de reseteo cancelado.
        """
        self.assertEqual(Mensajes.reseteo_cancelado(), "Reseteo de estado cancelado.")

    def test_confirmar_guardado(self):
        """
        Prueba el mensaje de confirmación de guardado.
        """
        self.assertEqual(Mensajes.confirmar_guardado(), "¿Desea guardar el estado actual antes de salir? (si/no):")

    def test_estado_guardado(self):
        """
        Prueba el mensaje de estado guardado.
        """
        self.assertEqual(Mensajes.estado_guardado(), "Estado guardado correctamente.")

    def test_estado_reseteado(self):
        """
        Prueba el mensaje de estado reseteado.
        """
        self.assertEqual(Mensajes.estado_reseteado(), "Estado reseteado correctamente.")

    def test_saliendo_sistema(self):
        """
        Prueba el mensaje de salida del sistema.
        """
        self.assertEqual(Mensajes.saliendo_sistema(), "Saliendo del sistema...")

    def test_ingrese_dia(self):
        """
        Prueba el mensaje para ingresar el día.
        """
        self.assertEqual(Mensajes.ingrese_dia(), "Ingrese el día (1: lunes, 2: martes, 3: miércoles, 4: jueves, 5: viernes, 6: sábado, 7: domingo): ")

    def test_ingrese_fila(self):
        """
        Prueba el mensaje para ingresar la fila.
        """
        self.assertEqual(Mensajes.ingrese_fila(), "Ingrese la fila: ")

    def test_ingrese_numero_asiento(self):
        """
        Prueba el mensaje para ingresar el número de asiento.
        """
        self.assertEqual(Mensajes.ingrese_numero_asiento(), "Ingrese el número de asiento: ")

    def test_dia_invalido(self):
        """
        Prueba el mensaje de día inválido.
        """
        self.assertEqual(Mensajes.dia_invalido(), "Día inválido. Por favor, intente de nuevo.")

    def test_asiento_no_encontrado(self):
        """
        Prueba el mensaje de asiento no encontrado.
        """
        self.assertEqual(Mensajes.asiento_no_encontrado(), "El asiento no se encuentra en el sistema.")

    def test_asiento_ya_reservado(self):
        """
        Prueba el mensaje de asiento ya reservado.
        """
        self.assertEqual(Mensajes.asiento_ya_reservado(), "El asiento ya está reservado.")

    def test_asiento_ya_existe(self):
        """
        Prueba el mensaje de asiento ya existente.
        """
        self.assertEqual(Mensajes.asiento_ya_existe(), "El asiento ya existe en el sistema.")

    def test_ingrese_edad(self):
        """
        Prueba el mensaje para ingresar la edad del espectador.
        """
        self.assertEqual(Mensajes.ingrese_edad(), "Ingrese la edad del espectador: ")

    def test_ingrese_nueva_fila(self):
        """
        Prueba el mensaje para ingresar la nueva fila.
        """
        self.assertEqual(Mensajes.ingrese_nueva_fila(), "Ingrese la nueva fila: ")

    def test_ingrese_nuevo_numero_asiento(self):
        """
        Prueba el mensaje para ingresar el nuevo número de asiento.
        """
        self.assertEqual(Mensajes.ingrese_nuevo_numero_asiento(), "Ingrese el nuevo número de asiento: ")

    def test_asiento_eliminado(self):
        """
        Prueba el mensaje de asiento eliminado.
        """
        self.assertEqual(Mensajes.asiento_eliminado(), "Asiento eliminado correctamente.")

    def test_asiento_actualizado(self):
        """
        Prueba el mensaje de asiento actualizado.
        """
        self.assertEqual(Mensajes.asiento_actualizado(), "Asiento actualizado correctamente.")

if __name__ == '__main__':
    unittest.main()