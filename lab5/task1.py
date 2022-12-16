import matplotlib.pyplot as plt
import numpy
import math
import functools

f = lambda x: 2/x + x/2
alpha = 1
beta = 2
n = 10
M = 35
N = 40

nodes = []

h = (beta-alpha)/n

for i in range(n):
    nodes.append(alpha+i*h)

def find_c(iteration):
    s = 0

    for i in range(n):
        s += nodes[i] ** iteration

    return s


def find_d(iteration):
    s = 0

    for i in range(n):
        s += (nodes[i] ** iteration) * f(nodes[i]) 

    return s

def build_polynomial(base):
    left_part = []
    right_part = []

    for r in range(base):
        row = []

        for ci in range(base):
            row.append(find_c(ci+r))

        left_part.append(numpy.array(row)) 
        right_part.append(find_d(r))

    solution = numpy.linalg.solve(left_part, numpy.array(right_part))

    pb = base

    def polynomial(x):
        s = 0

        for i in range(pb):
            s += solution[i] * (x ** i)

        return s

    return polynomial

poly = build_polynomial(3)

func_values = [f(x) for x in nodes]
poly_values = [poly(x) for x in nodes]
errors = list(map(lambda y,p: y - p, func_values, poly_values))

print(errors)

avg_error = math.sqrt(
    functools.reduce(
        lambda acc, item: acc + item,
        [er*er for er in errors]
    ) / (n+1)
)

print(avg_error)

plt.plot(nodes, func_values, 'ro')
plt.plot(nodes, poly_values)
plt.show()
