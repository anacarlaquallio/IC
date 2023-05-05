NAOEXISTE = 0
import inverso as eb

def inverso (b, d):
    m, x, y = eb.mdc_extendido(b, d)
    if (m!=1): return NAOEXISTE
    else: return y

def calcula_equacao (a, b, c, d):
    if (inverso(b, d) == NAOEXISTE): return NAOEXISTE, NAOEXISTE
    x = ((inverso(b, d)) * b * (c - a) + a)
    alfa = b * d
    if (x > alfa): x = x % alfa
    return x, alfa

print ("Este algoritmo resolve um sistema modular da forma:")
print ("x ≡ a (mod b)")
print ("x ≡ c (mod d)")
x, alfa = calcula_equacao(2, 3, 7, 10)
print("Possível solução que satisfaz ambas as equações: x ≡", x, "mod (",alfa, ")")