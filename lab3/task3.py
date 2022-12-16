import math
import random
import numpy
import matplotlib.pyplot as plt

import operator as op
from functools import reduce

alpha = 1
beta = 2
n = 10
m = 10000

h = (beta - alpha) / n

# функція
def f(x):
    return x**2 - x**3


def build_nodes():
    return numpy.linspace(
        alpha,
        beta,
        n
    ).tolist()


#
def find_error(interp_fn):
    err = 0
    
    for i in range(0, m):
        r = random.uniform(alpha, beta)

        err = max(err, math.fabs(f(r) - interp_fn(r)))

    return err


# пошук різниці, параметр forward визиначає напрям (вперед або назад)
def find_diff(x_values, y_values, offset, forward = True):
    res = 0
    
    for j in range(0, offset+1):
        pr = 1

        for i in range(0, offset+1):
            if i == j: continue

            pr *= x_values[j] - x_values[i]

        res += y_values[j] / pr

    return res 

# побудова поліному Ньютона за заданими параметрами
def build_newton(x_values, y_values, forward = True):
    diffs = []

    N = len(x_values)

    for i in range(0, N):
        diffs.append(
            [ 0 for i in range(N)]
        )

        diffs[i][0] = y_values[i]

    # будуємо таблицю різниць у вигляді матриці
    if forward:
        for i in range(1, N):
            for j in range(0, N-i):
                diffs[j][i] = diffs[j+1][i-1] - diffs[j][i-1]
    else:
        for i in range(1, N):
            for j in range(N-1, i-1, -1):
                diffs[j][i] = diffs[j][i-1] - diffs[j-1][i-1]

    # Обчислення поліному
    def polynomial(x):
        s = diffs[0][0] if forward else diffs[N-1][0]

        for i in range(1, N):
            product = 1

            products_range = range(0,i) if forward else range(N-1, i-1, -1)

            for j in products_range:
                product *= x - x_values[j]

            s += diffs[0 if forward else n-1 ][i] / ((h ** i) * math.factorial(i)) * product

        return s
   
    return polynomial

X = build_nodes()
Y = list(map(lambda x: f(x), X))

Nf = build_newton(X, Y)
Yf = list(map(lambda x: Nf(x), X))

Nb = build_newton(X, Y, False)
Yb = list(map(lambda x: Nb(x), X))

print("X = ", X)
print("Y = ", Y)
print("Nf(n) = ", Yf)
print("Nb(n) = ", Yb)
print("Newton Forward error = ", find_error(Nf))
print("Newton Backward error = ", find_error(Nb))

plot_x = numpy.linspace(alpha,beta,100).tolist()

plot_Y = list(map(lambda x: f(x), plot_x))
plot_Nf = list(map(lambda x: Nf(x), plot_x))
plot_Nb = list(map(lambda x: Nb(x), plot_x))

plt.plot(plot_x, plot_Y, 'r')
plt.plot(plot_x, plot_Nf, 'g') 
plt.plot(plot_x, plot_Nb, 'b') 
plt.show()  
