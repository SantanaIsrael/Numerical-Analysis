import Metodos.jacobi as jacobi

A = []
b = []
epsilon = 0.05

# Jacobi
with open('Input/entrada6.txt', 'r') as arquivo:
    readMatriz = True
    readList = True

    # Lê o arquivo linha por linha
    for linha in arquivo:
        linha = linha.strip() 

        if linha == "------------":
            if readMatriz:
                readMatriz = False
            elif readList:
                readList = False
            else:
                break  # Saímos do loop quando todas as seções foram lidas
        else:
            elementos = [float(elemento) for elemento in linha.split()]
            if readMatriz:
                A.append(elementos)
            elif readList:
                b.extend(elementos)

x, cont = jacobi.jacobi(A, b, epsilon)

with open('Output/resultadoJacobi.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write(f'================ PROBLEMA 1 ====================\n')
    arquivo.write("Matriz A: \n")
    
    for i in range(len(A)):
        for j in range(len(A)):
            arquivo.write("[" + str(A[i][j]) + "] ")

        arquivo.write("\n")

    arquivo.write("Vetor b: " + str(b) + "\n")
    arquivo.write("Vetor resultante: " + str(x) + "\n")
    arquivo.write(f"Iterações: {cont}")