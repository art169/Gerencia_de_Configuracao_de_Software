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

# Teste
num = int(input("Digite um número inteiro positivo: "))
if is_prime(num):
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")
