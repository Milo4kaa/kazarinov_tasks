word = input('Введите слово: ')
number = int(input('Введите номер: '))
if number <= len(word):
    print(word[number - 1])
else:
    print('Ошибка')