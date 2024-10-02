from sympy import *

x = symbols('x')

def quadratura_gauss(a, b, funcao):
    
    I = ((b - a)/2)*funcao.subs(x, a) + ((b - a)/2)*funcao.subs(x, b)
    return I