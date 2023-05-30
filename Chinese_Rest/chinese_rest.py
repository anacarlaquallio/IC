import inverso as iv

def inverso (b, d):
    mdc, x, y = iv.mdc_extendido(b, d)
    
    if (mdc != 1):
        b = b // mdc
        d = d // mdc

    if (x < 0): x = d + x        
    return x, b, d, mdc
        
def calcula_equacao (a, b, c, d):
    i, b, d, mdc = inverso(b, d)
    x = (i * b * (c - a) + a)
    gama = b * d * mdc
    if (x > gama): x = x % gama
    return x, gama

print ("Este algoritmo resolve um sistema modular da forma:")
print ("x ≡ a (mod b)")
print ("x ≡ c (mod d)")
a = int(input("Digite um valor para a: "))
b = int(input("Digite um valor para b: "))
c = int(input("Digite um valor para c: "))
d = int(input("Digite um valor para d: "))
x, gama = calcula_equacao(a, b, c, d)
print("Possível solução que satisfaz ambas as equações: x ≡", x, "mod (",gama, ")")