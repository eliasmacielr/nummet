import math

def newton_raphson(x0, es, imax):
    xr = x0
    it = 0
    while True:
        xrold = xr
        xr = xrold - f(xrold) / f_(xrold)
        it = it + 1
        if xr != 0:
            ea = abs((xr - xrold) / xr) * 100
        if ea < es or it >= imax:
            break
    return xr, it, ea

def f(x):
    return math.exp(-x**2) + math.sin(x)

def f_(x):
    return (f(x+1e-6) - f(x)) / 1e-6
