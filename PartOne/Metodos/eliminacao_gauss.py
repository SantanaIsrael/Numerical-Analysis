def substituicoes_retorativas(A, b):
    '''Executa o método das substituições retroativas para resolver o sistema 
       linear triangular superior Ax=b.
       Parâmetros de entrada: A é uma matriz triangular superior e b é o vetor constante. 
    '''

    # n é a ordem da matrzi A
    n = len(A)

    # Inicializa o vetor x com o tamanho de n e elementos iguais a 0
    x = n * [0]

    for i in range(n - 1, -1, -1):
        s = 0

        for j in range(i + 1, n):
            s = s + A[i][j] * x[j]

        x[i] = (b[i] - s) / A[i][i]

    return x

def eliminacao_gauss(A, b):
    '''
    Executa o método da eliminação de Gauss para resolver o sistema  linear Ax=b 
    transformando o sistema em um sistema triangular superior equivalente.
    Parâmetros de entrada: A é uma matriz quadrada de ordem n e b é o vetor constante.
    Saída: vetor x
    '''

    # n é a ordem da matriz
    n = len(A)

    # Para cada etapa k
    for k in range(0, n-1):
        # Para cada linha i
        for i in range(k+1, n):
            # Calcula o fator m
            m = - A[i][k]/A[k][k]

            # Atualiza a linha i da matriz, percorrendo todas as colunas j
            for j in range(k+1, n):
                A[i][j] = m * A[k][j] + A[i][j]

            # Atualiza o vetor b na linha i
            b[i] = m * b[k] + b[i]

            # Zera o elemento Aik
            A[i][k] = 0

    # Agora resolve o sistema triangular superior usando as substituições retroativas
    x = substituicoes_retorativas(A, b)
    
    return x, k
