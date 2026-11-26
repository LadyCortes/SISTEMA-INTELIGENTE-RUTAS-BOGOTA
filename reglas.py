from conocimiento import NODOS

def evaluar_reglas_transito(origen, destino, tipo_servicio, hora, alerta_viento):
    # REGLA 1: Disponibilidad de infraestructura (estaciones abiertas)
    if not NODOS[origen]["abierto"] or not NODOS[destino]["abierto"]:
        return False, 0, "Estacion cerrada por mantenimiento"

    # REGLA 2: Horario de rutas expresas (operan de 5:00 a 22:00)
    if tipo_servicio == "expreso" and (hora < 5 or hora > 22):
        return False, 0, "Servicio expreso fuera de horario operativo"

    # REGLA 3: Condicion climatica en TransMiCable
    tiempo_extra = 0
    if tipo_servicio == "cabina" and alerta_viento:
        tiempo_extra += 4  # Reduccion de velocidad por vientos fuertes

    return True, tiempo_extra, "OK"

def calcular_penalizacion_transbordo(sistema_origen, sistema_destino, servicio_anterior, servicio_nuevo):
    # REGLA 4: Cambio modal entre Cable Aereo y TransMilenio (caminata en portal)
    if sistema_origen != sistema_destino:
        return 5
    # REGLA 5: Cambio de bus dentro de la misma troncal (espera en vagon)
    if servicio_anterior is not None and servicio_anterior != servicio_nuevo:
        return 3
    return 0

def calcular_costo_tullave(sistema_origen, sistema_destino, minutos_desde_ultimo_viaje):
    # REGLA 6: Beneficio tarjeta TuLlave (transbordo a $0 si pasan <= 110 minutos)
    if sistema_origen != sistema_destino:
        if minutos_desde_ultimo_viaje <= 110:
            return 0
        else:
            return 3500
    return 0