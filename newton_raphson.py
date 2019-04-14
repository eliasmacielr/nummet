import math

def newton_raphson(x0, tol, imax):
    xr = x0
    it = 0
    while True:
        xrold = xr
        xr = xrold - f(xrold) / f_(xrold)
        it = it + 1
        if xr != 0:
            er = abs(xr - xrold) # abs(f(xr)) #
        if er < tol or it >= imax:
            break
    return xr, it, er

def f(x):
    return x**3 - x - 1

def f_(x):
    return (f(x+1e-6) - f(x)) / 1e-6
