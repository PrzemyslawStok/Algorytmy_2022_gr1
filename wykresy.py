import numpy as np
from matplotlib import pyplot as plot

if __name__ == "__main__":
    X = np.arange(1, 10)
    Y = X * X

    print(X)
    print(Y)

    plot.plot(X, Y)
    plot.show()
