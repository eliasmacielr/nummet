import math

def secant(x_1, x0, es, imax):
    xrold = x_1
    xr = x0
    it = 0
    while True:
        xroldold = xrold
        xrold = xr
        xr = xrold - (f(xrold) * (xroldold - xrold)/(f(xroldold) - f(xrold))
        it = it + 1
        if xr != 0:
            ea = abs((xr - xrold) / xr) * 100
        if ea < es or it >= imax:
            break
    return xr, it, ea

def f(x):
    return math.exp(-x**2) + math.sin(x)
