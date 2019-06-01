import math
import numpy as np
from math import exp
from numpy.linalg import norm
from scipy.sparse.linalg import spsolve
from scipy.sparse import csr_matrix
from scipy.sparse import dia_matrix


def main():
    N = 50
    h = (100-1)/(N+1)

    # Arrays for diagonals, right-hand side and solution
    d_b = [] # below main diagonal
    d_m = [] # main diagonal
    d_a = [] # above main diagonal
    b = []   # right-hand side
    Y = []   # solution
    for j in range(1, N+1):
        tj = j*h + 1
        #print(tj, end=' ')
        aux_exp1 = (tj**2)/(h**2)
        aux_exp2 = tj/(2*h)
        d_b.append(aux_exp1 - aux_exp2)
        d_m.append(-(2*aux_exp1 + 1))
        d_a.append(aux_exp1 + aux_exp2)
        b.append((tj**2) * math.exp(-tj))
        Y.append(y(tj))
    #print('')

    # Sparse matrix, need CSR or CSC to use spsolve.
    data = np.array([d_m,d_b,d_a])
    offset = np.array([0,-1,1])
    S = dia_matrix((data, offset), shape=(N,N))
    S = csr_matrix(S)
    #F = S.toarray()
    X = spsolve(S, b)
    #print(np.allclose(S.dot(X), b))
    print(norm(S.dot(X) - b))
    print(norm(S.dot(X) - b, np.inf))
    #print(np.allclose(X, Y))
    print(norm(Y - X))
    #np.savetxt('X', X)
    #np.savetxt('Y', Y)


# Exact solution
def y(x):
    y = ((2*(x**2 - 10000))/exp(1) - (101*(x**2 - 1))/exp(100) + 9999*exp(-x)*(x + 1))/9999*x
    return y


if __name__ == "__main__":
    main()
