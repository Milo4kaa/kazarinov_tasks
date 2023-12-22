def monkey_games(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + monkey_games(n // 2)
    else:
        return 1 + monkey_games(n - 1)
print("Введите количество камней: ")
results = []
for n in range(1, 20):
    steps = monkey_games(n)
    results.append((n, steps))
for result in results:
    print(f"Число: {result[0]}, Минимальное количество действий: {result[1]}")

