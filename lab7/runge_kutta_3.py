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

y_kutta3 = [0] * n
y_kutta3[0] = y0
for i in range(1, n):
    k1 = h * func(x[i - 1], y0)
    k2 = h * func(x[i - 1] + h / 2, y0 + k1 / 2)
    k3 = h * func(x[i - 1] + h / 2, y0 + k2 / 2)
    y_kutta3[i] = y0 + (k1 + 4 * k2 + k3) / 6
    y0 = y_kutta3[i]

diff = np.amax(np.abs(np.subtract(y_kutta3, y)))

print('Точний розв’язок:\n', y)
print('Методом Рунге-Кутта 3: \n', y_kutta3)
print('Похибка:', diff)
plt.plot(x, y)  # Точний роз'язок
plt.plot(x, y_kutta3)  # По методу Рунге-Кутта 3 порядку
plt.show()
