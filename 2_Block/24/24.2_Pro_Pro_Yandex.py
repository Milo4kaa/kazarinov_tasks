test_string = '''
8
сериал шерлок смотреть онлайн
учебник питона
мемы
социальная сеть
упражнения по питону
кормовые мыши для питонов
ответы егэ скачать бесплатно
компьютерные мыши
питон
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

list = list()
number = int(input('Введите количество строк: '))
for i in range(number):
    str = input('Введите строку: ')
    list.append(str)
find = input('Введите поисковую строку: ')
for i in list:
    if find in i:
        print(i)