# import stuff
import numpy as np


def r(m):
    return 1 / sqrt(2) * (1 - 2 * c(2 * m)) + 1j * 1 / sqrt(2) * (1 - 2 * c(2 * m))


def c(n, C_init):
    Nc = 1600
    # n = 0,1,2...,M_pn-1
    n = 5  # arbitrary
    ret_value = X1(n + Nc) + X2(n + Nc)
    ret_value = ret_value % 2
    return ret_value


def X1(n):
    # initialise
    X = np.zeros(n + 31)
    X[0] = 1

    # cyclic shifting
    for i in range(n - 31):
        print(f"cyclic shift: {i} {i + 31} / {n}")
        X[i + 31] = (X[i + 3] + X[i]) % 2

    return X


def X2():
    C_init = 0
    for i in range(30):

        return X

"""
MAIN STARTING HERE
"""

# Global variable?
C_init = 5151
