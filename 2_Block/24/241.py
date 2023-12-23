basket = list()
number = int(input('Введите количество покупок: '))
for i in range(number):
    buy = input('Введите товар для добавления в корзину: ')
    basket.append(buy)
for i in basket:
    print(i)