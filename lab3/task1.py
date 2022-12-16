import math
import random
import matplotlib.pyplot as plt
import numpy

alpha = 1
beta = 5
n = 20
m = 10000


# Наша функція
def f(x):
    return x**2 - x**3

# Створення вузлів згідно формули Чебишева
def build_nodes():
    res = []

    for i in range(0,n):
        res.append(
            ((beta + alpha) / 2) + ((beta - alpha) / 2) * math.cos(
                ((2*i+1)/(2*(n+1))*math.pi)
            )
        )

    return res

# Будуємо функцію яка по задами x,y зможе обчисилити поліном Лагранжа
def build_lagrange(x_values, y_values):
    parts = []
    
    for i in range(0, len(x_values)):
        def part_fn(x, _i = i):
            product = 1

            for k in range(0,len(x_values)):
                if _i == k: continue

                product *= (x - x_values[k]) / (x_values[_i] - x_values[k])

            return product
        
        parts.append(part_fn)

    # Вбудована функція яка динамічно створюється
    def polynomial(x):
        return sum(
            [
                y_values[i] * parts[i](x) for i in range(0, len(x_values))
            ]
        )

    return polynomial

# Обчислення похибки
def find_error(interp_fn):
    h = (beta - alpha) / n*2

    s = alpha

    err = 0

    while s < beta:
        err = max(err, math.fabs(f(s) - interp_fn(s)))

        s += h

    return err


X = build_nodes()
Y = list(map(lambda x: f(x), X))

L = build_lagrange(X, Y)
YL = list(map(lambda x: L(x), X))

print("X = ", X)
print("Y = ", Y)
print("L(X) =", YL)
print("Lagrange error = ", find_error(L))

plot_x = numpy.linspace(alpha,beta,10).tolist()

plot_Y = list(map(f, plot_x))
plot_L = list(map(L, plot_x))

plt.plot(plot_x, plot_Y, 'r')
plt.plot(plot_x, plot_L, 'g') 
plt.show()