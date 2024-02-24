test_string = '''
4
картину
корзину
картонку
маленькую собачонку
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

basket = list()
number = int(input('Введите количество покупок: '))
for i in range(number):
    buy = input('Введите товар для добавления в корзину: ')
    basket.append(buy)
for i in basket:
    print(i)