
# Sistema Inteligente de Rutas - TransMiCable y TransMilenio (Bogotá)

Proyecto desarrollado para la Actividad 2 - Búsqueda y sistemas basados en reglas. Este sistema permite encontrar la mejor ruta de viaje entre Ciudad Bolívar (Mirador del Paraíso) y la Troncal Caracas Sur (Restrepo) usando reglas lógicas y búsqueda heurística (algoritmo A*).


## Estructura del Proyecto
- **conocimiento.py**: Contiene las estaciones, ubicaciones y tiempos base de los tramos.
- **reglas.py**: Contiene las condiciones lógicas del sistema (restricción horaria de expresos, alerta por vientos en el cable, tiempos de espera y validación de transbordo con tarjeta TuLlave).
- **buscador.py**: Ejecuta el algoritmo A* para calcular la ruta óptima y muestra el resultado en consola.

## Requisitos
- Python 3.8 o superior (utiliza únicamente librerías estándar: `heapq` y `math`).

## Instrucciones de Ejecución
1. Clonar este repositorio:
   
   git clone https://github.com/LadyCortes/SISTEMA-INTELIGENTE-RUTAS-BOGOTA
   
2. Ingresar a la carpeta del proyecto:
   
   cd SISTEMA-INTELIGENTE-RUTAS-BOGOTA
   
3. Ejecutar el sistema desde la terminal:
   
   python buscador.py
   