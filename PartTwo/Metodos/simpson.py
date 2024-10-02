from sympy import *
from math import *

x = symbols('x')

def intervalos(inicio, fim, h):
	
	xi = [inicio]
	aux = inicio + h
 
	while(True):
		if aux >= fim:
			break
		aux = round(aux, 2)
		xi.append(aux)
		aux += h
	xi.append(aux)
	
	return xi

def Simpson1_3(funcao, a, b, n):
	
	h = (b - a) / (2*n)
	xi = intervalos(a, b, h)
	I = funcao.subs(x, a) + funcao.subs(x, b)

	for i in range(1,len(xi)-1):
		aux = funcao.subs(x, xi[i])
		if(i % 2 == 0):
			I += 2*aux
		elif i % 2 != 0:
			I += 4*aux
	I *= h/3
	
	return round(I, 4)

def Simpson3_8(funcao, a, b, n):

	h = (b - a) / (2*n)
	xi = intervalos(a, b, h)
	I = funcao.subs(x, a) + funcao.subs(x, b)
	count = 0

	for i in range(1,len(xi)-1):
		aux = funcao.subs(x, xi[i])
		if(count >= 2):
			I += 2*aux
			count = 0
		elif count < 2:
			I += 3*aux
			count += 1
			
	I *= (3*h)/8
	
	return round(I, 4)