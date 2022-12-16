import math
import random
import numpy
import matplotlib.pyplot as plt

alpha = 1
beta = 2
n = 10
m = 10000


# наша фукнція
def f(x):
    return x**2 - x**3

# будуємо вузли
def build_nodes():
    res = []

    for i in range(0, n):
        res.append(
            random.uniform(alpha,beta)
        )

    return res

# пошук похибки
def find_error(interp_fn):
    err = 0
    
    for i in range(0, m):
        r = random.uniform(alpha, beta)

        err = max(err, math.fabs(f(r) - interp_fn(r)))

    return err

# функція знаходження різниці
def find_diff(x_values, y_values, offset):
    res = 0
    
    for j in range(0, offset+1):
        pr = 1

        for i in range(0, offset+1):
            if i == j: continue

            pr *= x_values[j] - x_values[i]

        res += y_values[j] / pr

    return res 

# побудова многолчена Ньютона
def build_newton(x_values, y_values):
    diffs = []

    for i in range(0, len(x_values)):
        diffs.append(
            find_diff(x_values, y_values, i)
        )

    def polynomial(x):
        members = []

        for i in range(0, len(x_values)):
            product = 1

            for j in range(1, i+1):
                product *= x - x_values[j-1]

            members.append(
                product * diffs[i]
            )

        return sum(
            members
        )


    return polynomial

X = build_nodes()
Y = list(map(lambda x: f(x), X))

Nn = build_newton(X, Y)
YN = list(map(lambda x: Nn(x), X))

print("X = ", X)
print("Y = ", Y)
print("N(n) = ", YN)
print("Newton error = ", find_error(Nn))

plot_x = numpy.linspace(alpha,beta,100).tolist()

plot_Y = list(map(lambda x: f(x), plot_x))
plot_N = list(map(lambda x: Nn(x), plot_x))

plt.plot(plot_x, plot_Y, 'r')
plt.plot(plot_x, plot_N, 'g') 
plt.show()