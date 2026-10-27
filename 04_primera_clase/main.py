"""EJERCICIO 04 — Funciones como valores y argumentos

ENUNCIADO
Completa aplicar_operacion: recibe una lista y una función; aplica esa
función a cada elemento usando un ciclo y devuelve una lista.
Completa transformar: crea un diccionario de funciones lambda con las claves
"doble", "cuadrado" y "negativo". Usa aplicar_operacion para obtener
un diccionario con esas mismas claves y las listas transformadas.
No uses map ni modifiques la lista original.
Con [] cada lista del resultado debe estar vacía.

Entrada de transformar: [1, 2, 3]
Resultado esperado:
{"doble": [2, 4, 6], "cuadrado": [1, 4, 9], "negativo": [-1, -2, -3]}

Entrada de aplicar_operacion: [2, 4] y una función que sume 1.
Resultado esperado: [3, 5]

ENTREGA
Completa la implementación sin cambiar los nombres ni los parámetros.
Ejecuta el archivo y compara lo impreso con el resultado del enunciado.
Añade al menos otro ejemplo usando print y escribe en un comentario qué esperas.
Al terminar: git commit -m "Resuelve ejercicio 04".
"""

"""EJERCICIO 04 — Funciones como valores y argumentos
(enunciado igual que el original)
"""

def aplicar_operacion(valores, operacion):
    resultado = []

    for valor in valores:
        nuevo = operacion(valor)
        resultado.append(nuevo)

    return resultado


def transformar(valores):
    operaciones = {
        "doble": lambda x: x * 2,
        "cuadrado": lambda x: x * x,
        "negativo": lambda x: -x,
    }

    resultado = {}

    for nombre in operaciones:
        funcion = operaciones[nombre]
        resultado[nombre] = aplicar_operacion(valores, funcion)

    return resultado


valores = [1, 2, 3]
print(transformar(valores))
# Esperado: {'doble': [2, 4, 6], 'cuadrado': [1, 4, 9], 'negativo': [-1, -2, -3]}

# f)1
print(aplicar_operacion([2, 4], lambda x: x + 1))
# Esperado: [3, 5]

# EjemX
print(transformar([5, -2, 0]))
# Esperado: {'doble': [10, -4, 0], 'cuadrado': [25, 4, 0], 'negativo': [-5, 2, 0]}
# (el negativo de 0 es 0, y el negativo de -2 es 2)

# Caso lista vacía
print(transformar([]))
# Esperado: {'doble': [], 'cuadrado': [], 'negativo': []}ado esperado en un comentario.
