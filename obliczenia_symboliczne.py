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


def evaluate_f(sympy_lambda, T: np.ndarray) -> np.ndarray:
    array = sympy_lambda(T)
    if np.ndim(array) == 0:
        array = array * np.ones(np.shape(T))

    return array


if __name__ == "__main__":
    # calki()
    t = sym.symbols("t")

    x_t = t ** 2 / (t + 1) + 5 * t + 1
    v_t, a_t = przyspieszenie(x_t)

    pprint(x_t)
    pprint(v_t)
    pprint(a_t)

    x_t_f = sym.lambdify(t, x_t, "numpy")
    v_t_f = sym.lambdify(t, v_t, "numpy")
    a_t_f = sym.lambdify(t, a_t, "numpy")

    T = np.linspace(0, 10, 100)
    X_t = x_t_f(T)
    V_t = v_t_f(T)

    A_t = evaluate_f(a_t_f, T)

    plot.plot(T, X_t, label="$x(t)=" + sym.latex(x_t) + "$")
    plot.plot(T, V_t, label="$v(t)=" + sym.latex(v_t) + "$")
    plot.plot(T, A_t, label="$a(t)=" + sym.latex(a_t) + "$")

    plot.legend()
    plot.show()

    print(sym.latex(x_t))
