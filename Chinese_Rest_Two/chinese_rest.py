import inverso as iv

def novo_x (m, a, b):
    mdc, i, _ = iv.mdc_extendido(m, b)
    if mdc != 1: return -1
    if (i < 0): i = b + i        
    return (a*i) % b

def coprime(num1, num2):
    mdc, _, _ = iv.mdc_extendido(num1, num2)
    if mdc != 1:
        return True
    else:
        return False

def inverso (b: int, d: int):
    mdc, x, _ = iv.mdc_extendido(b, d)

    if (mdc != 1):
        if b % mdc == 0 and d % mdc == 0:
            b = b // mdc
            d = d // mdc

        else:
            return 0, 0, 0, -1
    
    if (x < 0): x = d + x        
    return x, b, d, mdc
        
def calcula_equacao (m:int, n:int, a:int, b:int, c:int, d:int):
    if (m == 0 or n == 0): return 0, 0

    if (m != 1):
        a = novo_x(m, a, b)
        if a == -1: return 0, 0
    
    if (n != 1):
        c = novo_x(n, c, d)
        if c == -1: return 0, 0

    i, b, d, mdc = inverso(b, d)
    if mdc == -1: return 0, 0
    x = ((i * b * (c - a)) + a)
    gama = b * d * mdc
    
    if (x > gama): 
        return x % gama, gama

    while (x < 0):
        x = gama + x
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
if (b < 0 or d < 0): print("O número que acompanha mod precisa ser positivo!")
else: 
    x, gama = calcula_equacao(m, n, a, b, c, d)
    if x == 0 and gama == 0: print("O sistema não possui solução!")
    else: print("Possível solução que satisfaz ambas as equações: x ≡", x, "mod (",gama, ")")