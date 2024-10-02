from sympy import *

x = symbols('x')

def Polinomios(k, pontos, n):
	
    L = 1
    for i in range(n):
        if i != k:
            L *= Poly((x - pontos[i]) / (pontos[k] - pontos[i]))
    return L

def lagrange(fx, pontos):
	
	P = 0.0
	Poli = 0
 
	for k in range(len(pontos)):
		Poli = Polinomios(k, pontos, len(pontos))
		P = P + fx[k] * Poli

	return str(P.args[0])