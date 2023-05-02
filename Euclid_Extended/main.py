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

def calcula_alfa(posicao, resto_lm, quociente):
    alfa_i = []
    q = 0
    z = posicao - 2
    linha = 1
    alfa_i.append(1) # alfa 0 = 1

    if (eh_par(z)):
        i = z // 2
        k = 2
        l = 0 
        while (linha <= i):
            q = (alfa_i[linha-1] * resto_lm[posicao-k] - quociente[z - l])//(resto_lm[posicao-l])
            alfa_i.append(q)
            k+=2
            l+=2
            linha +=1
    else:
        i = (z-1)// 2
        k = 3
        l = 1
        while (linha <= i):
            q = (alfa_i[linha-1] * resto_lm[posicao-k] - quociente[posicao-l])//resto_lm[posicao-l]
            alfa_i.append(q)
            k+=2
            l+=2
            linha +=1
    return alfa_i

def mdc_extendido(a, b):
    resto = 1
    resto_l = []
    quociente = []
    alfa  = []
    resto_l.append(a)
    resto_l.append(b)
    
    while (resto != 0):
        resto = a % b
        resto_l.append(resto)
        quociente.append(a//b)
        a = b # assume rn na última iteração
        b = resto
 
    print ("Tabela de restos: ", resto_l)
    print("Valores dos quocientes: ", quociente)
    print("Valor de rn: ", a)

    resto_lm = metade_restos(resto_l, a)
    print("Após a divisão por rn: ", resto_lm)

    posicao = len(resto_lm) - 2
    alfa = []
    alfa = calcula_alfa(posicao, resto_lm, quociente)
    print("Valores de alfa_i: ", alfa)
    
    x, y = coeficientes(alfa, resto_lm, quociente)

    return a, x, y

def metade_restos (resto_l, rn):
    resto_lm = [int(linha) // rn for linha in resto_l]
    return resto_lm
    
mdc, x, y = mdc_extendido(372, 162)
print ("MDC :", mdc)
print("x: ", x)
print("y: ", y)