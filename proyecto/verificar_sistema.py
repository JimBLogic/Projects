import os
import subprocess
import logging
import time

# Configurar el logger para el archivo de verificación
logging.basicConfig(filename='verificacion.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def ejecutar_tests():
    """
    Ejecuta los tests y verifica que todos pasen sin errores.
    """
    logging.info("Ejecutando tests...")
    print("Ejecutando tests...")
    try:
        resultado = subprocess.run(['python', '-m', 'unittest', 'discover', '-s', 'tests'], capture_output=True, text=True)
        logging.info("Resultado de los tests:\n" + resultado.stdout)
        if resultado.returncode != 0:
            logging.error("Algunos tests fallaron:\n" + resultado.stderr)
            print("Algunos tests fallaron.")
        else:
            logging.info("Todos los tests pasaron correctamente.")
            print("Todos los tests pasaron correctamente.")
    except Exception as e:
        logging.error(f"Error al ejecutar los tests: {e}")
        print(f"Error al ejecutar los tests: {e}")

def revisar_debug_log():
    """
    Verifica que el archivo debug.log se haya generado correctamente y no contenga errores inesperados.
    """
    logging.info("Revisando debug.log...")
    print("Revisando debug.log...")
    if os.path.exists('debug.log'):
        with open('debug.log', 'r') as file:
            contenido = file.read()
            if "ERROR" in contenido or "Exception" in contenido:
                logging.error("Se encontraron errores en debug.log:\n" + contenido)
                print("Se encontraron errores en debug.log.")
            else:
                logging.info("debug.log no contiene errores inesperados.")
                print("debug.log no contiene errores inesperados.")
    else:
        logging.error("El archivo debug.log no se generó.")
        print("El archivo debug.log no se generó.")

def probar_programa():
    """
    Ejecuta el programa y realiza pruebas manuales.
    """
    logging.info("Ejecutando el programa para pruebas manuales...")
    print("Ejecutando el programa para pruebas manuales...")
    try:
        resultado = subprocess.run(['python', 'main.py'], capture_output=True, text=True)
        logging.info("Salida del programa:\n" + resultado.stdout)
        if resultado.returncode != 0:
            logging.error("El programa encontró errores:\n" + resultado.stderr)
            print("El programa encontró errores.")
        else:
            logging.info("El programa se ejecutó correctamente.")
            print("El programa se ejecutó correctamente.")
    except Exception as e:
        logging.error(f"Error al ejecutar el programa: {e}")
        print(f"Error al ejecutar el programa: {e}")

def mostrar_progreso(tarea, total_tareas, tarea_actual):
    """
    Muestra una barra de progreso simple basada en texto.

    Args:
        tarea (str): Nombre de la tarea actual.
        total_tareas (int): Número total de tareas.
        tarea_actual (int): Número de la tarea actual.
    """
    progreso = (tarea_actual / total_tareas) * 100
    barra = '#' * int(progreso // 2) + '-' * (50 - int(progreso // 2))
    print(f"\r[{barra}] {progreso:.2f}% - {tarea}", end='')

if __name__ == "__main__":
    # Lista de funciones a ejecutar
    funciones = [ejecutar_tests, revisar_debug_log, probar_programa]
    total_tareas = len(funciones)

    for i, funcion in enumerate(funciones, start=1):
        mostrar_progreso(funcion.__name__, total_tareas, i)
        funcion()
        time.sleep(1)  # Simulación de tiempo de espera para cada tarea

    print("\nVerificación completa.")
    logging.info("Verificación completa.")