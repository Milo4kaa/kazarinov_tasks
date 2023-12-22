test_string = '''
32
30
31
34
38
37
39
0
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp


def calculate_profit(prices):
    buy_price = 0
    sell_price = 0
    profit = 0

    for i in range(1, len(prices) - 1):
        if prices[i] > prices[i - 1]:
            buy_price = prices[i]
            break

    for j in range(i, len(prices) - 1):
        if prices[j] < prices[j - 1]:
            sell_price = prices[j - 1]
            break

    profit = sell_price - buy_price

    return buy_price, sell_price, profit


prices = []
while True:
    price = int(input("Введите цену акции (для завершения введите 0): "))
    if price == 0:
        break
    prices.append(price)

buy_price, sell_price, profit = calculate_profit(prices)
print(f"Цена покупки: {buy_price}, Цена продажи: {sell_price}, Выгода: {profit}")