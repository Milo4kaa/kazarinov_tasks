test_string = '''
1
учебники
4
учебники
скачать бесплатно реферат
как обойти фильтр поисковых запросов
учебники
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

white = list()
str = list()
num = int(input('Введите количество пунктов белого списка: '))
for i in range(num):
    wrds = input('Введите запрос белого списка: ')
    white.append(wrds)
num1 = int(input('Введите количество пунктов: '))
for i in range(num1):
    wrd = input('Введите запрос: ')
    str.append(wrd)
for i in str:
    if i in white:
        print(i)