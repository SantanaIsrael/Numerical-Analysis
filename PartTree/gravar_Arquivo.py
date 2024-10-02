import datetime as dt

hoje = dt.date.today()
hora = dt.time()
def gravaArquivo_euler(nome, x_values, y_values, simb):
    
    # Abrir o arquivo de saída
    with open('resultados.txt', simb, encoding="utf-8") as arquivo:
        arquivo.write(f'dia: {hoje.day}/{hoje.month}\nhora: {hora.hour}:{hora.minute}\n')
        arquivo.write('\nResultados ' + nome + '\n')
        i = 0
        for x, y in zip(x_values, y_values):
            arquivo.write(f"x[{i}] = {x:.1f},  y = {y:.6f}\n")
            i = i + 1

    arquivo.close()

def gravarArquivo_EDOS(x, Yn, Zn):
    with open('resultados.txt', 'a') as arquivo:
        arquivo.write('\nResultados EDOs\n')
        arquivo.write(f"x       y           z       h=0.1\n\n")

        for x, y, z in zip(x, Yn, Zn):
            arquivo.write(f"{x:.1f}     {y:.4f}      {z:.4f}\n")
    arquivo.close()

def gravarArquivo_heun(solucao):
    with open('resultados.txt', 'a') as arquivo:
        arquivo.write('\nResultados Heun\n')
        i = 0
        for x, y in solucao:
            arquivo.write(f"x[{i}] = {x:.2f},  y[{i}] = {y:.6f}\n")
            i = i+1

def gravarArquivo_ralston(res):
    with open('resultados.txt', 'a', encoding="utf-8") as arquivo:
        arquivo.write('\nResultados Ralson\n')
        i = 0
        for x, y in res.items():
            arquivo.write(f"x[{i}] = {x:.1f},  y = {y:.6f}\n")
            i = i + 1
            #

def gravaArquivo_rungeKutta(x_values, y_values):
    with open('resultados.txt', 'a') as arquivo:
        # Imprime os resultados
        i = 0
        arquivo.write('\nResultados Runge Kutta\n')
        for x, y in zip(x_values, y_values):
            arquivo.write(f"x[{i}] = {x:.2f},  y =  {y:.6f}\n")
            # x[{i}] = {x:.2f},  y = 
            i = i + 1


def gravaArquivo_shooting(funcao, resultado):
    cont = 0
    with open("resultados.txt", "a") as arquivo:
        arquivo.write('\nResultado Shooting\n')
        for i in range(len(funcao)):
            #resultado = shooting(funcao[i], y_inicial[i], intervalo[i], valor[i], h[i], n[i])
            for item in resultado:
                arquivo.write(f"I[{cont}] = {item[0]}, y[{cont}] = {item[1]}\n")
                cont = cont + 1
            if i < len(funcao) - 1:
                arquivo.write("\n")
    arquivo.close()

import numpy as np
vetor_x = np.linspace(0 + 1/4, 1 - 1/4, 3)
def gravarArquivo_diferencas(y):
        with open("resultados.txt", "a") as arquivo:
            arquivo.write('\nResultado Diferencas Finitas\n')
            arquivo.write(f"Resolucao do sistema linear resultante:\n\n")

            for i in range(len(y)):
                arquivo.write(f"y({vetor_x[i]}) = {y[i]}\n")
        arquivo.close()