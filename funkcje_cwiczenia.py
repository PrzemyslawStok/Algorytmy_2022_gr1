import timeit
import numpy as np
import tensorflow as tf

from numba import jit


def tuple_list():
    A = (1, 2, 3, 4, 5, 6)
    print(A)

    A_list = list(A)

    A_list[1] = 10

    A_tuple = tuple(A_list)

    for a in A_tuple:
        print(a)


def f0() -> (int, (int, int)):
    return (10, (2, 5))


if __name__ == "__main__":
    a, b = f0()
    print(f"a={a}, b={b}")

    print(f0())
