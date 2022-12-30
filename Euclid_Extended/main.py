def eh_par(n):
    if (n % 2) == 0:
        return False
    else:
        return True

def calcula_alfa (alfa_ant, resto_lm, quociente, k, l, n):
    alfa_i = 0
    alfa_i = (alfa_ant * (resto_lm[n]) - quociente[n])//resto_lm[n]
    print ((alfa_ant * (resto_lm[n]))-quociente[n])
    return alfa_i

def mdc(a, b):
    resto = 1
    resto_l = []
    quociente = []
    alfa  = []
    n = -2
    resto_l.append(a)
    resto_l.append(b)
    
    while (resto != 0):
        resto = a % b
        resto_l.append(resto)
        quociente.append(a//b)
        a = b
        b = resto
        n+=1
    print (resto_l)
    print ("N: ", n)
    
    resto_lm = metade_restos(resto_l)
    alfa = []

    if (eh_par(n)):
        i = n // 2
        alfa.append(1)
        linha = 0
        k = 2
        l = 0    
        while (linha <= i):
            q = calcula_alfa(alfa[linha], resto_lm, quociente, k, l, n)
            alfa.append(q)
            k+=2
            l+=2
            linha +=1
    else:
        i = (n-1)// 2
        alfa.append(1)
        linha = 0
        k = 3
        l = 1   
        while (linha <= i):
            q = calcula_alfa(alfa[linha], resto_lm, quociente, k, l, n)
            alfa.append(q)
            k+=2
            l+=2
            linha +=1
    return a

def metade_restos (resto_l):
    resto_lm = [int(linha) // 2 for linha in resto_l]
    return resto_lm
    

mm = mdc(796, 518)
print ("MDC :", mm)