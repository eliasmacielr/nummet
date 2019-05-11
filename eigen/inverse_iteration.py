from numpy.linalg import norm
from scipy.linalg import lu

def inverse_iteration(A, x, e, u, f, maxit):
    if f == 0:
        # Perform LU factorization
    elif f == 1:
        # Perform QR factorization
    x = x / norm(x)
    # Solve (A - uI)a = x
    l_ = dot(a, x)
    l = 1/l_ + u
    i = 0
    while norm(a - l_*x) > e * abs(l_):
        x = x / norm(x)
        # Solve (A - uI)a = x
        l_ = dot(a, x)
        l = 1/l_ + u
        i = i + 1

    x = insert(x, 0, l)
    x = append(x, i)
    return x
