def f(x,y):
  return 3*(x+y)

h = 0.5
y0 = 1
x0 = 0

y_half = y0 + h / 2 * f(x0, y0)
y_e = y0 + h * f(x0 + h / 2, y_half)
y0 = y_e

print(y0)
