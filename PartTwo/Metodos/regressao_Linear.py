import math

def regressao_linear(x, y):

  xsom, ysom, xy, x2, i = 0, 0, 0, 0, 0
  tamX = len(x)

  for i in range(tamX):
    xsom = xsom + x[i]
    ysom = ysom + y[i]
    xy = xy + x[i] * y[i]
    x2 = x2 + x[i]**2

  a1 = (tamX * xy - (xsom * ysom)) / ((tamX * x2) - xsom**2)
  a0 = (ysom/tamX) - (a1 * (xsom/tamX))
    
  return a0, a1

def coeficiente_correlacao(x, y):

  xsom, ysom, xy, x2, i, y2 = 0, 0, 0, 0, 0, 0
  tamX = len(x)

  for i in range(tamX):
    xsom = xsom + x[i]
    ysom = ysom + y[i]
    xy = xy + x[i] * y[i]
    x2 = x2 + x[i]**2
    y2 = y2 + y[i]**2

  r = (tamX * xy - (xsom * ysom)) / (math.sqrt(((tamX * x2) - xsom**2)) * math.sqrt(((tamX * y2) - ysom**2)))

  return r