"""EJERCICIO 05 — Subtotales de pedidos

ENUNCIADO
Cada pedido es una tupla (producto, precio_unitario, cantidad).
Usa map con lambda para calcular precio_unitario * cantidad de cada pedido.
Devuelve una lista en el orden original. Convierte el resultado de map con list.
No uses ciclos ni comprensiones. Los valores son enteros no negativos.
Para [] devuelve [].

Entrada: [("cafe", 10, 2), ("te", 8, 3), ("torta", 25, 1)]
Resultado esperado: [20, 24, 25]

ENTREGA
Completa la implementación sin cambiar los nombres ni los parámetros.
Ejecuta el archivo y compara lo impreso con el resultado del enunciado.
Añade al menos otro ejemplo usando print y escribe en un comentario qué esperas.
Al terminar: git commit -m "Resuelve ejercicio 05".
"""

def calcular_subtotales(pedidos):
    # A cada pedido (producto, precio, cantidad) le calculamos precio * cantidad
    subtotales = list(map(lambda pedido: pedido[1] * pedido[2], pedidos))
    return subtotales


# Ejemplo de uso del enunciado
pedidos = [("cafe", 10, 2), ("te", 8, 3), ("torta", 25, 1)]
print(calcular_subtotales(pedidos))
# Esperado: [20, 24, 25]

# Otro ejemplo
pedidos2 = [("pan", 3, 4), ("leche", 20, 0), ("jugo", 12, 5)]
print(calcular_subtotales(pedidos2))
# Esperado: [12, 0, 60]
# (leche tiene cantidad 0, así que su subtotal es 0)

# Caso lista vacía
print(calcular_subtotales([]))
# Esperado: []
