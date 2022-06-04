from sympy import symbols, pprint, sqrt
import sympy as sym


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
    return v_t, None


if __name__ == "__main__":
    # calki()
    t = sym.symbols("t")

    x_t = t ** 2 + 5 * t + 1

    v_t, a_t = przyspieszenie(x_t)
    pprint(v_t)
    pprint(a_t)
