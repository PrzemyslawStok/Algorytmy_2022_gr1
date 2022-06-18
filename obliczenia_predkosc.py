import timeit
import numpy as np
import tensorflow as tf

from numba import jit


def mnozenie(l=100_000) -> (list, float):
    start = timeit.default_timer()
    A = []
    for i in range(l):
        A.append(1)

    for i in range(l):
        for j in range(10):
            A[i] = A[i] * 10

    end = timeit.default_timer()

    return A, end - start


@jit
def mnozenie_numba(l=100_000) -> (list, float):
    A = []
    for i in range(l):
        A.append(1)

    for i in range(l):
        for j in range(10):
            A[i] = A[i] * 10

    return A, 0.0


def mnozenie_numpy(l=100_000) -> (np.ndarray, float):
    start = timeit.default_timer()

    A = np.ones(l)

    for i in range(10):
        A = A + 10

    end = timeit.default_timer()
    return A, end - start


@tf.function
def mnozenie_tensorflow(l=100_000) -> (np.ndarray, float):
    start = timeit.default_timer()

    A = tf.ones(l)

    for i in range(10):
        A = A + 10

    end = timeit.default_timer()
    return A, end - start


def zmierz_czas(f, l=100_000):
    start = timeit.default_timer()
    A, _ = f(l)
    end = timeit.default_timer()
    czas = end - start

    print(f"obliczenia zajęły: {czas:0.2}s")


if __name__ == "__main__":
    l = 100_000
    zmierz_czas(mnozenie, l)
    zmierz_czas(mnozenie_numpy, l)
    zmierz_czas(mnozenie_tensorflow, l)
    zmierz_czas(mnozenie_numba, l)
    zmierz_czas(mnozenie_numba, l)
