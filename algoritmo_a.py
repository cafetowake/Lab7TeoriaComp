"""
Universidad del Valle de Guatemala
Facultad de Ingenieria
Ciencia de la Computacion y Tecnologias de la Informacion
CC2019 - Teoria de la Computacion
Seccion 30
Semestre 2, 2026

Laboratorio #7 - Ejercicio 2
Modulo: algoritmo_a - profiling del algoritmo a) del ejercicio 1

Integrantes:
Nombre: Paula De Leon
Carnet: 23202

Nombre: Karen Pineda
Carnet: 231132

Nombre: 
Carnet: 

Fecha: 26/09/2026

Descripcion:
Cuenta las operaciones y mide el tiempo real de ejecucion del algoritmo
a) del ejercicio 1 para los tamanos de entrada indicados. Por su
complejidad O(n^2 log n), los tamanos mas grandes exceden el limite de
tiempo practico definido en profiling_utils.py (TIMEOUT_SECONDS) y
quedan marcados como N/A (timeout) en la tabla; esto es un resultado
esperado, no un error.

Instalacion:
pip install matplotlib

Ejecucion:
python algoritmo_a.py
"""

import time

from profiling_utils import perfilar, imprimir_tabla, graficar, CHEQUEO_CADA


def algoritmo_a(n, inicio=None, timeout=None):
    counter = 0
    ops = 0
    i = n // 2
    while i <= n:
        j = 1
        while j + n // 2 <= n:
            k = 1
            while k <= n:
                counter += 1
                ops += 1
                k *= 2
                if timeout is not None and ops % CHEQUEO_CADA == 0:
                    if time.perf_counter() - inicio > timeout:
                        return None
            j += 1
        i += 1
    return ops


if __name__ == "__main__":
    resultados = perfilar(algoritmo_a)
    imprimir_tabla("a", resultados)
    graficar("a", resultados, "algoritmo_a_grafica.png")