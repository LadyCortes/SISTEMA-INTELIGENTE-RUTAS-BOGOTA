import heapq
import math
from conocimiento import NODOS, TRAMOS
from reglas import evaluar_reglas_transito, calcular_penalizacion_transbordo, calcular_costo_tullave

def heuristica_euclidiana(nodo_a, nodo_b):
    x1, y1 = NODOS[nodo_a]["coord"]
    x2, y2 = NODOS[nodo_b]["coord"]
    return round(math.hypot(x2 - x1, y2 - y1) * 1.5, 2)

def encontrar_ruta_optima(inicio, fin, hora_viaje=8, alerta_viento=False, min_tullave=30):
    # Cola de prioridad: (f_costo, g_tiempo, costo_dinero, nodo_actual, historial_ruta, servicio_actual)
    abiertos = [(0, 0, 3500, inicio, [], None)]
    visitados = {}

    while abiertos:
        f, g, costo_dinero, actual, ruta, serv_previo = heapq.heappop(abiertos)

        if actual == fin:
            return ruta, g, costo_dinero

        estado = (actual, serv_previo)
        if estado in visitados and visitados[estado] <= g:
            continue
        visitados[estado] = g

        for orig, dest, min_base, servicio, tipo in TRAMOS:
            if orig == actual:
                valido, extra_clima, _ = evaluar_reglas_transito(
                    orig, dest, tipo, hora_viaje, alerta_viento
                )
                if not valido:
                    continue

                penalizacion = calcular_penalizacion_transbordo(
                    NODOS[orig]["sistema"], NODOS[dest]["sistema"], serv_previo, servicio
                )
                costo_transbordo = calcular_costo_tullave(
                    NODOS[orig]["sistema"], NODOS[dest]["sistema"], min_tullave
                )

                nuevo_g = g + min_base + extra_clima + penalizacion
                nuevo_costo = costo_dinero + costo_transbordo
                nuevo_f = nuevo_g + heuristica_euclidiana(dest, fin)

                paso = {
                    "desde": orig,
                    "hasta": dest,
                    "servicio": servicio,
                    "tiempo_tramo": min_base + extra_clima,
                    "espera_transbordo": penalizacion,
                    "costo_extra": costo_transbordo
                }
                heapq.heappush(abiertos, (nuevo_f, nuevo_g, nuevo_costo, dest, ruta + [paso], servicio))

    return None, -1, 0

if __name__ == "__main__":
    print("=== SISTEMA INTELIGENTE DE RUTAS: TRANSMICABLE - TUNAL ===")
    origen = "Mirador del Paraiso"
    destino = "Restrepo"
    
    hora = int(input("Ingrese la hora del viaje (0 - 23): "))
    viento = input("Hay alerta de vientos fuertes en Ciudad Bolivar? (s/n): ").lower() == "s"
    min_tarjeta = int(input("Hace cuantos minutos valido su tarjeta TuLlave?: "))

    ruta, total_tiempo, total_pesos = encontrar_ruta_optima(origen, destino, hora, viento, min_tarjeta)

    if ruta:
        print(f"\nMejor ruta encontrada de '{origen}' a '{destino}':\n")
        for i, p in enumerate(ruta, 1):
            espera = f" (+{p['espera_transbordo']} min transbordo)" if p['espera_transbordo'] > 0 else ""
            print(f"{i}. {p['desde']} -> {p['hasta']} | Servicio: {p['servicio']} | Tiempo: {p['tiempo_tramo']} min{espera}")
        print(f"\nTIEMPO TOTAL ESTIMADO: {total_tiempo} minutos.")
        print(f"COSTO TOTAL PASAJE TULLAVE: ${total_pesos:,} COP.")
    else:
        print("\nNo fue posible calcular una ruta bajo las condiciones actuales.")