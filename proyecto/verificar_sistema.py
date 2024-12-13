import logging
import subprocess
import os
import json

# Configurar el logger para el archivo de verificación
logging.basicConfig(filename='verificacion.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def ejecutar_tests():
    """
    Ejecuta los tests del sistema y registra los resultados.
    """
    logging.info("Ejecutando tests...")
    result = subprocess.run(["python", "-m", "unittest", "discover"], capture_output=True, text=True)
    logging.info("Resultado de los tests:\n%s", result.stdout)
    if result.returncode != 0:
        logging.error("Algunos tests fallaron:\n%s", result.stderr)
    else:
        logging.info("Todos los tests pasaron correctamente.")

def revisar_debug_log():
    """
    Revisa el archivo debug.log en busca de errores.
    """
    logging.info("Revisando debug.log...")
    try:
        with open('debug.log', 'r') as file:
            contenido = file.read()
            if "ERROR" in contenido:
                logging.error("Se encontraron errores en debug.log.")
            else:
                logging.info("debug.log no contiene errores inesperados.")
    except FileNotFoundError:
        logging.error("debug.log no encontrado.")

def probar_programa():
    """
    Ejecuta el programa principal para pruebas manuales.
    """
    logging.info("Ejecutando el programa para pruebas manuales...")
    result = subprocess.run(['python', 'main.py'], capture_output=True, text=True)
    logging.info(f"Salida del programa:\n{result.stdout}")
    if result.returncode != 0:
        logging.error(f"El programa encontró errores:\n{result.stderr}")

def crear_archivo_estado():
    """
    Crea el archivo de estado inicial si no existe.
    """
    if not os.path.exists('estado_sala.json'):
        with open('estado_sala.json', 'w') as file:
            json.dump({}, file)
        logging.info("Archivo de estado inicial creado.")

def cargar_archivo_estado():
    """
    Carga el archivo de estado si existe.
    """
    if os.path.exists('estado_sala.json'):
        with open('estado_sala.json', 'r') as file:
            return json.load(file)
    return {}

def main():
    """
    Función principal que ejecuta las verificaciones del sistema.
    """
    crear_archivo_estado()
    estado = cargar_archivo_estado()
    # Lista de funciones a ejecutar
    funciones = [ejecutar_tests, revisar_debug_log, probar_programa]
    total_tareas = len(funciones)

    # Ejecutar cada función en la lista
    for i, funcion in enumerate(funciones, start=1):
        logging.info(f"Ejecutando tarea {i} de {total_tareas}: {funcion.__name__}")
        try:
            funcion()
        except Exception as e:
            logging.error(f"Error al ejecutar {funcion.__name__}: {e}")
            print(f"Error al ejecutar {funcion.__name__}: {e}")

    logging.info("Verificación completa.")
    print("\nVerificación completa.")

if __name__ == "__main__":
    main()