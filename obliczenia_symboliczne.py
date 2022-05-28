from sympy import symbols, pprint, sqrt
import sympy

if __name__ == "__main__":
    x = symbols("x")
    y = x * (x + 1) + sympy.sin(x)
    pprint(y)
    integral1 = sympy.integrate(y, x)
    pprint(integral1)

    y = (x + sympy.sin(x)) ** 10
    integral2 = sympy.integrate(y, x)
    pprint(integral2)
