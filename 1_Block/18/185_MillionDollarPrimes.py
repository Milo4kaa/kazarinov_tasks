def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers_less_than_n(n):
    prime_list = []
    for number in range(2, n):
        if is_prime(number):
            prime_list.append(number)
    return prime_list

for n in range(1, 20):
    result = prime_numbers_less_than_n(n)
    print("Простые числа, меньшие", n, ":", result,)
