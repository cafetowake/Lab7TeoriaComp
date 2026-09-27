"""
Universidad del Valle de Guatemala
Facultad de Ingenieria
Ciencia de la Computacion y Tecnologias de la Informacion
CC2019 - Teoria de la Computacion
Seccion 30
Semestre 2, 2026

Laboratorio #7 - Ejercicio 2
Modulo: algoritmo_b - profiling del algoritmo b) del ejercicio 1

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
b) del ejercicio 1 para los tamanos de entrada indicados.

Instalacion:
pip install matplotlib

Ejecucion:
python algoritmo_b.py
"""

import time

from profiling_utils import perfilar, imprimir_tabla, graficar, CHEQUEO_CADA


def algoritmo_b(n, inicio=None, timeout=None):
    ops = 0
    if n <= 1:
        return ops
    i = 1
    while i <= n:
        j = 1
        while j <= n:
            ops += 1  # equivale a printf("Sequence\n")
            break
        i += 1
        if timeout is not None and ops % CHEQUEO_CADA == 0:
            if time.perf_counter() - inicio > timeout:
                return None
    return ops


if __name__ == "__main__":
    resultados = perfilar(algoritmo_b)
    imprimir_tabla("b", resultados)
    graficar("b", resultados, "algoritmo_b_grafica.png")