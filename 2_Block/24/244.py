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