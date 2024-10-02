import math

def runge_kutta4(f, x0, y0, h, n):
    x_values = [x0]
    y_values = [y0]

    for _ in range(n):
        x = x_values[-1]
        y = y_values[-1]

        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)

        y_next = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        x_next = x + h

        x_values.append(x_next)
        y_values.append(y_next)

    return x_values, y_values