import math
import Metodos.pontoFixo as ponto_fixo
import Metodos.secante as secante
import Metodos.newtonRaphson as newton

def f(x):
    return 0.1 - (1 + x + (x**2)/2)*math.exp(x)

def fd(x):
    return 1/2*(-4*math.exp(x)*-4*x*math.exp(x)-x**2*math.exp(x))

with open('Input/entrada.txt', 'r', encoding='utf-8') as arquivo:
    a = arquivo.readline().strip() # primeira linha 
    b = arquivo.readline().strip() # segunda linha
    erro = arquivo.readline().strip() # terceira linha


# salvando os intervalos...
inf = a
sup = b

# casting ...
a = float(a)
b = float(b)
erro = float(erro)

x, cont = ponto_fixo.ponto_fixo(f, a, erro)

# Salvando o resultado no txt "resultado":
with open('Output/resultadoPonto1.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write(f'================ PROBLEMA 3.3 ====================\n')
    arquivo.write(f'Intervalo: [{sup}, {inf}]\n')
    arquivo.write(f'A raiz encontrada é: {x}\n')
    arquivo.write(f'Número de iterações necessário: {cont}')

cont, x = secante.secante(f, a, b, erro)

# Salvando o resultado no txt "resultado":
with open('Output/resultadoSecante1.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write(f'================ PROBLEMA 3.3 ====================\n')
    arquivo.write(f'Intervalo: [{sup}, {inf}]\n')
    arquivo.write(f'A raiz encontrada é: {x}\n')
    arquivo.write(f'Número de iterações necessário: {cont}')

cont, x = newton.newton_raphson(f, fd, a, erro)

# Salvando o resultado no txt "resultado":
with open('Output/resultadoNewton1.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write(f'================ PROBLEMA 3.3 ====================\n')
    arquivo.write(f'Intervalo: [{sup}, {inf}]\n')
    arquivo.write(f'A raiz encontrada é: {x}\n')
    arquivo.write(f'Número de iterações necessário: {cont}')