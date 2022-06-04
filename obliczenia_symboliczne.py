from sympy import symbols, pprint, sqrt
import sympy as sym
from matplotlib import pyplot as plot

import numpy as np


def calki():
    x = symbols("x")
    y = x * (x + 1) + sym.sin(x)
    # pprint(y)
    integral1 = sym.integrate(y, x)
    # pprint(integral1)

    y = (x + sym.sin(x)) ** 2
    integral2 = sym.integrate(y, x)

    # pprint(integral2)

    y = (sym.sin(x) + 1) / sym.cos(x) ** 5
    integral3 = sym.integrate(y, x)

    pprint(integral3)


def przyspieszenie(x_t: sym.core.Add):
    v_t = sym.diff(x_t, t)
    a_t = sym.diff(v_t, t)
    return v_t, a_t


if __name__ == "__main__":
    # calki()
    t = sym.symbols("t")

    x_t = 10 * sym.sin(t) + 5 * t + 1
    v_t, a_t = przyspieszenie(x_t)

    pprint(x_t)
    pprint(v_t)
    pprint(a_t)

    X_t = sym.lambdify(t, x_t, "numpy")
    V_t = sym.lambdify(t, v_t, "numpy")
    A_t = sym.lambdify(t, a_t, "numpy")

    T = np.linspace(0, 10, 100)

    X = X_t(T)

    plot.plot(T, X)
    plot.show()


