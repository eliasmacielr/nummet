import math

def false_position(xl, xu, tol, imax, xr):
    it = 0
    while True:
        xrold = xr
        xr = xu - (f(xu) * (xl - xu))/(f(xl) - f(xu))
        it = it + 1
        fxr = f(xr)
        if xr != 0:
            er = abs(xr - xrold) # abs(fxr) #
        test = f(xl) * fxr
        if test < 0:
            xu = xr
        elif test > 0:
            xl = xr
        else:
            er = 0
        if er < tol or it >= imax:
            break
    return xr, it, er

def f(x):
    return math.exp(-x**2) + math.sin(x)
