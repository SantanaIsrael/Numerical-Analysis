import math

def heun(f, x0, y0, h, interacao):
   
    x = x0
    y = y0
    solucao = [(x, y)]

    for _ in range(interacao):
        y_euler = y + h * f(x, y)
        y = y + (h / 2) * (f(x, y) + f(x + h, y_euler))
        x += h
        solucao.append((x, y))

    return solucao

#x[{i}] = {x:.2f},  y[{i}] = {y:.4f}