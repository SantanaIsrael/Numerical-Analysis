import sympy as sp
import leitura_Arquivo as leitura

#Ler arquuivo de ralston
lines = leitura.lerArquivo_ralston()
func = lines[0]
n = int(lines[1])
x0 = float(lines[2])
y0 = float(lines[3])
h = float(lines[4])

# Função que define a EDO. Substitua 'func' pela sua própria função.
def f(x, y):
    return eval(func)

# Resolve uma EDO de primeira ordem pelo método de Ralston.
def ralston_method(x0, y0, h, n):
    dots = {x0: round(y0, 6)}
    for _ in range(n):
        # Retorna um dicionário com os valores de x e y.
        k1 = f(x0, y0)
        k2 = f(x0 + (3/4)*h, y0 + (3/4)*h*k1)

        y0 += h * ((1/3)*k1 + (2/3)*k2)
        x0 += h
        dots[x0] = round(y0, 6)
    return dots