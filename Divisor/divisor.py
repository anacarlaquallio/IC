import sys

def separar_numero(n, j):
    n_str = str(n)
    if j < len(n_str):
        b = int(n_str[:-j])
        z = int(n_str[-j:])
        return b, z
    else: 
        print("\nErro: Valor inválido para o particionamento")
        sys.exit()

print ("Conjectura d | n se e somente se d | n'")
print("Esse programa consiste em encontrar n'\n")
n = int(input("Digite o valor de n: "))
d = int(input("Digite o valor de d: "))
m_d = int(input("Digite um múltiplo qualquer de d: "))
k = int(input("Digite o valor para o particionamento de n: "))
j = int(input("Digite o valor para o particionamento de m(d): "))

if (n % d != 0):
        print("\nErro: d não divide. Esse é um requisito")
        sys.exit()

if (k % j != 0):
    print("\nErro: os particionamentos devem ser múltiplos entre si")
    sys.exit()

if (m_d % d != 0):
    print("\nErro: não foi inserido um múltiplo de d")
    sys.exit()

b, z = separar_numero(n, k)
a, u = separar_numero(m_d, j)
if (b == 0 or z == 0 or a == 0 or u == 0):
    print("\nErro: As partes b, z, a e u não podem ser nulas")
    sys.exit()
i = k // j

if i % 2 == 0:
    n_l = b * (u**i) + (a**i) * z

else: 
    n_l = b * (u**i) - (a**i)*z

print("\nValor de n' encontrado: ", n_l)

if (n_l % d == 0):
    print("Logo, d | n'")

else:
    print("Encontrou-se um contra exemplo para a conjectura")