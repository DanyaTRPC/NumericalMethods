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

INTEGRAL_PRECISION = 30

nodes = []
demo_nodes =[]

demo_beta = beta + 3
demo_alpha = alpha - 0.5
demo_n = n * 2

demo_h = (demo_beta-demo_alpha)/demo_n
h = (beta-alpha)/n

for i in range(n):
    nodes.append(alpha+i*h)

for i in range(demo_n):
    demo_nodes.append(demo_alpha+i*h)

def local_integrate(lf):
    local_x = []
    
    local_h = (beta-alpha) / INTEGRAL_PRECISION

    for i in range(INTEGRAL_PRECISION):
        local_x.append(alpha + i * local_h)

    local_y = [lf(x) for x in local_x]

    return numpy.trapz(local_y, local_x)

def build_polynomial(base):
    right_part = []
    left_part = []

    for r in range(base):
        row = []

        for ci in range(base):
            def col_func(x):
                return x ** (r + ci)
            
            row.append(
                local_integrate(col_func)
            )
        
        left_part.append(numpy.array(row))

        def right_part_func(x):
            return f(x) * (x ** r)
        
        right_part.append(
            local_integrate(right_part_func)
        )

    solution = numpy.linalg.solve(
        left_part,
        right_part
    )

    pb = base

    def polynomial(x):
        s = 0

        for i in range(pb):
            s += solution[i] * (x ** i)
        
        return s
    
    return (polynomial, solution.tolist())

m = 3

poly, solution = build_polynomial(m)

func_values = [f(x) for x in demo_nodes]
poly_values = [poly(x) for x in demo_nodes]

err_nodes = []
err_values = []

err_h = (beta-alpha) / N

for j in range(N):
    err_nodes.append(
        alpha + j*h
    )

for j in range(N):
    es = 0

    for i in range(m):
        es += solution[i] * (err_nodes[j] ** i)

    err_values.append(
        f(err_nodes[j]) - es
    )

err = math.sqrt(
    sum(
        [x*x for x in err_values]
    ) / (N+1)
)

print(err)

plt.plot(demo_nodes, func_values, 'ro')
plt.plot(demo_nodes, poly_values)
plt.show()
