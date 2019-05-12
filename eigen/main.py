from time import time
from numpy import append
from numpy import array

from power_iteration import power_iteration
from inverse_iteration import inverse_iteration


def main():
    A = array([[4,-5],
               [2,-3]])
    s = 1
    f = 0
    e = 10e-5
    u = 500
    x = power_method(A, s, f, e, u)
    print(x)


def power_method(A, s, f, e, u):
    x = array([1,0])
    maxit = 1000
    start = None
    end = None
    if s == 0:
        start = time()
        x = power_iteration(A, x, e, maxit)
        end = time()
    if s == 1:
        start = time()
        x = inverse_iteration(A, x, e, u, f, maxit)
        end = time()
    x = append(x, end - start)
    return x


if __name__ == '__main__':
    main()
