import matplotlib.pyplot as plt
from sympy.abc import z
import sympy
import numpy as np

from task1 import half_method, simple_iteration, hordes, newton,combined_method

pol = [3, 4, -12, 0, 1]
pol_ = [12, 12, -24, 0]

a = -3
b = 2
n = 80

X = []

xi = a

while xi <= b:
    X.append(xi)
    xi += (b - a) / n


def mathsign(x): return -1 if x < 0 else (1 if x > 0 else 0)

def normalize(poly):
    while poly and poly[-1] == 0:
        poly.pop()
    if poly == []:
        poly.append(0)

def poly_divmod(num, den):
    #Create normalized copies of the args
    num = num[:]
    normalize(num)
    den = den[:]
    normalize(den)

    if len(num) >= len(den):
        #Shift den towards right so it's the same degree as num
        shiftlen = len(num) - len(den)
        den = [0] * shiftlen + den
    else:
        return [0], num

    quot = []
    divisor = float(den[-1])
    for i in range(shiftlen + 1):
        #Get the next coefficient of the quotient.
        mult = num[-1] / divisor
        quot = [mult] + quot

        #Subtract mult * den from num, but don't bother if mult == 0
        #Note that when i==0, mult!=0; so quot is automatically normalized.
        if mult != 0:
            d = [mult * u for u in den]
            num = [u - v for u, v in zip(num, d)]

        num.pop()
        den.pop(0)

    normalize(num)
    return quot, num

def make_polynomial(coeffs):
    return lambda x: np.polyval(coeffs, x)

def W(ff, x):
    last_sign = None
    sol = 0

    for f in ff:
        val = f(x)

        if not last_sign is None:
            if last_sign != mathsign(val):
                sol += 1
            
        last_sign = mathsign(val)

    return sol
        

def sturm():
    symr = sympy.sturm('3*z^4 + 4*z^3 - 12*z^2 + 1', z)
    ffs = [sympy.lambdify(z, s) for s in symr]

    return ffs

def sgn_chg(a,b):
    return 1 if a*b < 0 else 0

def num_of_roots(p):
    changes = 0
    bound = 100
    for idx in range(len(p)-1):
        changes += sgn_chg( p[idx](-bound),p[idx+1](-bound) )

    for idx in range(len(p)-1):
        changes -= sgn_chg( p[idx](bound),p[idx+1](bound) )
    return changes

def intervals(p):
    max_roots = num_of_roots(p)
    num = max_roots
    interval = []
    upperbound = 1000
    for x in range(num-1):
        changes = max_roots - x

        if(x == 0):
            lowerbound = -100
        else:
            lowerbound = interval[x-1]

        while(changes == max_roots-x):
            changes = 0
            lowerbound += .5
            for y in range(len(p)-1):
                changes += sgn_chg(p[y](lowerbound),
                                      p[y+1](lowerbound))
            for y in range(len(p)-1):
                changes -= sgn_chg(p[y](upperbound),
                                     p[y+1](upperbound))
        interval.append(lowerbound-.5)

    max_roots = 0
    for y in range(len(p)-1):
        max_roots += sgn_chg(p[y](upperbound),
                              p[y+1](upperbound))
    changes = max_roots
    while(changes == max_roots):
        changes = 0
        upperbound -= 1
        for y in range(len(p)-1):
            changes += sgn_chg(p[y](upperbound),
                                  p[y+1](upperbound))
    interval.append(upperbound)
    interval.append(upperbound+1)
    return(interval)

sturms = sturm()

print(num_of_roots(sturms))
print(intervals(sturms))

r = intervals(sturms)[:-2]

polf = lambda x: 3*x**4 + 4*x**3 - 12*x**2 + 1
polfd = lambda x: 12*x**3 + 12*x**2 - 24*x

print(np.roots(pol))

print(half_method(r[0], r[1], polf))
print(hordes(r[0], r[1], polf))
print(newton(r[0], r[1], polf, polfd))
print(combined_method(r[0], r[1], polf, polfd))
print(simple_iteration(r[0], r[1], polf, 0.02))

plt.plot(X, [polf(x) for x in X])
plt.plot(X, [0 for x in X])
plt.show()