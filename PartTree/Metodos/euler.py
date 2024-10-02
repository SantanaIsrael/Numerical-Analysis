def euler(f, x0, y0, h, n):
    x_values = [x0]
    y_values = [y0]
    
    for _ in range(n):
        x = x_values[-1]
        y = y_values[-1]
        
        y_new = y + h * f(x, y)
        x_new = x + h
        
        x_values.append(x_new)
        y_values.append(y_new)
    
    return x_values, y_values

def euler_modificado(f, x0, y0, h, n):
    x_values = [x0]
    y_values = [y0]
    
    for i in range(1, n + 1):
        x = x_values[i - 1]
        y = y_values[i - 1]
        
        k1 = h * f(x, y)
        k2 = h * f(x + h, y + k1)
        
        y_next = y + 0.5 * (k1 + k2)
        x_next = x + h
        
        x_values.append(x_next)
        y_values.append(y_next)
    
    return x_values, y_values

#x[{i}] = {x:.1f},  y = {y:.6f}