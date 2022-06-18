import timeit
import numpy as np


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


def mnozenie_numpy(l=100_000) -> (np.ndarray, float):
    return None, 0.0


def zmierz_czas(f, l=100_000):
    A, czas = f(l)
    print(f"obliczenia zajęły: {czas:0.2}s")


if __name__ == "__main__":
    l = 100_000
    zmierz_czas(mnozenie, l)
    zmierz_czas(mnozenie_numpy, l)
