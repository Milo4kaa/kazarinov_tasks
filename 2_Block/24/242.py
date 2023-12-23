list = list()
number = int(input('Введите количество строк: '))
for i in range(number):
    str = input('Введите строку: ')
    list.append(str)
find = input('Введите поисковую строку: ')
for i in list:
    if find in i:
        print(i)