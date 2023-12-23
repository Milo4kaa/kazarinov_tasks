test_string = '''
8
Лондон
Париж
Москва
Вашингтон
Берлин
Вена
Мадрид
Рим
Мадрид
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

kolv = int(input('Введите количество названных городов: '))
cities = set()
for i in range(kolv):
    citi = input('Введите город: ')
    cities.add(citi)
city = input('Введите последний город: ')
if city in cities:
    print('TRY ANOTHER')
else:
    print('OK')