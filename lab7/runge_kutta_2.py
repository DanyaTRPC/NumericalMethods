import matplotlib.pyplot as plt
from math import e, log
import numpy as np


def func(x, y):
    return 1 + y / (x * (x + 1) )

def dy_dx(x):
    return (x ** 2 + (x * log(x))) / (x + 1)


x0 = 1
y0 = 0.5
xn = 2
n = 10
h = (xn - x0) / (n - 1)
x = np.linspace(x0, xn, n)
y = list(map(lambda x: dy_dx(x), x))

y_kutta2 = [0] * n
y_kutta2[0] = y0
for i in range(1, n):
    k1 = h * func(x[i - 1], y0)
    k2 = h * func(x[i - 1] + 3 * h / 4, y0 + k1 * 3 * h / 4)
    y_kutta2[i] = y0 + (k1 + 2 * k2) / 3
    y0 = y_kutta2[i]

diff = np.amax(np.abs(np.subtract(y_kutta2, y)))
print('Точний розв’язок:\n', y)
print('Методом Рунге-Кутта 2: \n', y_kutta2)
print('Похибка:', diff)
plt.plot(x, y)  # Точний розв'язок
plt.plot(x, y_kutta2)  # По методу Рунге-Кутта 2 порядку
plt.show()
