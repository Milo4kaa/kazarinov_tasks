test_string = '''
привет
-100
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

word = input('Введите слово: ')
number = int(input('Введите номер: '))
if number <= len(word) <= number:
    print(word[number - 1])
else:
    print('Ошибка')