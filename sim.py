# import stuff
import numpy as np
import math


def r(m):
    return 1 / math.sqrt(2) * (1 - 2 * c(2 * m)) + 1j * 1 / math.sqrt(2) * (
        1 - 2 * c(2 * m)
    )


def c(limit):
    vector = np.zeros(limit)

    Nc = 1600
    # n = 0,1,2...,M_pn-1
    for n in range(limit):
        vector[n] = (X1(n + Nc) + X2(n + Nc)) % 2

    return vector


def X1(n):
    # initialise
    X = np.zeros(n)
    X[0] = 1

    # cyclic shifting
    for i in range(n - 31):
        X[i + 31] = (X[i + 3] + X[i]) % 2

    return X[n - 1]


def X2(n):
    X = np.zeros(n)

    c_init = C_init(5, 6, 7, 8)  # arbitrary numbers
    c_init_b = format(c_init, "31b")
    c_init_b = c_init_b.replace(" ", "0")

    for i in range(31):
        X[i] = c_init_b[-1 - i]

    for i in range(n - 31):
        X[i + 31] = (X[i + 3] + X[i]) % 2

    return X[n - 1]  # Solve indexing


def C_init(n_PRS_idseq, Nslot_symb, n, l):
    # n: slot number
    # l OFDM symbol within the slot
    # n_PRS_idseq: 0,1,...,4095
    c_init = (
        2**22 * math.floor(n_PRS_idseq / 1024)
        + 2**10 * (Nslot_symb * n + l + 1) * (2 * (n_PRS_idseq % 1024) + 1)
        + (n_PRS_idseq % 1024)
    ) % 2**31

    return c_init


"""
MAIN STARTING HERE
"""


def main():
    vector = r(35)


if __name__ == "__main__":
    main()
