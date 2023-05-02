DEBUG = True

def eh_par(n):
    if (n % 2) == 0:
        return True
    else:
        return False

def coeficientes(alfa, resto_lm, quociente):
    i = len(alfa) - 1
    y = (alfa[i]*resto_lm[0] - quociente[0])//resto_lm[2]
    x = (y * resto_lm[1] - 1)//-(resto_lm[0])
    return x, y

def metade_restos (resto_l, rn):
    resto_lm = [int(linha) // rn for linha in resto_l]
    return resto_lm

def calcula_alfa(posicao, resto_lm, quociente):
    alfa_i = [1]
    z = posicao - 3 # tirar a e b

    # define número de iterações
    i = z // 2 if eh_par(z) else (z - 1) // 2
    
    # define valores de k e l
    k, l = (2, 0) if eh_par(z) else (3, 1)

    linha = 1
    while (linha <= i):
        q = (alfa_i[linha - 1] * resto_lm[(posicao - 1) - k] - quociente[(posicao - 1) - l]) // resto_lm[(posicao - 1)- l]
        alfa_i.append(q)
        k += 2
        l += 2
        linha+=1

    return alfa_i

def verifica (resto_l, a, x, y):
    c = resto_l[0] * x + resto_l[1] * y
    if (c==a):
        return True
    else:
        return False


def mdc_extendido(a, b):
    resto = 1
    resto_l = [a, b]
    quociente = [0, 0]
    
    while (resto != 0):
        resto = a % b
        resto_l.append(resto)
        quociente.append(a//b)
        a, b = b, resto #atualização de valores
 
    resto_lm = metade_restos(resto_l, a)
    posicao = len(resto_lm) - 1
    alfa = calcula_alfa(posicao, resto_lm, quociente)
    x, y = coeficientes(alfa, resto_lm, quociente)

    if (DEBUG):
        print ("\nTabela de restos: ", resto_l)
        print("Valores dos quocientes: ", quociente)
        print("Valor de rn: ", a)
        print("Após a divisão por rn: ", resto_lm)
        print("Valores de alfa_i: ", alfa)
        print(verifica(resto_l, a, x, y), "\n")

    return a, x, y
    
mdc, x, y = mdc_extendido(239, 151)
print ("MDC :", mdc)
print("x: ", x)
print("y: ", y)