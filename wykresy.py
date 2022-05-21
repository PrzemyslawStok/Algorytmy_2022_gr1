import numpy as np
from matplotlib import pyplot as plot


def zadanie1():
    X = np.linspace(-2, 2, 50)
    Y = X * X
    a = 2
    plot.plot(X, Y, label=rf"$y=x^{a}$")
    Y = np.sin(X)
    plot.plot(X, Y, label=rf"y=sin(x)")

    plot.legend()
    plot.show()


def wielomiany(A: np.array):
    # [1,2]
    # y = x^1
    # y = x^2

    # y = x^a

    X = np.linspace(-2, 2, 50)

    for a in A:
        Y = X ** a
        plot.plot(X, Y, label=rf"$y=x^{a}$")

    plot.legend()
    plot.show()


if __name__ == "__main__":
    #zadanie1()
    wielomiany(np.arange(1, 5))
