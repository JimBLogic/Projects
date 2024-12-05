import unittest
from unittest.mock import patch
from contextlib import redirect_stdout
import io
import os
import json

# Importar el archivo principal
from V8ReservaCine import main, reset_estado, cargar_estado, guardar_estado

class TestReservaCineBot(unittest.TestCase):
    def setUp(self):
        # Resetear el estado antes de cada prueba
        if os.path.exists("estado_sala.json"):
            os.remove("estado_sala.json")

    def test_agregar_asiento_individual(self):
        inputs = iter([
            '1', '1', '1', '1', '1', '5', 'no'
        ])
        with patch('builtins.input', lambda _: next(inputs)):
            with redirect_stdout(io.StringIO()) as stdout:
                main()
            output = stdout.getvalue()
            self.assertIn("Asiento 1 en fila 1 para el día lunes agregado correctamente.", output)

    def test_agregar_fila_completa(self):
        inputs = iter([
            '1', '2', '1', '1', '5', 'no'
        ])
        with patch('builtins.input', lambda _: next(inputs)):
            with redirect_stdout(io.StringIO()) as stdout:
                main()
            output = stdout.getvalue()
            self.assertIn("Asiento 1 en fila 1 para el día lunes agregado correctamente.", output)
            self.assertIn("Asiento 20 en fila 1 para el día lunes agregado correctamente.", output)

    def test_agregar_todos_asientos_dia(self):
        inputs = iter([
            '1', '3', '1', '5', 'no'
        ])
        with patch('builtins.input', lambda _: next(inputs)):
            with redirect_stdout(io.StringIO()) as stdout:
                main()
            output = stdout.getvalue()
            self.assertIn("Asiento 1 en fila 1 para el día lunes agregado correctamente.", output)
            self.assertIn("Asiento 20 en fila 10 para el día lunes agregado correctamente.", output)

    def test_agregar_todos_asientos_semana(self):
        inputs = iter([
            '1', '4', '5', 'no'
        ])
        with patch('builtins.input', lambda _: next(inputs)):
            with redirect_stdout(io.StringIO()) as stdout:
                main()
            output = stdout.getvalue()
            self.assertIn("Asiento 1 en fila 1 para el día lunes agregado correctamente.", output)
            self.assertIn("Asiento 20 en fila 10 para el día domingo agregado correctamente.", output)

    def test_reservar_asiento(self):
        inputs = iter([
            '1', '1', '1', '1', '1', '2', '1', '1', '1', '65', '5', 'no'
        ])
        with patch('builtins.input', lambda _: next(inputs)):
            with redirect_stdout(io.StringIO()) as stdout:
                main()
            output = stdout.getvalue()
            self.assertIn("Asiento 1 en fila 1 reservado.", output)

    def test_cancelar_reserva(self):
        inputs = iter([
            '1', '1', '1', '1', '1', '2', '1', '1', '1', '65', '3', '1', '1', '1', '5', 'no'
        ])
        with patch('builtins.input', lambda _: next(inputs)):
            with redirect_stdout(io.StringIO()) as stdout:
                main()
            output = stdout.getvalue()
            self.assertIn("Asiento 1 en fila 1 ahora está disponible.", output)

    def test_mostrar_asientos(self):
        inputs = iter([
            '1', '1', '1', '1', '1', '4', '5', 'no'
        ])
        with patch('builtins.input', lambda _: next(inputs)):
            with redirect_stdout(io.StringIO()) as stdout:
                main()
            output = stdout.getvalue()
            self.assertIn("Asiento 1, Fila 1, Día: lunes, Precio: €0.00, Estado: Disponible, Edad: 0, Descuentos: Sin descuentos", output)

    def test_reset_estado(self):
        inputs = iter([
            '1', '1', '1', '1', '1', '6', 'si', '4', '5', 'no'
        ])
        with patch('builtins.input', lambda _: next(inputs)):
            with redirect_stdout(io.StringIO()) as stdout:
                main()
            output = stdout.getvalue()
            self.assertIn("Estado reseteado correctamente.", output)
            self.assertIn("No hay asientos disponibles aún.", output)

    def test_guardar_y_cargar_estado(self):
        inputs = iter([
            '1', '1', '1', '1', '1', '5', 'si', '4', '5', 'no'
        ])
        with patch('builtins.input', lambda _: next(inputs)):
            with redirect_stdout(io.StringIO()) as stdout:
                main()
            output = stdout.getvalue()
            self.assertIn("Estado guardado correctamente.", output)
            self.assertIn("Estado cargado correctamente.", output)

if __name__ == '__main__':
    with open('test_log.txt', 'w') as f:
        with redirect_stdout(f):
            unittest.main()