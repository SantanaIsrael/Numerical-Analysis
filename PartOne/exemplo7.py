import Metodos.eliminacao_gauss as elim_gaus
import Metodos.fatoracao_LU as f_LU

A = []
b = []

with open("Input/entrada7.txt") as arquivo:
    lendo_matriz = True

    for linha in arquivo:
        linha = linha.strip()  # Remove espaços em branco e quebras de linha

        # Verifica se a linha é a linha de delimitação
        if linha == "------------":
            lendo_matriz = False  # Agora começaremos a ler a lista
            continue  # Pule a linha de delimitação

        # Converte os elementos em inteiros e adiciona à matriz ou lista
        elementos = [int(elemento) for elemento in linha.split()]
        if lendo_matriz:
            A.append(elementos)
        else:
            b.extend(elementos)

#Gauss
x, cont = elim_gaus.eliminacao_gauss(A, b)

with open('Output/resultadoElimGaus.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write(f'================ PROBLEMA 3 ====================\n')
    arquivo.write("Matriz A: \n")
    
    for i in range(len(A)):
        for j in range(len(A)):
            arquivo.write("[" + str(A[i][j]) + "] ")

        arquivo.write("\n")

    arquivo.write("Vetor b: " + str(b) + "\n")
    arquivo.write("Vetor resultante: " + str(x)+ "\n")
    arquivo.write(f"Número de interações: {cont}")


#LU
(L, U), cont = f_LU.fatoracao_LU(A)

x = f_LU.lux(L, U, b)

with open('Output/resultadoFatoLU.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write(f'================ PROBLEMA 3 ====================\n')
    arquivo.write("Matriz A: \n")
    
    for i in range(len(A)):
        for j in range(len(A)):
            arquivo.write("[" + str(A[i][j]) + "] ")

        arquivo.write("\n")

    arquivo.write("Vetor b: " + str(b) + "\n")
    arquivo.write("Vetor resultante: " + str(x)+ "\n")
    arquivo.write(f"Número de interações: {cont}")