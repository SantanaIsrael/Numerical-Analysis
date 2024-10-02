import math
from sympy import *

def shooting(funcao, y_inicial, intervalo, valor, h, pontos):
    x = symbols('x')

    y_final = []

    x_y_z = [[], [], []]

    for j in range(len(x_y_z)):
        x_y_z[0] = [0]
        x_y_z[1] = [y_inicial]
        if j != 2:
            x_y_z[2] = [intervalo[j]]
            for i in range(pontos):        
                x_y_z[1].append(x_y_z[1][i] + h *x_y_z[2][i])
                x_y_z[2].append(x_y_z[2][i] + h * funcao.subs(x, x_y_z[0][i]))
                x_y_z[0].append(x_y_z[0][i] + h)
            y_final.append(x_y_z[1][-1])
        else:
            x_y_z[2] = [intervalo[0] + ( (intervalo[1]-intervalo[0]) / (y_final[1]-y_final[0]) ) * (valor-y_final[0])]
            for i in range(pontos):
                x_y_z[1].append(x_y_z[1][i] + h * x_y_z[2][i])
                x_y_z[2].append(x_y_z[2][i] + h * funcao.subs(x, x_y_z[0][i]))
                x_y_z[0].append(x_y_z[0][i] + h)

        if x_y_z[1][-1] == valor: 
            resultado = []
            for i in range (len(x_y_z[1])):
                resultado.append([i, round(x_y_z[1][i], 3)])

            return resultado