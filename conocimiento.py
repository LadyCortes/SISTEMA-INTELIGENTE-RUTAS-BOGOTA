# NODOS DEL SISTEMA ( TRANSMICABLE + TRONCAL TUNAL)
NODOS = {
    "Mirador del Paraiso": {"sistema": "TransMiCable", "coord": (1, 1), "abierto": True},
    "Manitas":             {"sistema": "TransMiCable", "coord": (2, 2), "abierto": True},
    "Juan Pablo II":       {"sistema": "TransMiCable", "coord": (3, 3), "abierto": True},
    "Portal del Tunal":    {"sistema": "TransMilenio", "coord": (4, 4), "abierto": True},
    "Parque":              {"sistema": "TransMilenio", "coord": (5, 5), "abierto": True},
    "Biblioteca":          {"sistema": "TransMilenio", "coord": (6, 5), "abierto": True},
    "Santa Lucia":         {"sistema": "TransMilenio", "coord": (7, 6), "abierto": True},
    "Calle 40 Sur":        {"sistema": "TransMilenio", "coord": (8, 7), "abierto": True},
    "Restrepo":            {"sistema": "TransMilenio", "coord": (10, 9), "abierto": True},
}

# BASE DE CONEXIONES
TRAMOS = [
    ("Mirador del Paraiso", "Manitas", 5, "Cable Aereo", "cabina"),
    ("Manitas", "Juan Pablo II", 4, "Cable Aereo", "cabina"),
    ("Juan Pablo II", "Portal del Tunal", 5, "Cable Aereo", "cabina"),
    ("Portal del Tunal", "Parque", 3, "Ruta Facil 3", "corriente"),
    ("Parque", "Biblioteca", 2, "Ruta Facil 3", "corriente"),
    ("Biblioteca", "Santa Lucia", 4, "Ruta Facil 3", "corriente"),
    ("Portal del Tunal", "Santa Lucia", 6, "H21 / B21", "expreso"),
    ("Santa Lucia", "Calle 40 Sur", 3, "Ruta Facil 3", "corriente"),
    ("Calle 40 Sur", "Restrepo", 5, "Ruta Facil 3", "corriente"),
    ("Santa Lucia", "Restrepo", 5, "H75 / B75", "expreso"),
]

