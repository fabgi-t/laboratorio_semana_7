"""EJERCICIO 02 — Preparar un catálogo

ENUNCIADO
Cada producto tiene nombre, precio y categoria. Los nombres son únicos.
Devuelve un diccionario con:
- disponibles: lista de nombres con precio <= 20, en el orden original.
- precios: diccionario nombre -> precio de todos los productos.
- categorias: set de todas las categorías.
Usa una comprensión para cada estructura. No uses ciclos explícitos.
No modifiques la entrada. Para [] devuelve las tres estructuras vacías.

Con los datos entregados se espera:
{"disponibles": ["cafe", "te"],
 "precios": {"cafe": 10, "torta": 25, "te": 8},
 "categorias": {"bebida", "postre"}}
El orden de los elementos del set puede cambiar.

ENTREGA
Completa la implementación sin cambiar los nombres ni los parámetros.
Ejecuta el archivo y compara lo impreso con el resultado del enunciado.
Añade al menos otro ejemplo usando print y escribe en un comentario qué esperas.
Al terminar: git commit -m "Resuelve ejercicio 02".
"""

"""EJERCICIO 02 — Preparar un catálogo
(enunciado igual que el original)
"""

def preparar_catalogo(productos):
    # Lista de nombres con precio <= 20, en el orden original
    disponibles = [p["nombre"] for p in productos if p["precio"] <= 20]

    # Diccionario nombre -> precio de todos los productos
    precios = {p["nombre"]: p["precio"] for p in productos}

    # Set con todas las categorías (sin repetir)
    categorias = {p["categoria"] for p in productos}

    resultado = {
        "disponibles": disponibles,
        "precios": precios,
        "categorias": categorias,
    }
    return resultado


# Ejemplo de uso del enunciado
productos = [
    {"nombre": "cafe", "precio": 10, "categoria": "bebida"},
    {"nombre": "torta", "precio": 25, "categoria": "postre"},
    {"nombre": "te", "precio": 8, "categoria": "bebida"},
]
print(preparar_catalogo(productos))
# Esperado: {'disponibles': ['cafe', 'te'],
#            'precios': {'cafe': 10, 'torta': 25, 'te': 8},
#            'categorias': {'bebida', 'postre'}}
# (el orden de los elementos del set puede cambiar)

# Otro ejemplo
productos2 = [
    {"nombre": "pan", "precio": 3, "categoria": "panaderia"},
    {"nombre": "queso", "precio": 22, "categoria": "lacteo"},
    {"nombre": "leche", "precio": 20, "categoria": "lacteo"},
    {"nombre": "jugo", "precio": 12, "categoria": "bebida"},
]
print(preparar_catalogo(productos2))
# Esperado: {'disponibles': ['pan', 'leche', 'jugo'],
#            'precios': {'pan': 3, 'queso': 22, 'leche': 20, 'jugo': 12},
#            'categorias': {'panaderia', 'lacteo', 'bebida'}}
# (leche cuesta exactamente 20, y como la condición es <= 20, sí entra)

# Caso lista vacía
print(preparar_catalogo([]))
# Esperado: {'disponibles': [], 'precios': {}, 'categorias': set()}
