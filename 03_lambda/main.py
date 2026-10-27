"""EJERCICIO 03 — Precios con recargo

ENUNCIADO
Dentro de la función, define una lambda que reciba un precio y devuelva
ese precio con un recargo del 10 %, redondeado a dos decimales con round.
Aplica la lambda mediante un ciclo y devuelve una lista.
No uses map todavía. Los precios son no negativos. No modifiques la entrada.
Para [] devuelve [].

Entrada: [10, 20, 35]
Resultado esperado: [11.0, 22.0, 38.5]

ENTREGA
Completa la implementación sin cambiar los nombres ni los parámetros.
Ejecuta el archivo y compara lo impreso con el resultado del enunciado.
Añade al menos otro ejemplo usando print y escribe en un comentario qué esperas.
Al terminar: git commit -m "Resuelve ejercicio 03".
"""

def calcular_importes(precios):
    recargo = lambda precio: round(precio * 1.10, 2)
    importes = []
    for precio in precios:
        importes.append(recargo(precio))
    return importes


# Ejemplo de uso: inicialmente imprime None porque falta la implementación.
precios = [10, 20, 35]
print(calcular_importes(precios))

# Otro ejemplo
precios2 = [5, 15, 25]
print(calcular_importes(precios2))
