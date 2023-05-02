def eh_par(n):
    if (n % 2) == 0:
        return True
    else:
        return False

def mdc(a, b):
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
 
    print ("Tabela: ", resto_l)
    print("Valores dos quocientes: ", quociente)
    print("Valor de rn: ", a)

    resto_lm = metade_restos(resto_l, a)
    print("Após a divisão por rn: ", resto_lm)

    alfa = []
    q = []
    posicao = len(resto_lm) - 2
    z = posicao - 2 #-2 porque desconsidera-se os dois primeiros valores, que são de a e b
    
    if (eh_par(z)):
        i = z// 2
        alfa.append(1) # alfa 0 = 1
        linha = 1
        k = 2
        l = 0 
        while (linha <= i):
            q = (alfa[linha-1] * resto_lm[posicao-k] - quociente[z - l])//(resto_lm[posicao-l])
            alfa.append(q)
            k+=2
            l+=2
            linha +=1
        print(alfa)
    else:
        i = (z-1)// 2
        alfa.append(1)
        linha = 1
        k = 3
        l = 1
        while (linha <= i):
            q = (alfa[linha-1] * resto_lm[posicao-k] - quociente[posicao-l])//resto_lm[posicao-l]
            alfa.append(q)
            k+=2
            l+=2
            linha +=1
        print(alfa) 
    return a

def metade_restos (resto_l, rn):
    resto_lm = [int(linha) // rn for linha in resto_l]
    return resto_lm
    
mm = mdc(796, 518)
print ("MDC :", mm)