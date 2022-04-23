import numpy as np


def funkcja1():
    A = np.arange(1, 10)
    print(A)
    print(A[0])

    for i in range(5, 9):
        print(A[i])

    print(A[:7])
    print(A[2:])
    print(A[2:5])


def funkcja2():
    A = np.arange(0, 100)
    B = A.reshape([10, -1])

    print(B)
    print("")

    print(B[:2, :])
    print(B[:, :2])

    # zad 35-78
    print(B[3:8, 5:9])


def funkcja3():
    A = np.arange(0, 10)
    # B = A.reshape([10, -1])

    print(A)
    print(A[0:2])
    print(A[2:])

    B = np.arange(1, 6)

    print(B)
    a = 2
    print(B[:a])
    print(B[a:])


def podzial1(A: np.ndarray, a=90) -> (np.ndarray, np.ndarray):
    A = np.zeros(10)
    B = np.zeros(10)
    return A, B


if __name__ == "__main__":
    # funkcja1()
    # funkcja2()

    A, B = podzial1(np.arange(0, 100), 50)
    print(A)
    print(B)
