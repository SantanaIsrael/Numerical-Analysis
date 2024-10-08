import numpy as np

def p(x):
    return x/3

def q(x):
    return -1

def r(x):
      return 6*x - 1

def diferenças_finitas(x0, y0, xf, yf, N):
    ## Variaveis iniciais
    delta_x = (xf - x0) / N
    vetor_x = np.linspace(x0 + delta_x, xf - delta_x, N - 1)
    dim_sist = N - 1
    A = np.zeros((dim_sist, dim_sist))
    b = np.zeros(dim_sist)

    ## Montagem da matirz A
    for i in range(dim_sist):
        x = vetor_x[i]

        for j in range(dim_sist):
            if i == j:
                A[i][j] = 2 + q(x) * pow(delta_x, 2)
            elif i == (j + 1):
                A[i][j] = -1 - p(x) * delta_x / 2
            elif i == (j - 1):
                A[i][j]: -1 + p(x) * delta_x / 2 # type: ignore
            else:
                A[i][j] = 0

    ## Montagem do vetor b
    for i in range(dim_sist):
        x = vetor_x[i]

        if i == 0:
            b[i] = (1 + p(x) * delta_x / 2) * y0 - r(x) * pow(delta_x, 2)
        elif i == (dim_sist - 1):
            b[i] = (1 - p(x) * delta_x / 2) * yf - r(x) * pow(delta_x, 2)
        else:
            b[i] = -r(x) * pow(delta_x, 2)

    ## Resolução do sistema linear Ay = b
    y = np.linalg.solve(A, b)
    return y