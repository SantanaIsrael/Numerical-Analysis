def substituicoes_sucessivas(A, b):
    n = len(A)

    x = n * [0]
    for i in range(0, n):
        s = 0

        for j in range(0, i):
            s = s + A[i][j] * x[j]

        x[i] = (b[i] - s) / A[i][i]

    return x

def identidade(n):

    m = []

    for i in range(0, n):
        linha = [0] * n
        linha[i] = 1
        m.append(linha)

    return m

def fatoracao_LU(A):

    n = len(A)

    # Inicializa a matriz L com a matriz identidade
    L = identidade(n)

    for k in range(0, n - 1):
        
        # Para cada linha i
        for i in range(k + 1, n):
            
            # calcula o fator m
            m = - A[i][k] / A[k][k]
            L[i][k] = -m

            # Atualiza a linha i da matriz, percorrendo todas as colunas j
            for j in range(k + 1, n):
                A[i][j] = m * A[k][j] + A[i][j]

            # Zera o elemento Aik
            A[i][k] = 0

    return (L, A), k

def substituicoes_retorativas(A, b):
    n = len(A)

    x = n * [0]

    for i in range(n - 1, -1, -1):
        s = 0

        for j in range(i + 1, n):
            s = s + A[i][j] * x[j]

        x[i] = (b[i] - s) / A[i][i]

    return x

def lux(L, U, b):

    y = substituicoes_sucessivas(L, b)
    x = substituicoes_retorativas(U, y)

    return x
