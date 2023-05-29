import inverso as iv


def solver_equation(a, b, n):
    mdc, x, y = iv.mdc_extendido(a, n)
    print(mdc, x, y)
    if ((b % mdc) == 0):
        x0 = (x*(b//mdc)) % n
        i = 0
        while (i <= mdc - 1):
            print("Possível solução: ", (x0 + i*(n//mdc)) % n)
            i += 1
    else:
        print("Nenhuma solução!")


solver_equation(2, 1, 17)
