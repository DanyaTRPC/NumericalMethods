import math
import numpy

a = 3
b = 9

epsilon = 10 ** (-4)


def f(x):
    return 1/(1+x**2)

def F(x):
    return math.atan(x)

exact_solution = F(b) - F(a)

def middle_rectangles_method(x, h):
    return f(x + h/2) * h

def trapezoids_method(x, h):
    return (f(x) + f(x + h))/2 * h

def simpson_method(x,h):
    return (f(x) + 4 * f(x + h/2) + f(x + h)) * (h/6)

def double_calc(k, approximator):
    n = 10

    h = (b-a) / n

    last_sum = 0
    s = 0

    depth = 0 

    while True:
        xptr = a
        s = 0

        # Quadratur Formula Sum
        while xptr < b:
            s += approximator(xptr, h)

            xptr += h

        # Runge Condition
        exit_sum = math.fabs(
            s - last_sum
        ) / (2 ** k  - 1)

        if exit_sum < epsilon:
            break

        h = h / 2
        last_sum = s
        depth += 1

    return (s, depth)

    
middle_rectangles_result = double_calc(
    2, middle_rectangles_method
)

trapezoids_result = double_calc(
    2, trapezoids_method
)

simpsons_result =  double_calc(
    4, simpson_method
)

print("розвязок = ", exact_solution)
print("метод середніх прямокутників = ", middle_rectangles_result,
      ", похибка = ", math.fabs(exact_solution - middle_rectangles_result[0]))
print("метод трапецій = ", trapezoids_result, ", похибка = ", math.fabs(exact_solution - trapezoids_result[0]))
print("Сімпсона = ", simpsons_result, ", похибка = ",
      math.fabs(exact_solution - simpsons_result[0]))
