import numpy as np
import numpy.linalg as la


def power_iteration(A, x, e): 
    x = x / la.norm(x)
    a = np.matmul(A, x)
    l = np.dot(a, x)
    i = 0
    while la.norm(a - l * x) > e * abs(l):
        x = a / np.norm(a)
        a = np.matmul(A, x)
        l = np.dot(a, x)
        i = i + 1

    x.insert(0, l)
    x.append(i)
