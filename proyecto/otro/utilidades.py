def calcular_descuento(precio_base, edad, dia):
    descuento = 0
    if dia.lower() == "miércoles":
        descuento += 0.20
    if edad >= 65:
        descuento += 0.30
    return descuento
