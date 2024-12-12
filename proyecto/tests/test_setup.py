import os
import json

def reset_estado_sala():
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