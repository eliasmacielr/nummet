import numpy.linalg.norm as norm
import numpy.matmul as matmul
import numpy.dot as dot


def power_iteration(A, x, e): 
    x = x / norm(x)
    a = matmul(A, x)
    l = dot(a, x)
    i = 0
    while norm(a - l * x) > e * abs(l):
        x = a / norm(a)
        a = matmul(A, x)
        l = dot(a, x)
        i = i + 1

    x.insert(0, l)
    x.append(i)

