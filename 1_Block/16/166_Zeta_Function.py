for n in range(1,10):
    i = 1
    sum = 0
    while i <= n:
        sum += 1 / (i ** 2)
        i += 1
    result = 3.141592653589793 ** 2 / sum

    print(f"Результат числа {n}: {result}")
