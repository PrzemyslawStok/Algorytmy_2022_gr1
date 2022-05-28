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

    X = np.linspace(-1, 1, 50)

    for a in A:
        Y = X ** a
        plot.plot(X, Y, label=rf"$y=x^{a}$")

    plot.legend()
    plot.show()


def sin_array(A: np.ndarray):
    X = np.linspace(-np.pi, np.pi, 200)

    for a in A:
        Y = a * np.sin(a * X)
        plot.plot(X, Y, label=rf"$y={a}sin({a}x)$")

    plot.legend()
    plot.show()


def sin_multiplot(A: np.ndarray, B: np.ndarray):
    fig = plot.figure(figsize=(5 * len(A), 5), dpi=100)
    grid_spac = fig.add_gridspec(1, len(A))
    subplots = grid_spac.subplots()

    X = np.linspace(-np.pi, np.pi, 200)

    Y = np.sin(X)

    for i in range(len(A)):
        a = A[i]
        Y = np.sin(a * X)
        subplots[i].plot(X, Y, label=rf"$y=sin({a}x)$")

    for i in range(len(A)):
        subplots[i].legend()

    plot.show()


if __name__ == "__main__":
    # zadanie1()
    # wielomiany(np.arange(1, 10))
    # sin_array(np.arange(1, 6))
    sin_multiplot(np.arange(1, 3), np.array([1, 2, 10]))
