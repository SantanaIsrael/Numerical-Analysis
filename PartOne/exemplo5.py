import Metodos.pontoFixo as ponto_fixo
import Metodos.secante as secante
import Metodos.newtonRaphson as newton

def f(x):
    return (6.5116*(x**13)) - (7.5116*(x**12)) + 1

def df(x):
    return 84.6508 * (x**12) - 90.1392 * (x**11)

with open('Input/entrada4.txt', 'r', encoding='utf-8') as arquivo:
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
with open('Output/resultadoPonto5.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write(f'================ PROBLEMA 3.8 - Plano B ====================\n')
    arquivo.write(f'Intervalo: [{inf}, {sup}]\n')
    arquivo.write(f'A raiz encontrada é: {x}\n')
    arquivo.write(f'Número de iterações necessário: {cont}')

cont, x = secante.secante(f, a, b, erro)

# Salvando o resultado no txt "resultado":
with open('Output/resultadoSecante5.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write(f'================ PROBLEMA 3.8 - Plano B ====================\n')
    arquivo.write(f'Intervalo: [{inf}, {sup}]\n')
    arquivo.write(f'A raiz encontrada é: {x}\n')
    arquivo.write(f'Número de iterações necessário: {cont}')
    
cont, x = newton.newton_raphson(f, df, a, erro)

# Salvando o resultado no txt "resultado":
with open('Output/resultadoNewton5.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write(f'================ PROBLEMA 3.8 - Plano B ====================\n')
    arquivo.write(f'Intervalo: [{inf}, {sup}]\n')
    arquivo.write(f'A raiz encontrada é: {x}\n')
    arquivo.write(f'Número de iterações necessário: {cont}')