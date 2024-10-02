import math

def f(x, y, z):
    dy_dz = z
    dz_dx = y + math.e**x

    return dy_dz, dz_dx

def euler(f, x, y, z, h):
    d = f(x, y, z)
    Yn = y + d[0] * h
    Zn = z + d[1] * h

    return Yn, Zn

def sistemas_edo(x, y, z, h):
    Yn = []
    Zn = []
    
    for xi in x:
        yi, zi = euler(f, xi, y, z, h)
        Yn.append(yi)
        Zn.append(zi)

        y = yi
        z = zi

    return Yn, Zn