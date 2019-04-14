from math import *

def f(x):
    return x**3 - 3*x + 1

def rtd(n, sd=5):
    if n == 0: return 0
    factor = 10 ** (sd - ceil(log10(fabs(n))))
    return round(n * factor) / factor

def sd(n, s=5):
    a = '%E' % n
    return a.split('E')[0].rstrip('0').rstrip('.') + 'E' + a.split('E')[1] 

def sign(n):
    if n < 0:
        return -1
    return 1

def bisection(f, a, b, n_max):
    fa = f(a)
    fb = f(b)

    if sign(fa) == sign(fb):
        print('function has the same signs at a and b')
        return

    xr = max((a + b) / 2, 1)

    for n in range(1, n_max + 1):
        x = (a + b) / 2
        fx = f(x)

        if abs(fx) < abs(f(xr)):
            xr = x

        print('{:2}| a = {:11} b = {:11} x = {:11} f(x) = {:11}'.format(\
            n, sd(rtd(a)), sd(rtd(b)), sd(rtd(x)), sd(rtd(fx))))

        if fx == 0:
            print('the (aprox.) root of the equation is {:11}\n'.format(sd(rtd(x))))
            return
        elif sign(fx) != sign(fa):
            b = x
        else:
            a = x

    print('the (aprox.) root of the equation is {}'.format(sd(rtd(xr))))


def main():
    a = float(input(r'a = '))
    b = float(input(r'b = '))
    n_max = int(input(r'n = '))

    bisection(f, a, b, n_max)


if __name__ == "__main__":
    main()
