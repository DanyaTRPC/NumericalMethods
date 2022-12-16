import math
import matplotlib.pyplot as plt
import time

f = lambda x: math.cos(x) / math.sin(x) - (x / 3) + 2
f1 = lambda x: -1/(math.sin(x)**2) - 1/3

a = 0.3
b = 3
n = 200
epsilon = 0.001

X = []

xi = a

while xi <= b:
    X.append(xi)
    xi += (b - a) / n


def half_method(_a, _b, fn=f):
    it_a = _a
    it_b = _b
    its = 0

    while math.fabs(it_a - it_b) > epsilon:
        x = (it_a + it_b) / 2
        if fn(x) * fn(it_a) < 0:
            it_b = x
        else:
            it_a = x

        its += 1
    
    return it_a, its

def simple_iteration(_a, _b, fn = f, tau = -0.5):
    i = 0
    x_k = 0
    it_a =_a
    while True:
        x_k = it_a + tau * fn(it_a)
        temp = it_a
        it_a = x_k
        i += 1

        if math.fabs(x_k - temp) < epsilon:
            break

    return x_k, i

def hordes(_a, _b, fn = f):
    hf = lambda x: (x*fn(_b)- _b*fn(x))/(fn(_b)-fn(x))

    x0 = _a
    x1 = hf(x0)
    its = 0

    while math.fabs(x0 - x1) > epsilon:
        x0 = x1
        x1 = hf(x0)
        its += 1

    return x1, its

def newton(_a, _b, fn = f, fnd = f1):
    x0 = _a
    x1 = _b

    its = 0

    while math.fabs(x0 - x1) > epsilon:
        x0 = x1
        x1 = x0 - fn(x0)/fnd(x0)
        its += 1

    return x1, its

def combined_method(_a, _b, fn = f, fnd = f1):
    x0 = _a
    x0n = _b

    x1 = (x0*fn(x0n)-x0n*fn(x0))/(fn(x0n)-fn(x0))
    x1n = x0n - fn(x0n)/fnd(x0n)
    its = 0

    while math.fabs(x0 - x1) > epsilon:
        x0 = x1
        x1 = (x0*fn(x0n)-x0n*fn(x0))/(fn(x0n)-fn(x0))

        x0n = x1n
        x1n = x0n - fn(x0n)/fnd(x0n)

        its += 1

    return x1, its

if __name__ == "__main__":
    r = (0.1, 3)

    print(half_method(r[0], r[1]))
    #print(simple_iteration(r[0], r[1], f, -0.35))
    print(hordes(r[0], r[1]))
    print(newton(r[0], r[1]))
    print(combined_method(r[0], r[1]))

    plt.plot(X, [f(x) for x in X])
    plt.plot(X, [0 for x in X])
    plt.show()
