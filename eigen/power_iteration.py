from numpy import append
from numpy import dot
from numpy import insert
from numpy import matmul
from numpy.linalg import norm


def power_iteration(A, x, e, maxit):
    x = x / norm(x)
    a = matmul(A, x)
    l = dot(a, x)
    i = 0
    while norm(a - l*x) > e * abs(l) and i < maxit:
        x = a / norm(a)
        a = matmul(A, x)
        l = dot(a, x)
        i = i + 1

    x = insert(x, 0, l)
    x = append(x, i)
    return x
