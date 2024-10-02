import math
import Metodos.pontoFixo as ponto_fixo
import Metodos.secante as secante
import Metodos.newtonRaphson as newton

def f(x):
    return (math.sin(x)/math.tan(40)) - 0.8 - math.cos(x)

def fd(x):
    return (math.cos(x)/math.tan(40)) + math.sin(x)

with open('Input/entrada2.txt', 'r', encoding='utf-8') as arquivo:
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
with open('Output/resultadoPonto3.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write(f'================ PROBLEMA 3.6 ====================\n')
    arquivo.write(f'Intervalo: [{inf}, {sup}]\n')
    arquivo.write(f'A raiz encontrada é: {x}\n')
    arquivo.write(f'Número de iterações necessário: {cont}')

cont, x = secante.secante(f, a, b, erro)

# Salvando o resultado no txt "resultado":
with open('Output/resultadoSecante3.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write(f'================ PROBLEMA 3.6 ====================\n')
    arquivo.write(f'Intervalo: [{inf}, {sup}]\n')
    arquivo.write(f'A raiz encontrada é: {x}\n')
    arquivo.write(f'Número de iterações necessário: {cont}')
    
cont, x = newton.newton_raphson(f, fd, a, erro)

# Salvando o resultado no txt "resultado":
with open('Output/resultadoNewton3.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write(f'================ PROBLEMA 3.6 ====================\n')
    arquivo.write(f'Intervalo: [{inf}, {sup}]\n')
    arquivo.write(f'A raiz encontrada é: {x}\n')
    arquivo.write(f'Número de iterações necessário: {cont}')