import matplotlib.pyplot as plt
from math import sqrt
import numpy as np

x0 = 0
y0 = 1
xn = 4
n = 20
h = 0.25

def f(x, y):
    return 3*(x+y)


def df(x):
    return 3*(x)


def find_err(ex, fc):
    return np.amax(np.abs(np.subtract(ex, fc)))

x = [0, 0.25, 0.5, 0.75]
y = list(map(lambda x: df(x), x))

def euler(y0):
    y_e = [0] * n
    y_e[0] = y0
    for i in range(1, n):
        y_e[i] = h * f(x[i - 1], y0) + y0
        y0 = y_e[i]

    return y_e

def euler_koshi(y0):
    y_e = [0] * n
    y_e[0] = y0
    for i in range(1, n):
        add = h*f(x[i - 1], y0)
        func_half = f(x[i - 1], y0)+f(x[i - 1]+h, y0+add)
        y_e[i] = h/2 * func_half + y0
        y0 = y_e[i]
        print(i, y0)

    return y_e

def kutta2(y0):
    y_kutta2 = [0] * n

    y_kutta2[0] = y0
    for i in range(1, n):
        k1 = h * f(x[i - 1], y0)
        k2 = h * f(x[i - 1] + 3 * h / 4, y0 + k1 * 3 * h / 4)
        y_kutta2[i] = y0 + (k1 + 2 * k2) / 3
        y0 = y_kutta2[i]
        print(y0)

    return y_kutta2


def euler_improved(y0):
    y_e = [0] * n
    y_e[0] = y0
    for i in range(1, n):
        y_half = y0 + h / 2 * f(x[i - 1], y0)
        y_e[i] = y0 + h * f(x[i - 1] + h / 2, y_half)
        y0 = y_e[i]

    return y_e

def kutta3(y0):
    y_kutta3 = [0] * n

    y_kutta3[0] = y0
    for i in range(1, n):
        k1 = h * f(x[i - 1], y0)
        k2 = h * f(x[i - 1] + h / 2, y0 + k1 / 2)
        k3 = h * f(x[i - 1] + h / 2, y0 + k2 / 2)
        y_kutta3[i] = y0 + (k1 + 4 * k2 + k3) / 6
        y0 = y_kutta3[i]

    return y_kutta3

def kutta4(y0):
    y_kutta4 = [0]*n

    y_kutta4[0] = y0
    for i in range(1, n):
        k1 = h * f(x[i - 1], y0)
        k2 = h * f(x[i - 1] + h / 2, y0 + k1 / 2)
        k3 = h * f(x[i - 1] + h / 2, y0 + k2 / 2)
        k4 = h * f(x[i - 1] + h, y0 + k3)
        y_kutta4[i] = y0 + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        y0 = y_kutta4[i]

    return y_kutta4

methods = [
    #("Euler", euler),
    #("Euler Improved", euler_improved),
    #("Euler-Koshi", euler_koshi),
    ("Runge-Kutta 2nd order", kutta2),
    #("Runge-Kutta 3rd order", kutta3),
    #("Runge-Kutta 4rd order", kutta4)
]

print('Exact Solution ', y)
print("-----------")


plt.plot(x, y) 

min_tp = ["n/a", 10000]

print(x)

for method in methods:
    (method_name, method_fn) = method
    result = method_fn(y0)

    print(method_name, result)

    plt.plot(x, result, 'o') 

    diff = find_err(y, result)
    print('err =', diff)

    if diff < min_tp[1]:
        min_tp = [method_name, diff]
    print("---------")

print("BEST METHOD ==>", min_tp)

plt.show()
