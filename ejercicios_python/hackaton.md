# Problema: Optimizador de Rutas de Recolección de Residuos

## Descripción del Problema
Tu ciudad necesita un sistema para optimizar las rutas de los camiones recolectores de residuos. Actualmente, los camiones siguen rutas predefinidas, pero esto no es eficiente porque no todos los contenedores se llenan al mismo ritmo. Quieren un software que genere rutas dinámicas basadas en las necesidades reales de cada contenedor.

### Requisitos

- Los contenedores de basura están distribuidos en coordenadas geográficas (latitud, longitud).
- Cada contenedor tiene sensores que reportan el nivel de llenado, un número entre 0 y 100%.
- Los camiones recolectores tienen una capacidad limitada en volumen (por ejemplo, 10 toneladas).
- Se debe generar una ruta eficiente para uno o más camiones, minimizando la distancia recorrida y asegurando que se recojan los contenedores más llenos primero.
- Si no es posible recoger todos los contenedores en una sola salida (debido a la capacidad del camión), el sistema debe planificar múltiples salidas.

---

## Entradas

- **Lista de contenedores**:
  - ID del contenedor.
  - Coordenadas (latitud, longitud).
  - Nivel de llenado (0-100%).
  - Capacidad máxima del contenedor (en kg).

- **Capacidad de cada camión** (en kg).
- **Ubicación inicial del camión** (por defecto, el centro de operaciones).

### Ejemplo de Entrada
```python
contenedores = [
    {"id": 1, "lat": 19.432608, "lon": -99.133209, "nivel": 80, "capacidad": 500},  # Contenedor lleno
    {"id": 2, "lat": 19.434105, "lon": -99.145646, "nivel": 60, "capacidad": 400},  # Contenedor priorizado
    {"id": 3, "lat": 19.440234, "lon": -99.127659, "nivel": 20, "capacidad": 600},  # Contenedor casi vacío
    {"id": 4, "lat": 19.427005, "lon": -99.138674, "nivel": 90, "capacidad": 300},  # Contenedor muy lleno
    {"id": 5, "lat": 19.436551, "lon": -99.150426, "nivel": 40, "capacidad": 350}   # Contenedor medio lleno
]

capacidad_camion = 1000
centro_operaciones = {"lat": 19.432608, "lon": -99.133209}



FUNCION optimizar_rutas(contenedores, capacidad_camion, centro_operaciones)
    # Paso 1: Filtrar contenedores con nivel >= 50%
    contenedores_prioritarios ← FILTRAR(contenedores DONDE nivel >= 50)
    
    # Paso 2: Ordenar contenedores por nivel de llenado (descendente)
    ORDENAR(contenedores_prioritarios POR nivel DECRECIENTE)

    rutas ← []  # Lista para guardar las rutas generadas
    camion_actual ← {"ruta": [], "carga_actual": 0, "distancia_recorrida": 0}
    ubicacion_actual ← centro_operaciones

    # Paso 3: Iterar sobre los contenedores prioritarios
    PARA CADA contenedor EN contenedores_prioritarios
        peso_contenedor ← (nivel / 100) * capacidad_contenedor

        SI camion_actual.carga_actual + peso_contenedor <= capacidad_camion ENTONCES
            # Añadir el contenedor al camión actual
            distancia ← calcular_distancia(ubicacion_actual, contenedor)
            camion_actual.ruta.AÑADIR(contenedor.id)
            camion_actual.carga_actual ← camion_actual.carga_actual + peso_contenedor
            camion_actual.distancia_recorrida ← camion_actual.distancia_recorrida + distancia
            ubicacion_actual ← contenedor
        SINO
            # Si el camión está lleno, guardar la ruta actual y empezar una nueva
            rutas.AÑADIR(camion_actual)
            camion_actual ← {"ruta": [], "carga_actual": 0, "distancia_recorrida": 0}
            ubicacion_actual ← centro_operaciones
    FIN PARA

    # Paso 4: Añadir la última ruta si el camión no está vacío
    SI camion_actual.ruta NO ESTA VACÍA ENTONCES
        rutas.AÑADIR(camion_actual)

    RETORNAR rutas
FIN FUNCION


FUNCION calcular_distancia(punto1, punto2)
    # Fórmula de Haversine para calcular distancia entre dos coordenadas geográficas
    R ← 6371  # Radio de la Tierra en kilómetros
    delta_lat ← radianes(punto2.lat - punto1.lat)
    delta_lon ← radianes(punto2.lon - punto1.lon)
    a ← (SIN(delta_lat/2)^2) + COS(radianes(punto1.lat)) * COS(radianes(punto2.lat)) * (SIN(delta_lon/2)^2)
    c ← 2 * ARCTAN2(RAIZ(a), RAIZ(1-a))
    RETORNAR R * c
FIN FUNCION



contenedores ← [
    {id: 1, lat: ..., lon: ..., nivel: ..., capacidad: ...},
    {id: 2, lat: ..., lon: ..., nivel: ..., capacidad: ...},
    ...
]
capacidad_camion ← 1000
centro_operaciones ← {lat: ..., lon: ...}

rutas ← optimizar_rutas(contenedores, capacidad_camion, centro_operaciones)

# Mostrar las rutas generadas
PARA CADA ruta EN rutas
    IMPRIMIR("Camión:")
    IMPRIMIR("  Contenedores recolectados:", ruta.ruta)
    IMPRIMIR("  Carga total:", ruta.carga_actual, "kg")
    IMPRIMIR("  Distancia total recorrida:", ruta.distancia_recorrida, "km")
FIN PARA
