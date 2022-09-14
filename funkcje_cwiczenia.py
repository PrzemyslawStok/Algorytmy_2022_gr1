import timeit
import numpy as np
#import tensorflow as tf

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


def dict0():
    d0 = {"p0": 2}
    d0['p1'] = 10
    d0[0] = 11

    print(d0)

    print(f"{d0.keys()}")
    print(f"{d0.values()}")
    print(f"{d0.items()}")

    for key, value in d0.items():
        print(f"key: {key}, value: {value}")


def cw1():
    dict0 = {}
    for i in range(10):
        dict0[f"i_{i}"] = np.random.randint(0, 10)

    print(dict0)
    suma = 0
    for value in dict0.values():
        a = int(value)
        kwadrat = a ** 2
        print(f"{value}*{value}={kwadrat}")
        suma += kwadrat

    print(f"suma kwadratow={suma}")


def f3(**kwargs):
    for item in kwargs.items():
        print(item)


def cw2(**kwargs):
    sum = 0
    for value in kwargs.values():
        sum += float(value) ** 2

    return sum


def f5() -> (int, int):
    return 10, 1


def f6() -> (int, (int, int)):
    return 10, (1, 100)


def f7() -> ((int, int), ((int, float), str)):
    return (1, 10), (1, (5.2, "f7"))


if __name__ == "__main__":
    # parametry()
    # f2(1, 5, 10, "f0", "f1")
    # print(suma_parametrow(1, 2, 5, 6, 7))
    # dict0()
    # cw1()

    kwargs = {"a": 10}
    f3(a=10, b=5)

    # print(cw2(a=10, b=5))
    # print(f5())
    a, _ = f5()

    print(a)

    a, (b, c) = f6()
    print(c)

    a = f7()
    print(a)
