import numpy as np


def wyznacznik3():
    A = np.array([[2, 0, 1], [0, 0, 1], [1, 2, -1]])
    print(A)

    print(np.linalg.det(A))


def wyznacznik4():
    A = np.array([[1, 2, 0, 1], [1, 1, 2, 0], [2, 0, 0, 1], [1, 0, 1, 0]])
    print(A)
    print(A.diagonal())

    A[3, 3] = 10
    A[2, 3] = 10

    A[0, 0] = 5
    A[1, 1] = 5
    A[2, 2] = 5
    A[3, 3] = 5

    print(A)

    for i in range(len(A)):
        A[i, i] = 0

    print(A)


def macierz1():
    A = np.array([[1, 2, 0, 1], [1, 1, 2, 0], [2, 0, 5, 1], [1, 0, 1, 7]])
    print(A)

    print(np.diag(A))

    B = np.eye(4)
    print(B)

    print(A * B)
    print(np.diag(np.diag(A)))

    print(A * np.eye(len(A)))


def macierz2():
    A = np.zeros([5, 3])
    print(A)
    A = np.ones([5, 3])
    print(A)

    A = np.random.random([5, 3])
    print(A)

    A = np.random.rand(5, 3)
    print(A)

    A = np.arange(0, 10)

    print(A)


def zad1():
    # proszę utworzyć macierz losowych elementów 10x10 i policzyć wyznacznik
    A = np.random.random([100, 100])
    print(A)
    print(np.linalg.det(A))


if __name__ == "__main__":
    #np.set_printoptions(precision=1)
    # wyznacznik3()
    # wyznacznik4()
    # macierz1()
    # macierz2()
    zad1()
