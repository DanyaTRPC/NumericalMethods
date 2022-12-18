def f(x,y):
  return 3*(x+y)

h = 0.25
y0 = 1
x0 = 0

k1 = h * f(x0, y0)
k2 = h * f(x0 + 3 * h / 4, y0 + k1 * 3 * h / 4)
y_kutta2 = y0 + (k1 + 2 * k2) / 3

print(y_kutta2)
