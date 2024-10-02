# Método da Secante
def secante(f, x0, x1, erro, max_iter=100):
  cont = 0
  for _ in range(max_iter):
    if abs(f(x1)) < erro:
      resultado = x1
      break

    try:
      x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
    except ZeroDivisionError:
      raise ValueError("Erro: divisão por zero")

    if abs(x2 - x1) < erro:
      resultado = x2
      break

    x0, x1 = x1, x2
    cont += 1

  if cont == max_iter:
    raise RuntimeError("Erro: limite máximo de iterações atingido")

  return cont, resultado
