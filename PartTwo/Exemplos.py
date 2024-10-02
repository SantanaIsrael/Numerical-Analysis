import Metodos.regressao_Linear as regresao
import Metodos.trapezio as Trapezio
import Metodos.quadratura_de_Gauss as gauss
import Metodos.lagrange as lagrange
import Metodos.newton as newton
import Metodos.derivada as derivadas
import Metodos.simpson as simpson
import Metodos.extra_Richards as richards
import gravar_Arquivo as gravar
import leitura_Arquivo as leitura

#REGRESSÃO LINEAR
x, y = leitura.LerArquivoRerLinear()
a0, a1 = regresao.regressao_linear(x, y)
r = regresao.coeficiente_correlacao(x, y)
gravar.salvar_resultado(a1, a0, r)

#LAGRANGE
fx, pontos = leitura.lerArquivoLagrange()
gravar.salvar_Lagrange(lagrange.lagrange(fx, pontos))

#NEWTON
fx, pontos = leitura.lerArquivoNewton()
gravar.salvar_Newton(newton.newton(fx, pontos))

#GAUSS
fun, a, b = leitura.lerArquivo('Gauss')
gravar.salvar(str(gauss.quadratura_gauss(a, b, fun)), 'Gauss')

#TRAPEZIO SIMPLES
fun, a, b = leitura.lerArquivo('Trapezio')
gravar.salvar(str(Trapezio.trapezio_simples(a, b, fun)), 'Trapezio')

#TRAPEZIO MULTIPLO
fun, a, b, sub = leitura.lerArquivo('TrapezioM')
gravar.salvar(str(Trapezio.trapezio_Multiplo(fun, a, b, sub)), 'Trapezio Multiplo')

#Simpson 1/3
fun, a, b, sub = leitura.lerArquivo('Simpson')
gravar.salvar(str(simpson.Simpson1_3(fun, a, b, sub)), 'Simpson 1/3')

#Simpson 3/8
fun, a, b, sub = leitura.lerArquivo('Simpson')
gravar.salvar(str(simpson.Simpson3_8(fun, a, b, sub)), 'Simpson 3/8')

#Derivadas
fun, x = leitura.lerArquivoDeri()
derivadas.setFuncao(fun)

    #primeira
gravar.salvar(derivadas.derivadaPrimeira(x), 'Derivada primeira')

    #segunda
gravar.salvar(derivadas.derivadaSegunda(x), 'Derivada Segunda')

#Extrapolação de richards
vetor_um, vetor_dois = leitura.lerArquivoRichards()
num_extrapolacao = 6
gravar.salvar_Richards(str(richards.extrapolacao_richards(vetor_um, vetor_dois, num_extrapolacao)),str(num_extrapolacao)) 