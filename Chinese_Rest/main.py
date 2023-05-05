NAOEXISTE = 0

def mdc (a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

def inverso (b, d):
    m = mdc(b, d)
    if (m!=1): return NAOEXISTE

def calcula_inequacao (y, z, a, b, c, d):
    x = ((inverso(b, d)) * b * (c - a) + a)
    alfa = b * d
    if (x > alfa): x = x // alfa
    return x, alfa