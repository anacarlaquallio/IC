def euclidean_extended(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = euclidean_extended(b, a % b)
        return d, y, x - (a // b) * y

def modulo_inverse(a, m):
    d, x, y = euclidean_extended(a, m)
    if d != 1:
        raise ValueError("O inverso multiplicativo não existe.")
    else:
        return x % m

# Exemplo de uso
a = 3  # Congruência
m = 5  # Módulo

inverse = modulo_inverse(a, m)
print(f"O inverso multiplicativo de {a} (módulo {m}) é: {inverse}")
