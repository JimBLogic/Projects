import unittest
from mensajes import Mensajes

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
        self.assertEqual(Mensajes.reporte_disponibilidad("lunes", 5, 3, 92), "Lunes: 5 asientos libres, 3 asientos reservados, 92 asientos no agregados.")

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
        self.assertEqual(Mensajes.ingrese_fila(), "Ingrese la fila: ")

    def test_ingrese_numero_asiento(self):
        self.assertEqual(Mensajes.ingrese_numero_asiento(), "Ingrese el número de asiento: ")

    def test_dia_invalido(self):
        self.assertEqual(Mensajes.dia_invalido(), "Día inválido. Por favor, intente de nuevo.")

    def test_error_generico(self):
        self.assertEqual(Mensajes.error_generico(), "Ha ocurrido un error. Por favor, intente de nuevo más tarde.")

    def test_asiento_no_encontrado(self):
        self.assertEqual(Mensajes.asiento_no_encontrado(), "El asiento no se encuentra en el sistema.")

    def test_asiento_ya_reservado(self):
        self.assertEqual(Mensajes.asiento_ya_reservado(), "El asiento ya está reservado.")

if __name__ == '__main__':
    unittest.main()