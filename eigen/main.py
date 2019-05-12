from time import time
from numpy import append
from numpy import array
from numpy import loadtxt
from numpy import matmul
from numpy import matrix

from power_iteration import power_iteration
from inverse_iteration import inverse_iteration


def main():
    k = 5
    Z = loadtxt('A')
    #B = matmul(Z, matrix.transpose(Z))
    s = 1
    f = 0
    e = 10e-5
    u = 0
    print('k =', k)
    print('s =', s)
    print('f =', f)
    print('e =', e)
    print('u =', u)
    x = power_method(Z, s, f, e, u)
    print(x)


def power_method(A, s, f, e, u):
    x = loadtxt('x',max_rows=(A.shape[0]))
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
