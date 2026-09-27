"""
Universidad del Valle de Guatemala
Facultad de Ingenieria
Ciencia de la Computacion y Tecnologias de la Informacion
CC2019 - Teoria de la Computacion
Seccion 30
Semestre 2, 2026

Laboratorio #7 - Ejercicio 2
Modulo: algoritmo_c - profiling del algoritmo c) del ejercicio 1

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
c) del ejercicio 1 para los tamanos de entrada indicados. Por su
complejidad O(n^2), el tamano mas grande puede exceder el limite de
tiempo practico definido en profiling_utils.py (TIMEOUT_SECONDS) y
quedar marcado como N/A (timeout) en la tabla; esto es un resultado
esperado, no un error.

Instalacion:
pip install matplotlib

Ejecucion:
python algoritmo_c.py
"""

import time

from profiling_utils import perfilar, imprimir_tabla, graficar, CHEQUEO_CADA


def algoritmo_c(n, inicio=None, timeout=None):
    ops = 0
    i = 1
    while i <= n // 3:
        j = 1
        while j <= n:
            ops += 1  # equivale a printf("Sequence\n")
            j += 4
            if timeout is not None and ops % CHEQUEO_CADA == 0:
                if time.perf_counter() - inicio > timeout:
                    return None
        i += 1
    return ops


if __name__ == "__main__":
    resultados = perfilar(algoritmo_c)
    imprimir_tabla("c", resultados)
    graficar("c", resultados, "algoritmo_c_grafica.png")