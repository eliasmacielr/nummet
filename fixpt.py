import math

def fixpt(x0, es, imax):
    xr = x0
    it = 0
    while True:
        xrold = xr
        xr = g(xrold)
        it = it + 1
        if xr != 0:
            ea = abs((xr - xrold) / xr) * 100
        if ea < es or it >= imax:
            break
    return xr, it, ea

def g(x):
    return math.exp(-x)
