def euclidean_extended(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = euclidean_extended(b, a % b)
        return d, y, x - (a // b) * y

def extended_gcd_iterative(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1

    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def modulo_inverse(a, m):
    d, x, y = euclidean_extended(a, m)
    if d != 1:
        raise ValueError("O inverso multiplicativo não existe.")
    else:
        return x % m

a = int(input("Diigte o valor de a: "))
b = int(input("Digite o valor de b: "))

print(extended_gcd_iterative(a,b))
