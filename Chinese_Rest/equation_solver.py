import inverso as iv


def solver_equation(a, b, n):
    mdc, x, y = iv.mdc_extendido(a, n)
    if ((b % mdc) == 0):
        x0 = (x*(b//mdc)) % n
        i = 0
        while (i <= mdc - 1):
            print("Possível solução: ", (x0 + i*(n//mdc)) % n)
            i += 1
    else:
        print("Nenhuma solução!")

print("Este algoritmo resolve uma equação da forma: ax ≡ b (mod n)")
a = int(input("Digite um valor para a: "))
b = int(input("Digite um valor para b: "))
n = int(input("Digite um valor para n: "))
solver_equation(a, b, n)
