import numpy as np

def lerArquivo_euler():    
# Lê a entrada do arquivo de euler
    with open('Entrada/entrada_Euler.txt', 'r', encoding="utf-8") as arquivo:
        equacao = arquivo.readline().strip()
        n = int(arquivo.readline())
        x0 = float(arquivo.readline())
        y0 = float(arquivo.readline())
        h = float(arquivo.readline())
    
    arquivo.close()
    return equacao, n, x0, y0, h        

def lerArquivo_diferencasFinitas():
# Lê a entrada do arquivo de difenraças finitas
    with open('Entrada/entrada_DiferencasFinitas.txt', 'r', encoding = 'utf8') as arquivo:

        valores_str = arquivo.readlines()
        valores = [int(valor.strip()) for valor in valores_str]

        x0 = valores[0]
        y0 = valores[1]
        xf = valores[2]
        yf = valores[3]
        n = valores[4]
    arquivo.close()
    return x0, y0, xf, yf, n

def lerArquivo_edos():
    with open('Entrada/entrada_edos.txt', 'r') as arquivo:
        valores_str = arquivo.readlines()
        valores = [float(valor.strip()) for valor in valores_str]

    x = valores[:3]
    y0 = int(valores[3])
    z0 = int(valores[4])
    h = valores[5]

    return x, y0, z0, h

def lerArquivo_heun():
    with open('Entrada/entrada_heun.txt', 'r') as arquivo:
        funcao = arquivo.readline().strip()
        n = int(arquivo.readline())
        x0 = float(arquivo.readline())
        y0 = float(arquivo.readline())
        h = float(arquivo.readline())
    arquivo.close()
    return funcao, n, x0, y0, h

def lerArquivo_ralston():
    #Lê um arquivo e retorna uma lista com as linhas do arquivo.
    with open('Entrada/entrada_ralston.txt', "r", encoding="utf-8") as arquivo:
        return [line.strip() for line in arquivo]
    
def lerArquivo_runge():
    # Lê a entrada do arquivo
    with open('Entrada/entrada_ruge.txt', 'r') as arquivo:
        equation = arquivo.readline().strip()
        n = int(arquivo.readline())
        x0 = float(arquivo.readline())
        y0 = float(arquivo.readline())
        h = float(arquivo.readline())
    arquivo.close()

    # Define a função a partir da string lida do arquivo
    f = lambda x, y: eval(equation)

    return n, x0, y0, h, f

from sympy import *
import math

def lerArquivo_shooting():
    with open("Entrada/entrada_shooting.txt", "r") as arquivo:
        x = symbols('x')

        funcao = []
        y_inicial = []
        intervalo = []
        valor = []
        h = []
        n = []

        linha = None
        while (linha != ''):
            linha = arquivo.readline()
            if (linha != ""):
                aux = linha.split(";")
                funcao_aux = eval(aux[0])

                y_inicial_aux = eval(aux[1])

                intervalo_aux = aux[2]
                intervalo_aux = intervalo_aux.split(",")
                for i in range (len(intervalo_aux)):
                    intervalo_aux[i] = eval(intervalo_aux[i])

                valor_aux = eval(aux[3])

                h_aux = eval(aux[4])

                n_aux = aux[5]
                n_aux = n_aux.split("\n")
                n_aux = eval(n_aux[0])

                funcao.append(funcao_aux)
                y_inicial.append(y_inicial_aux)
                intervalo.append(intervalo_aux)
                valor.append(valor_aux)
                h.append(h_aux)
                n.append(n_aux)
    
    arquivo.close()

    return funcao, y_inicial, intervalo, valor, h, n