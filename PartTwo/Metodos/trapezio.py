from sympy import *

x = Symbol('x')

def trapezio_simples(a, b, funcao):
    
    I = (b - a)*((funcao.subs(x, a) + funcao.subs(x, b))/2)
    return I

def intervalos(inicio, fim, h):
	xi = [inicio]

	aux = inicio + h
	while(aux < fim):
		aux = round(aux, 2)
		xi.append(aux)
		aux += h
	xi.append(aux)
	return xi

def trapezio_Multiplo(funcao, a, b, n):
	h = (b - a) / n
	xi = intervalos(a, b, h)
	tam = len(xi)
	I = funcao.subs(x, a) + funcao.subs(x, b)

	for i in range(1,tam-1):
		I += 2*(funcao.subs(x, xi[i]))
	I *= h/2
	return round(I, 3)