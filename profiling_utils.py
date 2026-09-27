"""
Universidad del Valle de Guatemala
Facultad de Ingenieria
Ciencia de la Computacion y Tecnologias de la Informacion
CC2019 - Teoria de la Computacion
Seccion 30
Semestre 2, 2026

Laboratorio #7 - Ejercicio 2
Modulo: profiling_utils - funciones comunes de profiling

Integrantes:
Nombre: Paula De Leon
Carnet: 23202

Nombre: Karen Pineda
Carnet: 231132

Nombre: 
Carnet: 

Fecha: 26/09/2026

Descripcion:
Funciones comunes de profiling (tiempo real y conteo de operaciones)
usadas por cada uno de los tres algoritmos del ejercicio 1: ejecutar la
funcion con distintos tamanos de entrada, imprimir la tabla de resultados
y generar la grafica comparativa de tiempo real contra operaciones.

Cada algoritmo revisa el tiempo transcurrido cada CHEQUEO_CADA
operaciones; si supera TIMEOUT_SECONDS, se detiene y devuelve None.
Cuando eso ocurre, ese tamano y los mayores quedan marcados como N/A
(timeout) en la tabla y ausentes de la grafica.
"""

import time
import matplotlib.pyplot as plt

TEST_SIZES = [1, 10, 100, 1000, 10000, 100000, 1000000]
TIMEOUT_SECONDS = 60  # limite practico de ejecucion por prueba
CHEQUEO_CADA = 5_000_000  # cada cuantas operaciones se revisa el tiempo transcurrido


def perfilar(func, tamanos=TEST_SIZES, timeout=TIMEOUT_SECONDS):
    resultados = []
    omitir_resto = False
    for n in tamanos:
        if omitir_resto:
            print(f"n={n}: omitido (el tamano anterior ya excedio el limite)")
            resultados.append((n, None, None))
            continue

        inicio = time.perf_counter()
        ops = func(n, inicio, timeout)
        tiempo = time.perf_counter() - inicio

        if ops is None:
            print(f"n={n}: excede {timeout}s, se omite este tamano y los mayores")
            resultados.append((n, None, None))
            omitir_resto = True
        else:
            print(f"n={n}: tiempo={tiempo:.6f}s, operaciones={ops}")
            resultados.append((n, tiempo, ops))

    return resultados


def imprimir_tabla(nombre, resultados):
    print(f"\nAlgoritmo {nombre}")
    print(f"{'n':>10} | {'tiempo (s)':>15} | {'operaciones':>15}")
    print("-" * 46)
    for n, tiempo, ops in resultados:
        t_str = f"{tiempo:.6f}" if tiempo is not None else "N/A (timeout)"
        o_str = str(ops) if ops is not None else "N/A"
        print(f"{n:>10} | {t_str:>15} | {o_str:>15}")


def graficar(nombre, resultados, archivo_salida):
    ns = [n for n, t, _ in resultados if t is not None]
    tiempos = [t for _, t, _ in resultados if t is not None]
    ns_ops = [n for n, _, o in resultados if o is not None]
    ops = [o for _, _, o in resultados if o is not None]

    fig, ax_tiempo = plt.subplots(figsize=(7, 5))
    ax_ops = ax_tiempo.twinx()

    ax_tiempo.plot(ns, tiempos, marker="o", color="tab:blue", label="Tiempo real (s)")
    ax_ops.plot(ns_ops, ops, marker="s", color="tab:red", label="Operaciones")

    ax_tiempo.set_xscale("log")
    ax_tiempo.set_yscale("log")
    ax_ops.set_yscale("log")
    ax_tiempo.set_xlabel("Tamaño de entrada (n)")
    ax_tiempo.set_ylabel("Tiempo real (s)", color="tab:blue")
    ax_ops.set_ylabel("Conteo de operaciones", color="tab:red")
    ax_tiempo.set_title(f"Algoritmo {nombre}: tiempo real vs. conteo de operaciones")

    lineas = ax_tiempo.get_legend_handles_labels()[0] + ax_ops.get_legend_handles_labels()[0]
    etiquetas = ax_tiempo.get_legend_handles_labels()[1] + ax_ops.get_legend_handles_labels()[1]
    ax_tiempo.legend(lineas, etiquetas, loc="upper left")

    ax_tiempo.grid(True, which="both", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(archivo_salida, dpi=150)
    plt.show()