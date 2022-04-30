import numpy as np
from matplotlib import pyplot as plot

if __name__ == "__main__":
    X = np.linspace(-2, 2, 50)
    Y = X * X

    plot.plot(X, Y, label=rf"$y=x^2$")
    Y = np.sin(X)
    plot.plot(X, Y, label=rf"y=sin(x)")

    plot.legend()
    plot.show()
