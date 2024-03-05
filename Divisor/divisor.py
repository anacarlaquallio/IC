# Código genérico para separar um número em duas partes, dado um índice j
def separar_numero(n, j):
    n_str = str(n)
    b = int(n_str[:-j])
    z = int(n_str[-j:])
    return b, z

# Exemplo de uso
n = 11661
d = 13
m_d = 17
n_d = d * m_d

k = 4
b, z = separar_numero(n, k)

#print(f"Para n = {n} e k = {k}, temos b = {b} e z = {z}")

j = 2

a, u = separar_numero(n_d, j)    
i = k // j

if i % 2 == 0:
    n_l = b * (u**i) + (a**i) * z

else: 
    n_l = b * (u**i) - (a**i)*z

print(n_l)

if (n_l % d == 0):
    print("Deu certo")

else:
    print("Contra exemplo")