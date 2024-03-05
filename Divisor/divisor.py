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
m_d = int(input("Digite um valor m(d) para cálculo de múltiplo: "))
k = int(input("Digite o valor para o particionamento de n: "))
j = int(input("Digite o valor para o particionamento de m(d): "))

if (n % d != 0):
        print("\nErro: d não divide. Esse é um requisito")
        sys.exit()

if (j % k != 0):
    print("\nErro: os particionamentos devem ser múltiplos entre si")
    sys.exit()

n_d = d * m_d
b, z = separar_numero(n, k)
a, u = separar_numero(n_d, j)    
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