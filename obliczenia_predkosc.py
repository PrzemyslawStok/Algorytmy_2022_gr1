import timeit


def mnozenie(l=100_000) -> list:
    A = []
    for i in range(l):
        A.append(1)

    for i in range(l):
        for j in range(10):
            A[i] = A[i] * 10

    return A


if __name__ == "__main__":
    A = mnozenie()
