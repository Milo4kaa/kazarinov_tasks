for n in range(0,20):
    divisors = []
    for i in range(2, int(n**.5)):
        if n % i == 0:
            divisors.append(i)
    if len(divisors) == 2:
        print(*divisors, "ПРОСТОЕ")
    else:
        print(*divisors, "НЕТ")