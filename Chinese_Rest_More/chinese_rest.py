import inverso as iv

def novo_x (m, a, b):
    i, _, _, _ = inverso (m, b)
    return (a*i) % b

def inverso (b: int, d: int):
    mdc, x, y = iv.mdc_extendido(b, d)
    
    if (mdc != 1):
        b = b // mdc
        d = d // mdc

    if (x < 0): x = d + x        
    return x, b, d, mdc
        
def calcula_equacao (m:int, n:int, a:int, b:int, c:int, d:int):
    if (m != 1):
        a = novo_x(m, a, b)
    
    if (n != 1):
        c = novo_x(n, c, d)

    i, b, d, mdc = inverso(b, d)
    x = (i * b * (c - a) + a)
    gama = b * d * mdc
    if (x > gama): x = x % gama
    return x, gama

print ("Este algoritmo resolve um sistema modular da forma:")
print ("m*x ≡ a (mod b)")
print ("n*x ≡ c (mod d)")
m = int(input("Digite um valor para m: "))
a = int(input("Digite um valor para a: "))
b = int(input("Digite um valor para b: "))
n = int(input("Digite um valor para n: "))
c = int(input("Digite um valor para c: "))
d = int(input("Digite um valor para d: "))
x, gama = calcula_equacao(m, n, a, b, c, d)
print("Possível solução que satisfaz ambas as equações: x ≡", x, "mod (",gama, ")")