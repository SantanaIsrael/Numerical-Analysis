from sympy import *

x = symbols('x')

def calculaFdosPontos(fx, pontos):
	n = len(pontos)
	if(n == 1):
		return fx[pontos[0]]
	elif(n == 2):
		return(fx[pontos[0]] - fx[pontos[1]]) / (pontos[0] - pontos[1])
	else:		
		return(calculaFdosPontos(fx, pontos[0 : n-1]) - calculaFdosPontos(fx, pontos[1 : n])) / (pontos[0] - pontos[n-1])

def newton(fx, pontos):
	termos = 1
	n = len(pontos)
	P = 0
	aux = []

	for i in range(n):
		aux.append(pontos[i])
		P += termos * round(calculaFdosPontos(fx, aux), 2)
		termos = termos * Poly(x - pontos[i])

	return str(P.args[0])