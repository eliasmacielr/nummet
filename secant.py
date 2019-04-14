import math

def secant(x_1, x0, tol, imax):
    xrold = x_1
    xr = x0
    it = 0
    while True:
        xroldold = xrold
        xrold = xr
        xr = xrold - (f(xrold) * (xroldold - xrold))/(f(xroldold) - f(xrold))
        it = it + 1
        if xr != 0:
            er = abs(xr - xrold) # abs(f(xr)) #
        if er < tol or it >= imax:
            break
    return xr, it, er

def f(x):
    return (x - 1)**2
