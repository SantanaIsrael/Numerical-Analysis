def norma(v, x):
    '''
        Calcula a norma entre dois vetores v e x.
    '''

    n = len(v)
    maxnum = 0
    maxden = 0

    for i in range(0, n):
        num = abs(v[i] - x[i])

        if num > maxnum:
            maxnum = num

        den = abs(v[i])

        if den > maxden:
            maxden = den

    return maxnum / maxden

def jacobi(A, b, epsilon, iterMax = 50):
    '''
        Resolve o sistema linear Ax=b usando o método iterativo Gauss-Jacobi.
        O critério de parada utiliza a norma-infinita.
        Saída é o valor x.
    '''

    n = len(A)
    x = n * [0]
    v = n * [0]

    for i in range(0, n):
        for j in range(0, n):
            if i != j:
                A[i][j] = A[i][j] / A[i][i]

        b[i] = b[i] / A[i][i]
        x[i] = b[i]

    for k in range(1, iterMax+1):
        for i in range(0, n):
            s = 0

            for j in range(0, n):
                if i != j:
                    s = s + A[i][j] * x[j]
                
            v[i] = b[i] - s

        d = norma(v, x)

        if d <= epsilon:
            return v, i
        
        x = v[:]
