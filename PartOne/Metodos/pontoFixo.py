def ponto_fixo(g, x0, erro, max_iter=100):

    x = x0
   
    for i in range(max_iter):
 
        x_prox = g(x)
        
        # Calcula o erro absoluto
        erro_abs = abs(x_prox - x)
        
        if erro_abs < erro:
            return x_prox, i  # Retorna a aproximação encontrada e o número de iterações
        
        # Atualiza a aproximação
        x = x_prox
        
    return x, i