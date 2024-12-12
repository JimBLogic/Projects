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
    with open("estado_sala.json", "w") as file:
        json.dump(estado_inicial, file)

reset_estado_sala()