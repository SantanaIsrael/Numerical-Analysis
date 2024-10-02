# import numpy as np

# Método newton-raphson
def newton_raphson(f, df, x0, erro):
    Er = 1
    x = x0
    cont = 0
    while(Er >= erro):
      xold = x
      x = xold - (f(xold) / df(xold))
      Er = abs((x - xold) / x)
      cont+1
    
    return cont, x
