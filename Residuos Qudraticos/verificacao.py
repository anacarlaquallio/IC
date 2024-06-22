import math

def verifica_euler(a: int, p: int):
    if ((a**((p-1)/2))%p) == 1:
        return True
    else:
        return False

def raiz_inteira(a):
    sqrt_a = math.sqrt(a)
    return sqrt_a.is_integer()

def alg_fernando (a: int, p: int):
    m = (p-1)/2
    j = (m**2) % p
    x = a
    while(x < j):
        x +=p
    Q = 4*(x-j) + 1
    print(j, x, x-j, Q)
    if raiz_inteira(Q):
        return True
    else:
        return False
    
print ("Este programa tem o intuito de verificar se um número a é resíduo quadrático mod p\n")
a = int(input("Diigte o valor de a: "))
p = int(input("Digite o valor do módulo p: "))

if (a<p):
    print("Pelo método de Euler: ",verifica_euler(a, p))
    print("Pelo método do prof. Fernando: ", alg_fernando(a,p))

else:
    print("Para o algoritmo funcionar, é preciso a<p")