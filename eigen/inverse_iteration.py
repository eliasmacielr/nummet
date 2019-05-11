from numpy import matrix
from numpy.linalg import norm
from scipy.linalg import lu
from scipy.linalg import qr
from scipy.linalg import solve_triangular


def inverse_iteration(A, x, e, u, f, maxit):
    # Change A for A - uI
    G = None # L or Q from the factorization
    R = None # U or R from the factorization
    P = None # Permutation matrix from A = P L U
    c = None # Result from triangular solve using U or R
    if f == 0:
        P, G, R = lu(A) # P L U = A
    elif f == 1:
        G, R = qr(A) # Q R = A
    x = x / norm(x)

    # Solve (A - uI)a = x
    if f == 0: # L x_ = P^T b
        x_ = matmul(matrix.transpose(P), x)
        c = solve_triangular(G, x_, True, True, True, False)
    elif f == 1: # Q^T b
        c = matmul(matrix.transpose(G), x)
    a = solve_triangular(R, c) # U x = c or R x = c
    l_ = dot(a, x)
    l = 1/l_ + u
    i = 0
    while norm(a - l_*x) > e * abs(l_):
        x = x / norm(x)
        # Solve (A - uI)a = x
        if f == 0: # L x_ = P^T b
            x_ = matmul(matrix.transpose(P), x)
            c = solve_triangular(G, x_, True, True, True, False)
        elif f == 1: # Q^T b
            c = matmul(matrix.transpose(G), x)
        a = solve_triangular(R, c) # U x = c or R x = c
        l_ = dot(a, x)
        l = 1/l_ + u
        i = i + 1

    x = insert(x, 0, l)
    x = append(x, i)
    return x
