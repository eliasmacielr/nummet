from time import time

from numpy import array


def main():
    A = array([[1,0],
               [0,1]])
    s = 0
    f = 0
    e = 10e-5
    u = 500
    x = power_method(A, s, f, e, u)


def power_method(A, s, f, e, u):
    x = array([0,0])
    x_ = None
    maxit = 100
    start = None
    end = None
    if s == 0:
        start = time()
        x_ = power_iteration(A, x, e, maxit)
        end = time()
    if s == 1:
        start = time()
        x_ = inverse_iteration(A, x, e, u, f, maxit)
        end = time()
    x = append(x, end - start)
    return x
