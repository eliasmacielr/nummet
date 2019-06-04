import math
import numpy as np
from math import e
from math import exp
from numpy.linalg import norm
from numpy.linalg import solve
from scipy.sparse import diags
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve


def main():
    N = 50
    h = (100-1)/(N+1)

    # Arrays for diagonals, right-hand side and solution
    d_b = [] # below main diagonal
    d_m = [] # main diagonal
    d_a = [] # above main diagonal
    b = []   # right-hand side
    Y = []   # solution

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
    X = spsolve(S, b)
    print(norm(Y - X))


# Exact solution
def y(x):
    y = (2/9999*e**(-1) - 101/9999*e**(-100))*x + (101/9999*e**(-100) - 20000/9999*e**(-1))*x**(-1) + e**(-x)*(1 + x**(-1))
    return y


if __name__ == "__main__":
    main()
