def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_cases():
    n = 2
    while True:
        k = 0
        while k <= n:
            num = 2*n + 1 + 2**k
            if is_prime(num):
                print(f"n = {n}, k = {k}, 2n+1 + 2^k = {num} PRIMO")
            k += 1
        n += 1

find_cases()