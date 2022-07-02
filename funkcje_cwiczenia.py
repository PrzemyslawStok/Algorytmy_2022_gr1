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


def f1() -> ((int, int, (int, int)), (int, int)):
    return ((10, 5, (3, 2)), (2, 7))


def parametry():
    a, b = f0()
    print(f"a={a}, b={b}")

    print(f0())

    a, (b, c) = f0()

    print(f"a={a}, b={b}, c={c}")

    a, _ = f0()

    print(f"a={a}")

    a, (b, _) = f0()

    print(f"a={a}, b={b}")


def f2(*args):
    for a in args:
        print(a)


def suma_parametrow(p0, p1, *args):
    print(f"p0={p0}")
    print(f"p1={p1}")

    sum = 0
    for a in args:
        sum += a
    return sum


if __name__ == "__main__":
    # parametry()

    # f2(1, 5, 10, "f0", "f1")

    print(suma_parametrow(1, 2, 5, 6, 7))
