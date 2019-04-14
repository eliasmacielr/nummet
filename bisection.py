from math import *

def bisection(xl, xu, es, imax, xr):
    it = 0
    while True:
        xrold = xr
        xr = (xl + xu) / 2
        it = it + 1
        if xr != 0:
            ea = abs((xr - xrold) / xr) * 100
        test = f(xl) * f(xr)
        if test < 0:
            xu = xr
        elif test > 0:
            xl = xr
        else:
            ea = 0
        if ea < es or it >= imax
            break
    return xr, it, ea

def f(x):
    return math.exp(-x**2) + math.sin(x)
