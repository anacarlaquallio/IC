import inverso as iv

def inverso (b, d):
    mdc, x, y = iv.mdc_extendido(b, d)
    
    if (mdc!=1):
        b = b // mdc
        d = d // mdc

    if (x < 0):
        x = d + x        
    return x, b, d, mdc
        
def calcula_equacao (a, b, c, d):
    i, b, d, mdc = inverso(b, d)
    print (i, b, d)
    x = (i * b * (c - a) + a)
    gama = b * d * mdc
    if (x > gama): x = x % gama
    return x, gama

print ("Este algoritmo resolve um sistema modular da forma:")
print ("x ≡ a (mod b)")
print ("x ≡ c (mod d)")
#x, alfa = calcula_equacao(5, 6, 19, 20)
x, alfa = calcula_equacao(2, 3, 7, 10)
print (x, alfa)
#print("Possível solução que satisfaz ambas as equações: x ≡", x, "mod (",alfa, ")")