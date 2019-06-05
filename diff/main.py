import math
import time
import numpy as np
from math import e
from math import exp
from numpy.linalg import norm
from numpy.linalg import solve
from scipy.sparse import diags
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve


def main():
    flag = 0 # 1 for full and 0 for sparse
    tol = 1e-12
    N = 8000000
    while True:
        h = (100-1)/(N+1)

        # Arrays for diagonals, right-hand side and solution
        d_b = [] # below main diagonal
        d_m = [] # main diagonal
        d_a = [] # above main diagonal
        b = []   # right-hand side
        Y = []   # exact solution
        X = []   # numerical solution

        # The diagonal above the main one goes from 1 to N-1,
        # the main diagonal goes from 1 to N,
        # the diagonal below the main one goes from 2 to N.
        tj = h + 1
        d_m.append(-(2*(tj**2)/(h**2) + 1))
        d_a.append((tj**2)/(h**2) + tj/(2*h))
        b.append((tj**2)*exp(-tj))
        Y.append(y(tj))
        for j in range(2, N):
            tj = j*h + 1
            d_b.append((tj**2)/(h**2) - tj/(2*h))
            d_m.append(-(2*(tj**2)/(h**2) + 1))
            d_a.append((tj**2)/(h**2) + tj/(2*h))
            b.append((tj**2)*exp(-tj))
            Y.append(y(tj))
        tj = N*h + 1
        d_b.append((tj**2)/(h**2) - tj/(2*h))
        d_m.append(-(2*(tj**2)/(h**2) + 1))
        b.append((tj**2)*exp(-tj))
        Y.append(y(tj))

        # Sparse matrix, need CSR or CSC to use spsolve.
        S = csr_matrix(diags([d_b,d_m,d_a],[-1,0,1]))
        if flag == 0:
            X = spsolve(S, b)
        elif flag == 1:
            # Full matrix
            F = S.toarray()
            X = solve(F, b)

        if norm(Y - X, np.inf) < tol:
            break
        N += 1000
        print(N)

    print(flag, tol, N)


# Exact solution
def y(x):
    y = (2/9999*e**(-1) - 101/9999*e**(-100))*x + (101/9999*e**(-100) - 20000/9999*e**(-1))*x**(-1) + e**(-x)*(1 + x**(-1))
    return y


if __name__ == "__main__":
    main()
