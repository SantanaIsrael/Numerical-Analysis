import Metodos.euler as euler
import Metodos.diferencasFinitas as diferencas
import Metodos.edos as edos
import Metodos.heun as heun
import Metodos.ralston as ralston
import Metodos.rungeKutta_quartaOrdem as runge
import Metodos.shooting as shooting
import math
import leitura_Arquivo as leitura
import gravar_Arquivo as gravar

#Ler o arquivo de euler
equacao,n, x0, y0, h = leitura.lerArquivo_euler()
# faz a função a partir da string que foi lida
f = lambda x, y: eval(equacao)
n = int(n)
# Chamada da função de Euler
x_values, y_values = euler.euler(f, x0, y0, h, n)
#grava euler
gravar.gravaArquivo_euler('euler', x_values, y_values, 'w')

#Chama a função euler modifificado
x_values, y_values = euler.euler_modificado(f, x0, y0, h, n)
#gravar euler modificado
gravar.gravaArquivo_euler('euler modificado', x_values, y_values, 'a')

#Ler o arquivo de Heun
funcao, n, x0, y0, h = leitura.lerArquivo_heun()
#Faz a função a partir da string que foi lida
f = lambda x, y: eval(funcao)
#Chama a função de heun
solucao = heun.heun(f, x0, y0, h, n)
#Grava heun
gravar.gravarArquivo_heun(solucao)

# Chamada da função do método de Ralston
res = ralston.ralston_method(x0, y0, h, n)
#grava os dados que foram gerados
gravar.gravarArquivo_ralston(res)

#leitura do arquivo runge
n, x0, y0, h, f = leitura.lerArquivo_runge()
#Chamada da função runge
x_valor, y_valor = runge.runge_kutta4(f, x0, y0, h, n)
#grava os dados que foram gerados
gravar.gravaArquivo_rungeKutta(x_valor, y_valor)

#Ler o arquivo de EDO's
x, y0, z0, h = leitura.lerArquivo_edos()
#Chama a função de EDO's
Yn, Zn = edos.sistemas_edo(x, y0, z0, h)
#gravar EDO's
gravar.gravarArquivo_EDOS(x, Yn, Zn)

#leitura do arquivo de shooting
funcao, y_inicial, intervalo, valor, h, n = leitura.lerArquivo_shooting()
#Chamada da função de shooting
for i in range(len(funcao)):
    resultado = shooting.shooting(funcao[i], y_inicial[i], intervalo[i], valor[i], h[i], n[i])
#grava os dados que foram gerados
gravar.gravaArquivo_shooting(funcao,resultado)

#Ler o arquivo diferenças finitas
x0, y0, xf, yf, n = leitura.lerArquivo_diferencasFinitas()
#Chama a função diferenças difirenças
y = diferencas.diferenças_finitas(x0, y0, xf, yf, n)
gravar.gravarArquivo_diferencas(y)