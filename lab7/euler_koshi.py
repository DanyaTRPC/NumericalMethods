import matplotlib.pyplot as plt
from math import e, log
import numpy as np


def func(x, y):
    return 1 + y / (x * (x + 1))


def dy_dx(x):
    return (x ** 2 + (x * log(x))) / (x + 1)


x0 = 1
y0 = 0.5
xn = 2
n = 10
h = (xn - x0) / (n - 1)

x = np.linspace(x0, xn, n)
y = list(map(lambda x: dy_dx(x), x))

y_e = [0] * n
y_e[0] = y0
for i in range(1, n):
    add = h*func(x[i - 1], y0)
    func_half = func(x[i - 1], y0)+func(x[i - 1]+h, y0+add)
    y_e[i] = h/2 * func_half + y0
    y0 = y_e[i]

diff = np.amax(np.abs(np.subtract(y_e, y)))

print('Точний розв’язок:\t', y)
print('Методом Ейлера:\t', y_e)
print('Похибка:', diff)
plt.plot(x, y)  # Точний розв'язок
plt.plot(x, y_e, 'o')  # По методу ейлера
plt.show()
